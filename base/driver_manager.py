"""
设备驱动管理器
管理 Android/iOS 设备的连接、断开和设备池，支持多设备并发
"""
import threading
from typing import Optional
from airtest.core.api import connect_device, device as current_device
from airtest.core.android.android import Android
from airtest.core.ios.ios import IOS

from config.settings import (
    get_android_devices,
    get_ios_devices,
    get_timeout,
)
from utils.logger import get_logger

log = get_logger("DriverManager")


class DeviceInfo:
    """设备信息封装"""

    def __init__(self, platform: str, serial: str = "", uuid: str = "", name: str = ""):
        self.platform = platform  # android / ios
        self.serial = serial      # Android 设备序列号
        self.uuid = uuid          # iOS 设备 UUID
        self.name = name or serial or uuid
        self._dev = None          # airtest 设备实例

    @property
    def uri(self) -> str:
        """获取 airtest 连接 URI"""
        if self.platform == "android":
            return f"Android:///{self.serial}"
        elif self.platform == "ios":
            return f"iOS:///{self.uuid}"
        return ""

    @property
    def device(self):
        return self._dev

    @device.setter
    def device(self, dev):
        self._dev = dev

    def __repr__(self):
        return f"DeviceInfo({self.platform}, {self.name}, {self.serial or self.uuid})"


class DriverManager:
    """
    设备驱动管理器（单例模式）

    核心功能:
    - 初始化设备连接池
    - 按序分配设备给 worker
    - 管理设备连接/断开生命周期
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._device_pool: list[DeviceInfo] = []
        self._allocated: dict[int, DeviceInfo] = {}  # worker_id -> DeviceInfo
        self._allocation_lock = threading.Lock()
        self._init_device_pool()

    def _init_device_pool(self):
        """根据配置初始化设备池"""
        # Android 设备
        for dev_conf in get_android_devices():
            serial = dev_conf.serial if hasattr(dev_conf, "serial") else ""
            name = dev_conf.name if hasattr(dev_conf, "name") else serial
            if serial:
                self._device_pool.append(
                    DeviceInfo(platform="android", serial=serial, name=name)
                )

        # iOS 设备
        for dev_conf in get_ios_devices():
            uuid = dev_conf.uuid if hasattr(dev_conf, "uuid") else ""
            name = dev_conf.name if hasattr(dev_conf, "name") else uuid
            if uuid:
                self._device_pool.append(
                    DeviceInfo(platform="ios", uuid=uuid, name=name)
                )

        log.info(f"设备池初始化完成，共 {len(self._device_pool)} 台设备: {self._device_pool}")

    def connect_device(self, device_info: DeviceInfo):
        """
        连接指定设备

        Args:
            device_info: 设备信息对象
        """
        try:
            dev = connect_device(device_info.uri)
            device_info.device = dev
            log.info(f"设备连接成功: {device_info}")
            return dev
        except Exception as e:
            log.error(f"设备连接失败: {device_info}, 错误: {e}")
            raise

    def allocate_device(self, worker_id: int) -> DeviceInfo:
        """
        为指定 worker 分配设备（线程安全）

        Args:
            worker_id: worker 编号

        Returns:
            分配的设备信息对象
        """
        with self._allocation_lock:
            if worker_id in self._allocated:
                return self._allocated[worker_id]

            for device_info in self._device_pool:
                already_allocated = device_info in self._allocated.values()
                if not already_allocated:
                    self._allocated[worker_id] = device_info
                    self.connect_device(device_info)
                    log.info(f"Worker-{worker_id} 分配设备: {device_info}")
                    return device_info

            # 如果设备都分配完了，循环分配（多个 worker 共享设备）
            if self._device_pool:
                device_info = self._device_pool[worker_id % len(self._device_pool)]
                self._allocated[worker_id] = device_info
                if not device_info.device:
                    self.connect_device(device_info)
                log.warning(f"Worker-{worker_id} 复用设备: {device_info}")
                return device_info

            raise RuntimeError("设备池为空，无法分配设备")

    def release_device(self, worker_id: int):
        """
        释放 worker 占用的设备

        Args:
            worker_id: worker 编号
        """
        with self._allocation_lock:
            if worker_id in self._allocated:
                device_info = self._allocated.pop(worker_id)
                log.info(f"Worker-{worker_id} 释放设备: {device_info}")

    def get_allocated_device(self, worker_id: int) -> Optional[DeviceInfo]:
        """获取 worker 已分配的设备"""
        return self._allocated.get(worker_id)

    @property
    def device_count(self) -> int:
        """设备池中的设备数量"""
        return len(self._device_pool)

    def cleanup(self):
        """清理所有设备连接"""
        for device_info in self._allocated.values():
            try:
                if device_info.device:
                    # airtest 没有显式 disconnect，这里做清理记录
                    log.info(f"清理设备连接: {device_info}")
            except Exception as e:
                log.error(f"清理设备连接异常: {e}")
        self._allocated.clear()
        log.info("所有设备连接已清理")


# 全局管理器实例
driver_manager = DriverManager()
