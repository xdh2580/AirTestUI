"""
Page Object 基类
封装 airtest / poco 核心操作，提供统一的页面对象交互接口
支持图像识别 + UI 树定位双模式
"""
import time
import allure

from airtest.core.api import (
    touch,
    swipe,
    wait,
    exists,
    assert_exists,
    assert_not_exists,
    sleep,
    snapshot,
)
from airtest.core.assertions import assert_equal, assert_not_equal
from airtest.core.helper import G
from poco.proxy import UIObjectProxy

from config.settings import get_timeout, settings, ROOT_DIR
from utils.logger import get_logger
from utils.screenshot import take_screenshot, attach_screenshot_to_allure, image_diff_ratio

log = get_logger("BasePage")


class BasePage:
    """
    Page Object 基类

    所有页面对象应继承此类，通过封装后的方法进行 UI 操作。
    内置智能等待、自动截图、操作日志、Allure 步骤记录。

    用法:
        class LoginPage(BasePage):
            def __init__(self):
                super().__init__()
                self.btn_login = Template("resources/android/btn_login.png")

            def login(self, username, password):
                self.input_text(username, self.input_username)
                self.input_text(password, self.input_password)
                self.click(self.btn_login)
    """

    def __init__(self, poco=None):
        """
        Args:
            poco: Poco 实例，用于 UI 树定位。为空则仅使用图像识别模式
        """
        self._poco = poco
        self._timeout = get_timeout("element_wait")
        self._page_load_timeout = get_timeout("page_load")

    # ==================== 图像识别操作 ====================

    @allure.step("点击元素: {target}")
    def click(self, target, **kwargs):
        """
        点击目标（图像识别）

        Args:
            target: airtest Template 对象 或 坐标元组
        """
        log.info(f"点击: {target}")
        try:
            touch(target, **kwargs)
        except Exception as e:
            log.error(f"点击失败: {target}, 错误: {e}")
            take_screenshot(f"click_fail_{target}")
            raise

    @allure.step("等待元素出现: {target}")
    def wait_for_element(self, target, timeout=None, interval=0.5):
        """
        等待元素出现

        Args:
            target: Template 对象
            timeout: 超时时间（秒），默认使用全局配置
            interval: 检查间隔

        Returns:
            元素坐标
        """
        timeout = timeout or self._timeout
        log.info(f"等待元素: {target}, 超时: {timeout}s")
        try:
            pos = wait(target, timeout=timeout, interval=interval)
            return pos
        except Exception as e:
            log.error(f"等待元素超时: {target}")
            take_screenshot(f"wait_timeout_{target}")
            raise

    @allure.step("判断元素是否存在: {target}")
    def is_exists(self, target) -> bool:
        """
        判断元素是否存在（不抛异常）

        Args:
            target: Template 对象

        Returns:
            bool
        """
        return exists(target)

    @allure.step("断言元素存在: {target}")
    def assert_element_exists(self, target, msg=""):
        """断言元素存在"""
        log.info(f"断言元素存在: {target}")
        try:
            assert_exists(target, msg or f"元素应存在: {target}")
        except AssertionError:
            take_screenshot(f"assert_exists_fail_{target}")
            raise

    @allure.step("断言元素不存在: {target}")
    def assert_element_not_exists(self, target, msg=""):
        """断言元素不存在"""
        log.info(f"断言元素不存在: {target}")
        assert_not_exists(target, msg or f"元素不应存在: {target}")

    @allure.step("滑动: {direction}")
    def swipe_screen(self, direction: str = "up", duration=0.5):
        """
        屏幕滑动

        Args:
            direction: 滑动方向 up/down/left/right
            duration: 滑动持续时间
        """
        log.info(f"滑动: {direction}")

        # 获取屏幕尺寸
        w, h = self._get_screen_size()

        cx, cy = w // 2, h // 2
        offset = min(w, h) // 3

        directions = {
            "up": (cx, cy + offset, cx, cy - offset),
            "down": (cx, cy - offset, cx, cy + offset),
            "left": (cx + offset, cy, cx - offset, cy),
            "right": (cx - offset, cy, cx + offset, cy),
        }

        if direction not in directions:
            raise ValueError(f"不支持的滑动方向: {direction}")

        start_x, start_y, end_x, end_y = directions[direction]
        swipe((start_x, start_y), (end_x, end_y), duration=duration)

    @allure.step("点击相对坐标")
    def click_by_ratio(self, rx: float, ry: float):
        """
        按页面相对坐标点击

        Args:
            rx: 水平相对位置 (0.0~1.0, 0.0=左边缘, 1.0=右边缘)
            ry: 垂直相对位置 (0.0~1.0, 0.0=顶部, 1.0=底部)

        用法:
            self.click_by_ratio(0.5, 0.3)   # 屏幕水平居中、上方30%处点击
            self.click_by_ratio(0.85, 0.92) # 右下角附近点击
        """
        w, h = self._get_screen_size()
        x, y = int(w * rx), int(h * ry)
        log.info(f"点击相对坐标: ({rx:.2f}, {ry:.2f}) -> 像素 ({x}, {y}) / ({w}x{h})")
        allure.attach(f"相对坐标: x={rx:.3f}, y={ry:.3f} | 像素: ({x}, {y}) | 屏幕: {w}x{h}",
                      name="坐标详情", attachment_type=allure.attachment_type.TEXT)
        touch((x, y))

    @allure.step("输入文本: {text}")
    def input_text(self, text: str, target=None, enter=False):
        """
        输入文本

        Args:
            text: 要输入的文本
            target: 目标元素，为空则直接输入到当前焦点
            enter: 输入后是否按回车
        """
        log.info(f"输入文本: {text}")
        if target:
            touch(target)
            sleep(0.5)

        from airtest.core.api import text as airtest_text
        airtest_text(text)

        if enter:
            from airtest.core.api import keyevent
            keyevent("ENTER")

    # ==================== Poco UI树操作 ====================

    def poco(self):
        """获取 Poco 实例"""
        if self._poco is None:
            raise RuntimeError("Poco 未初始化，请在构造函数中传入 poco 实例")
        return self._poco

    @allure.step("Poco点击: {name}")
    def poco_click(self, name_or_proxy, timeout=None):
        """
        通过 Poco 点击元素（UI树定位）

        Args:
            name_or_proxy: Poco UIObjectProxy 或 节点名
            timeout: 等待超时
        """
        timeout = timeout or self._timeout
        element = self._resolve_poco_element(name_or_proxy, timeout)
        log.info(f"Poco点击: {name_or_proxy}")
        element.click()

    @allure.step("Poco输入文本: {text}")
    def poco_set_text(self, name_or_proxy, text: str, timeout=None):
        """
        通过 Poco 设置文本

        Args:
            name_or_proxy: Poco 元素或节点名
            text: 要设置的文本
            timeout: 等待超时
        """
        timeout = timeout or self._timeout
        element = self._resolve_poco_element(name_or_proxy, timeout)
        log.info(f"Poco输入: {name_or_proxy} -> {text}")
        element.set_text(text)

    @allure.step("Poco获取文本")
    def poco_get_text(self, name_or_proxy, timeout=None) -> str:
        """获取元素的文本属性"""
        timeout = timeout or self._timeout
        element = self._resolve_poco_element(name_or_proxy, timeout)
        return element.get_text()

    @allure.step("Poco等待元素: {name_or_proxy}")
    def poco_wait_for_element(self, name_or_proxy, timeout=None) -> UIObjectProxy:
        """等待 Poco 元素出现"""
        timeout = timeout or self._timeout
        return self._resolve_poco_element(name_or_proxy, timeout)

    @allure.step("Poco断言元素存在: {name_or_proxy}")
    def poco_assert_exists(self, name_or_proxy, msg="", timeout=None):
        """断言 Poco 元素存在"""
        timeout = timeout or self._timeout
        try:
            element = self._resolve_poco_element(name_or_proxy, timeout)
            assert element.exists(), msg or f"Poco元素应存在: {name_or_proxy}"
        except (AssertionError, Exception) as e:
            take_screenshot(f"poco_assert_exists_fail")
            raise

    @allure.step("Poco断言文本: {expected}")
    def poco_assert_text(self, name_or_proxy, expected: str, timeout=None):
        """断言 Poco 元素的文本内容"""
        timeout = timeout or self._timeout
        element = self._resolve_poco_element(name_or_proxy, timeout)
        actual = element.get_text()
        log.info(f"Poco断言文本: 期望='{expected}', 实际='{actual}'")
        assert_equal(actual, expected, f"文本断言: {name_or_proxy}")

    # ==================== 通用断言 ====================

    @allure.step("断言相等")
    def assert_equal(self, actual, expected, msg=""):
        assert_equal(actual, expected, msg or f"期望 {expected}, 实际 {actual}")

    @allure.step("断言不相等")
    def assert_not_equal(self, actual, expected, msg=""):
        assert_not_equal(actual, expected, msg or f"不应等于 {expected}")

    @allure.step("断言为真: {msg}")
    def assert_true(self, condition, msg=""):
        assert condition, msg or f"条件应为 True"

    @allure.step("断言包含")
    def assert_contains(self, container, item, msg=""):
        assert item in container, msg or f"{item} 应在 {container} 中"

    # ==================== 工具方法 ====================
    @allure.step("点击复选框")
    def click_checkbox(self):
        """点击复选框"""
        from airtest.core.api import Template, touch, wait
        log.info("点击复选框")
        check_box = Template(self.resource_path("common/复选框.png"))
        wait(check_box, timeout=5)
        touch(check_box)

    @allure.step("点击返回箭头")
    def click_back_arrow(self):
        """点击返回箭头"""
        from airtest.core.api import Template, touch, wait
        log.info("点击返回箭头")
        arrow_back = Template(self.resource_path("common/返回箭头.png"))
        wait(arrow_back, timeout=5)
        touch(arrow_back)

    @allure.step("重新进入小程序首页")
    def reload_miniapp(self):
        """
        通过小程序菜单「重新进入」回到小程序首页。
        适用于任何页面需要回到首页的场景。
        """
        from airtest.core.api import Template, touch, wait
        log.info("通过小程序菜单重新进入首页")
        btn_menu = Template(
            self.resource_path("common/小程序菜单.png"))
        wait(btn_menu, timeout=15)
        touch(btn_menu)
        btn_reload = Template(
            self.resource_path("common/重新进入.png"))
        wait(btn_reload, timeout=15)
        touch(btn_reload)
        self.wait_seconds(3)

    def _get_screen_size(self):
        """获取当前设备屏幕分辨率 (宽, 高)"""
        device = G.DEVICE
        if device:
            return device.get_current_resolution()
        return 1080, 1920

    @allure.step("截取区域: ({x}, {y}, {w}x{h})")
    def capture_area(self, x: int, y: int, w: int, h: int, name: str = "") -> str:
        """
        截取屏幕指定区域并保存为图片

        Args:
            x, y: 区域左上角坐标（像素）
            w, h: 区域宽高（像素）
            name: 截图名称，用于生成文件名

        Returns:
            截图文件绝对路径
        """
        import os
        from PIL import Image

        ts = int(time.time() * 1000)
        # 截全屏 → 裁剪 → 删全屏临时图
        full_path = str(ROOT_DIR / "screenshots" / f"_tmp_full_{ts}.png")
        snapshot(full_path)

        img = Image.open(full_path)
        cropped = img.crop((x, y, x + w, y + h))

        label = name or f"area_{x}_{y}_{w}_{h}"
        crop_path = str(ROOT_DIR / "screenshots" / f"diff_{label}_{ts}.png")
        cropped.save(crop_path)
        log.info(f"区域截图已保存: {crop_path}")

        try:
            os.remove(full_path)
        except OSError:
            pass
        return crop_path

    @allure.step("断言区域({x},{y},{w}x{h})发生变化")
    def assert_area_changed(self, x: int, y: int, w: int, h: int, action,
                            threshold: float = 0.10, msg: str = ""):
        """
        截取指定区域 → 执行 action → 再次截取 → 断言变化超过阈值

        Args:
            x, y, w, h: 截取区域
            action:   无参可调用对象，执行触发变化的操作
            threshold: 差异阈值（默认 10%）
            msg:      断言失败时的提示信息
        """
        before = self.capture_area(x, y, w, h, name="before")
        action()
        self.wait_seconds(2)
        after = self.capture_area(x, y, w, h, name="after")
        diff = image_diff_ratio(before, after)

        # 对比完清理截图，避免文件堆积
        import os as _os
        for p in (before, after):
            try:
                _os.remove(p)
            except OSError:
                pass

        assert diff > threshold, (
            msg or f"区域应发生变化，但差异仅 {diff:.1%}（阈值 {threshold:.0%}）"
        )
        log.info(f"区域变化断言通过: {diff:.1%} > {threshold:.0%}")

    @allure.step("等待: {seconds}秒")
    def wait_seconds(self, seconds: float = 1.0):
        """显式等待"""
        sleep(seconds)

    @allure.step("截图")
    def take_page_screenshot(self, name: str = "page"):
        """截图当前页面"""
        filepath = take_screenshot(name)
        if filepath:
            attach_screenshot_to_allure(name, filepath)
        return filepath

    def _resolve_poco_element(self, name_or_proxy, timeout=10) -> UIObjectProxy:
        """
        解析 Poco 元素

        Args:
            name_or_proxy: 字符串节点名 或 UIObjectProxy 实例
            timeout: 等待超时

        Returns:
            UIObjectProxy 实例
        """
        if isinstance(name_or_proxy, UIObjectProxy):
            return name_or_proxy

        if isinstance(name_or_proxy, str):
            element = self.poco()(name_or_proxy)
            element.wait_for_appearance(timeout=timeout)
            return element

        raise TypeError(f"不支持的元素类型: {type(name_or_proxy)}")

    @staticmethod
    def resource_path(relative_path: str) -> str:
        """
        获取资源文件的绝对路径

        Args:
            relative_path: 相对于 resources/ 目录的路径

        用法:
            Template(BasePage.resource_path("android/btn_login.png"))
        """
        return str(ROOT_DIR / "resources" / relative_path)
