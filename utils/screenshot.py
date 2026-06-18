"""
截图工具模块
提供统一的截图保存、命名和 Allure 附件功能
"""
import time
from pathlib import Path

import allure
from airtest.core.api import snapshot

from config.settings import ROOT_DIR, settings
from utils.logger import get_logger

log = get_logger("Screenshot")


def get_screenshot_dir() -> Path:
    """获取截图保存目录"""
    save_dir = settings.get("screenshot", None)
    if save_dir and hasattr(save_dir, "save_dir"):
        dir_path = ROOT_DIR / save_dir.save_dir
    else:
        dir_path = ROOT_DIR / "screenshots"
    dir_path.mkdir(exist_ok=True)
    return dir_path


def take_screenshot(name: str = None, device=None) -> str:
    """
    截图并保存到本地

    Args:
        name: 截图名称前缀，为空则自动生成时间戳
        device: airtest 设备对象，为空则使用当前设备

    Returns:
        截图文件的绝对路径
    """
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png" if name else f"screenshot_{timestamp}.png"
    filepath = get_screenshot_dir() / filename

    try:
        if device:
            device.snapshot(str(filepath))
        else:
            snapshot(str(filepath))
        log.info(f"截图已保存: {filepath}")
        return str(filepath)
    except Exception as e:
        log.error(f"截图失败: {e}")
        return ""


def attach_screenshot_to_allure(name: str = "screenshot", filepath: str = None):
    """
    将截图附加到 Allure 报告

    Args:
        name: 附件名称
        filepath: 截图路径，为空则新截一张
    """
    if not filepath:
        filepath = take_screenshot(name)

    if filepath and Path(filepath).exists():
        with open(filepath, "rb") as f:
            allure.attach(
                f.read(),
                name=name,
                attachment_type=allure.attachment_type.PNG,
            )
        log.debug(f"截图已附加到 Allure: {name}")


def image_diff_ratio(img1_path: str, img2_path: str) -> float:
    """
    计算两张图片的像素差异比例

    Args:
        img1_path: 变更前截图路径
        img2_path: 变更后截图路径

    Returns:
        0.0 ~ 1.0，0 表示完全相同，1 表示完全不同
    """
    from PIL import Image
    import numpy as np

    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    if img1.size != img2.size:
        log.warning(f"图片尺寸不一致: {img1.size} vs {img2.size}，缩放后对比")
        img2 = img2.resize(img1.size)

    arr1 = np.array(img1, dtype=np.float32)
    arr2 = np.array(img2, dtype=np.float32)

    # 任一 RGB 通道差值 > 30 的像素视为"发生了变化"
    diff_mask = np.max(np.abs(arr1 - arr2), axis=2) > 30
    diff_pixels = int(np.sum(diff_mask))
    total_pixels = img1.size[0] * img1.size[1]

    ratio = diff_pixels / total_pixels
    log.info(f"图片差异比例: {ratio:.2%} ({diff_pixels}/{total_pixels})")
    return ratio


def screenshot_on_failure(func):
    """
    装饰器：函数执行失败时自动截图
    用于页面对象方法级别
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            func_name = func.__qualname__
            take_screenshot(f"failure_{func_name}")
            raise
    return wrapper
