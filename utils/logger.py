"""
日志模块
基于 loguru 实现结构化日志，支持文件轮转和多级别输出
"""
import sys
import os
from pathlib import Path
from loguru import logger

from config.settings import ROOT_DIR

# 日志目录
LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# 移除默认 handler
logger.remove()

# ---- Windows 编码修复 ----
# loguru 在 Windows 上通过 colorama 将 stderr 包装为 AnsiToWin32，
# 该包装会丢失 UTF-8 编码导致中文乱码。
# 解决：创建自定义 sink，直接以 UTF-8 字节写入 stdout.buffer。
if sys.platform == "win32":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

    def _utf8_console_sink(message):
        """绕过 colorama，直接以 UTF-8 写入 stdout"""
        line = str(message) + "\n"
        try:
            sys.stdout.buffer.write(line.encode("utf-8"))
            sys.stdout.buffer.flush()
        except Exception:
            pass

    console_sink = _utf8_console_sink
else:
    console_sink = sys.stderr

# 控制台输出（Windows 下关掉 colorize，因为自定义 sink 不支持 ANSI 颜色）
logger.add(
    console_sink,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
    colorize=sys.platform != "win32",
)

# ---- 全量日志文件 ----
logger.add(
    str(LOG_DIR / "airtestui_{time:YYYY-MM-DD}.log"),
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    rotation="20 MB",
    retention="7 days",
    compression="zip",
)

# ---- 错误日志文件 ----
logger.add(
    str(LOG_DIR / "error_{time:YYYY-MM-DD}.log"),
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
    level="ERROR",
    rotation="20 MB",
    retention="30 days",
    compression="zip",
)


def get_logger(name: str = "AirTestUI"):
    """
    获取带模块标识的 logger

    用法:
        log = get_logger("LoginPage")
        log.info("用户点击登录按钮")
    """
    return logger.bind(name=name)
