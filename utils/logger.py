"""
日志模块
基于 loguru 实现结构化日志，支持文件轮转和多级别输出
"""
import sys
import os
from pathlib import Path
from loguru import logger

from config.settings import ROOT_DIR


# 修复 Windows 控制台中文编码问题
if sys.platform == "win32":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 日志目录
LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# 移除默认 handler
logger.remove()

# 控制台输出 - 彩色、简洁
logger.add(
    sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
    colorize=True,
)

# 全量日志文件 - DEBUG 级别，单文件最大 20MB，保留 7 天
logger.add(
    str(LOG_DIR / "airtestui_{time:YYYY-MM-DD}.log"),
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    rotation="20 MB",
    retention="7 days",
    compression="zip",
    encoding="utf-8",
)

# 错误日志文件 - 仅 ERROR 及以上
logger.add(
    str(LOG_DIR / "error_{time:YYYY-MM-DD}.log"),
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
    level="ERROR",
    rotation="20 MB",
    retention="30 days",
    compression="zip",
    encoding="utf-8",
)


def get_logger(name: str = "AirTestUI"):
    """
    获取带模块标识的 logger

    用法:
        log = get_logger("LoginPage")
        log.info("用户点击登录按钮")
    """
    return logger.bind(name=name)
