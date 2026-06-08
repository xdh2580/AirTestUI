"""
APP 启停管理器
负责 APP 的启动、重启、关闭等生命周期管理
"""
from airtest.core.api import (
    start_app,
    stop_app,
    clear_app,
    install,
    shell,
    device as current_device,
)

from config.settings import get_android_app, get_ios_app, get_timeout
from utils.logger import get_logger

log = get_logger("AppLauncher")


class AppLauncher:
    """
    APP 启停管理器

    支持功能:
    - 启动 APP（自动区分 Android/iOS）
    - 关闭 APP
    - 重启 APP
    - 清除 APP 数据
    - 安装 APP（可选）
    """

    def __init__(self, platform: str = "android"):
        """
        Args:
            platform: 平台类型 android / ios
        """
        self.platform = platform
        if platform == "android":
            app_conf = get_android_app()
            self.package = app_conf.get("package", "") if hasattr(app_conf, "package") else ""
            self.activity = app_conf.get("activity", "") if hasattr(app_conf, "activity") else ""
            self.install_path = app_conf.get("install_path", "") if hasattr(app_conf, "install_path") else ""
        else:
            app_conf = get_ios_app()
            self.package = app_conf.get("bundle_id", "") if hasattr(app_conf, "bundle_id") else ""
            self.activity = ""
            self.install_path = app_conf.get("install_path", "") if hasattr(app_conf, "install_path") else ""

    def launch(self):
        """启动 APP"""
        if not self.package:
            log.error("APP 包名/Bundle ID 未配置")
            return

        try:
            # 可选：安装 APP
            if self.install_path:
                self._install_if_needed()

            log.info(f"启动 APP: {self.package}")
            if self.platform == "android" and self.activity:
                start_app(self.package, self.activity)
            else:
                start_app(self.package)

            # 等待 APP 启动
            app_timeout = get_timeout("app_launch")
            import time
            time.sleep(3)  # 基础等待
            log.info(f"APP 启动成功: {self.package}")

        except Exception as e:
            log.error(f"APP 启动失败: {e}")
            raise

    def close(self):
        """关闭 APP"""
        if not self.package:
            return
        try:
            stop_app(self.package)
            log.info(f"APP 已关闭: {self.package}")
        except Exception as e:
            log.error(f"APP 关闭失败: {e}")

    def restart(self):
        """重启 APP"""
        log.info(f"重启 APP: {self.package}")
        self.close()
        import time
        time.sleep(2)
        self.launch()

    def clear_data(self):
        """清除 APP 数据（仅 Android）"""
        if self.platform != "android":
            log.warning("清除数据仅支持 Android 平台")
            return
        try:
            clear_app(self.package)
            log.info(f"APP 数据已清除: {self.package}")
        except Exception as e:
            log.error(f"清除 APP 数据失败: {e}")

    def _install_if_needed(self):
        """如果配置了安装路径，执行安装"""
        if not self.install_path:
            return
        try:
            install(self.install_path)
            log.info(f"APP 安装完成: {self.install_path}")
        except Exception as e:
            log.error(f"APP 安装失败: {e}")
            raise

    def is_app_running(self) -> bool:
        """检查 APP 是否在运行"""
        try:
            if self.platform == "android":
                result = shell(f"dumpsys window | grep mCurrentFocus")
                return self.package in result
            else:
                # iOS 检测方式有限，默认返回 True
                return True
        except Exception:
            return False
