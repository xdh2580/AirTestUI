"""
全局配置管理模块
读取 config.yaml 并暴露为全局配置对象，支持环境变量覆盖
"""
import os
import yaml
from pathlib import Path


# 项目根目录
ROOT_DIR = Path(__file__).resolve().parent.parent


def _load_yaml(path: str) -> dict:
    """加载 YAML 配置文件"""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _merge_env_override(config: dict) -> dict:
    """
    环境变量覆盖机制
    规则: AIRTESTUI_<大写键名> 会覆盖 config.yaml 中的顶层配置
    例如: AIRTESTUI_ENV=production 会覆盖 config.env
    """
    prefix = "AIRTESTUI_"
    for key, value in os.environ.items():
        if key.startswith(prefix):
            config_key = key[len(prefix):].lower()
            config[config_key] = value
    return config


# 加载主配置
_config_path = os.environ.get(
    "AIRTESTUI_CONFIG_PATH",
    str(ROOT_DIR / "config" / "config.yaml")
)
_raw_config = _load_yaml(_config_path)

# 加载本地覆盖配置（不纳入版本控制）
_local_config_path = ROOT_DIR / "config" / "local_config.yaml"
if _local_config_path.exists():
    _local = _load_yaml(str(_local_config_path))
    _raw_config.update(_local)

# 应用环境变量覆盖
_raw_config = _merge_env_override(_raw_config)


class _Config:
    """配置访问对象，支持属性和字典两种方式访问"""

    def __init__(self, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self, key, _Config(value))
            elif isinstance(value, list):
                setattr(self, key, [
                    _Config(item) if isinstance(item, dict) else item
                    for item in value
                ])
            else:
                setattr(self, key, value)

    def get(self, key, default=None):
        return getattr(self, key, default)

    def __getitem__(self, key):
        return getattr(self, key)

    def __contains__(self, key):
        return hasattr(self, key)

    def __repr__(self):
        return str(self.__dict__)


# 全局配置实例
settings = _Config(_raw_config)


# 便捷访问函数
def get_env() -> str:
    """获取当前运行环境"""
    return settings.get("env", "dev")


def get_timeout(category: str = "element_wait") -> int:
    """获取超时配置"""
    return settings.timeout.get(category, 10) if hasattr(settings, "timeout") else 10


def get_android_devices() -> list:
    """获取 Android 设备列表"""
    return settings.get("android", _Config({})).get("devices", [])


def get_ios_devices() -> list:
    """获取 iOS 设备列表"""
    return settings.get("ios", _Config({})).get("devices", [])


def get_android_app() -> _Config:
    """获取 Android APP 配置"""
    return settings.get("android", _Config({})).get("app", _Config({}))


def get_ios_app() -> _Config:
    """获取 iOS APP 配置"""
    return settings.get("ios", _Config({})).get("app", _Config({}))
