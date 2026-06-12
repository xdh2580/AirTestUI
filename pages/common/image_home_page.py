"""
纯图像识别登录页面对象
示例: 仅使用 airtest Template 图像识别，不依赖 Poco
适用于：游戏、WebView、无法获取 UI 树的场景
"""
import allure
from airtest.core.api import Template

from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("ImageHomePage")


class ImageHomePage(BasePage):
    """
    纯图像识别登录页面

    所有元素定位和交互均通过 airtest Template 完成，
    不使用任何 Poco UI 树操作。

    Template 参数说明:
    - filename: 截图文件路径
    - threshold: 识别阈值 (0~1)，默认 0.7，值越低匹配越宽松
    - target_pos: 目标点击偏移 (0~1)，0=左上, 1=右下, 默认 0.5(中心)
    - resolution: 模板截图时的设备分辨率，用于跨分辨率适配
    """

    def __init__(self):
        # 纯图像识别模式，不传入 poco
        super().__init__(poco=None)

        # ---------- 页面元素定义 ----------
        # 所有 Template 图像需提前截图保存到 resources/android/ 目录
        # threshold: 识别阈值，建议 0.6~0.8
        # target_pos: 点击偏移位置，0.5 为中心点

        # 附属卡tab Logo（用于验证页面是否加载）
        self.fushuka_logo = Template(
            self.resource_path("common/附属卡Tab.png"),
            threshold=0.8,
        )

        # 附属卡tab选中Logo（用于验证页面是否加载）
        self.fushuka_logo_selected = Template(
            self.resource_path("common/附属卡Tab-已选中.png"),
            threshold=0.8,
        )

        # # 用户名输入框图标（点击后激活输入框）
        # self.img_username_field = Template(
        #     self.resource_path("android/img_username_field.png"),
        #     threshold=0.7,
        #     target_pos=0.5,
        # )

        # # 密码输入框图标
        # self.img_password_field = Template(
        #     self.resource_path("android/img_password_field.png"),
        #     threshold=0.7,
        #     target_pos=0.5,
        # )

        # # 登录按钮
        # self.img_login_button = Template(
        #     self.resource_path("android/btn_login.png"),
        #     threshold=0.8,
        # )

        # # 登录错误提示区域（用于验证错误信息出现）
        # self.img_error_popup = Template(
        #     self.resource_path("android/img_error_popup.png"),
        #     threshold=0.6,  # 错误提示文字可能多变，阈值稍低
        # )

        # # 登录成功后的首页标志
        # self.img_home_indicator = Template(
        #     self.resource_path("android/img_home_tab.png"),
        #     threshold=0.7,
        # )

        # # "记住密码" 复选框
        # self.img_remember_checkbox = Template(
        #     self.resource_path("android/img_remember_unchecked.png"),
        #     threshold=0.7,
        #     target_pos=0.5,
        # )

    # ---- 页面操作 ----
    @allure.step("点击附属卡tab")
    def click_fushuka_tab(self):
        """点击附属卡tab"""
        log.info("点击附属卡tab")
        self.click(self.fushuka_logo)

    @allure.step("点击用户名输入框并输入: {username}")
    def input_username(self, username: str):
        """
        点击用户名输入框图像，激活输入焦点后输入文本

        图像识别流程:
        1. Template 匹配到用户名输入框图标
        2. touch 点击图标中心 (target_pos=0.5)
        3. airtest text() 输入文本
        """
        log.info(f"点击用户名输入框并输入: {username}")
        self.click(self.img_username_field)
        self.wait_seconds(0.5)  # 等待输入框激活
        self.input_text(username)

    @allure.step("点击密码输入框并输入密码")
    def input_password(self, password: str):
        """点击密码输入框并输入密码"""
        log.info("点击密码输入框并输入密码")
        self.click(self.img_password_field)
        self.wait_seconds(0.5)
        self.input_text(password)

    @allure.step("勾选记住密码")
    def check_remember_password(self):
        """勾选"记住密码"复选框"""
        log.info("勾选记住密码")
        self.click(self.img_remember_checkbox)

    @allure.step("点击登录按钮")
    def click_login(self):
        """点击登录按钮"""
        log.info("点击登录按钮")
        self.click(self.img_login_button)

    @allure.step("执行完整登录流程: {username}")
    def login(self, username: str, password: str, remember=False):
        """
        完整登录流程（纯图像识别）

        Args:
            username: 用户名
            password: 密码
            remember: 是否勾选记住密码
        """
        log.info(f"执行登录: {username}, 记住密码={remember}")
        self.input_username(username)
        self.input_password(password)
        if remember:
            self.check_remember_password()
        self.click_login()

    # ---- 页面验证 ----
    @allure.step("验证附属卡tab已加载")
    def is_fushuka_tab_loaded(self) -> bool:
        """
        通过图像识别判断附属卡tab是否已加载
        等待 Logo 图像出现，超时则返回 False
        """
        log.info("验证附属卡tab是否已加载 (图像识别)")
        return self.is_exists(self.fushuka_logo)

    @allure.step("验证home页面已加载")
    def is_home_page_loaded(self) -> bool:
        """
        通过图像识别判断登录页面是否已加载
        等待 附属卡Logo 图像出现，超时则返回 False
        """
        log.info("验证home页面是否已加载 (图像识别)")
        return self.is_exists(self.fushuka_logo)

    @allure.step("等待登录页面加载")
    def wait_home_page_loaded(self, timeout=15):
        """
        等待home页面完全加载（等待 Logo 出现）

        Args:
            timeout: 最大等待时间

        Returns:
            Logo 图像的坐标位置
        """
        log.info(f"等待home页面加载, 超时: {timeout}s")
        return self.wait_for_element(self.fushuka_logo, timeout=timeout)

    @allure.step("验证登录成功 - 首页已出现")
    def is_login_success(self) -> bool:
        """通过图像识别判断是否已进入首页"""
        log.info("验证是否登录成功 (图像识别首页标志)")
        return self.is_exists(self.img_home_indicator)

    @allure.step("等待登录成功跳转首页")
    def wait_login_success(self, timeout=20):
        """等待首页标志出现，确认登录成功"""
        log.info(f"等待登录成功跳转, 超时: {timeout}s")
        return self.wait_for_element(self.img_home_indicator, timeout=timeout)

    @allure.step("验证登录失败 - 错误提示出现")
    def is_error_popup_displayed(self) -> bool:
        """通过图像识别判断错误提示弹窗是否出现"""
        log.info("验证错误提示弹窗 (图像识别)")
        return self.is_exists(self.img_error_popup)

    @allure.step("断言登录页面已加载")
    def assert_home_page_loaded(self):
        """断言home页面已加载（严格断言，失败抛异常）"""
        self.assert_element_exists(self.fushuka_logo, "home页面应已加载")

    @allure.step("断言登录成功")
    def assert_login_success(self, timeout=20):
        """断言登录成功，等待首页标志出现"""
        self.wait_for_element(self.img_home_indicator, timeout=timeout)
        self.assert_element_exists(self.img_home_indicator, "登录成功后首页应出现")

    @allure.step("断言登录失败 - 错误提示出现")
    def assert_login_failed(self):
        """断言登录失败，错误提示弹窗出现"""
        self.assert_element_exists(self.img_error_popup, "登录失败应出现错误提示")

    @allure.step("断言登录失败 - 仍在登录页")
    def assert_still_on_login_page(self):
        """断言登录失败后仍在登录页面"""
        self.assert_element_exists(self.img_logo, "登录失败后应仍在登录页面")

    # ---- 图像识别特有操作 ----

    @allure.step("清除输入框内容 (逐字删除)")
    def clear_input_field(self, char_count: int = 20):
        """
        通过模拟键盘逐字删除输入框内容
        图像识别模式下无法直接获取输入框文本，
        通常采用多次按 Delete 键的方式清空

        Args:
            char_count: 最多删除的字符数（防止删太多）
        """
        from airtest.core.api import keyevent
        log.info(f"清除输入框, 最多删 {char_count} 个字符")
        for _ in range(char_count):
            keyevent("DEL")
        self.wait_seconds(0.3)

    @allure.step("滑动登录页面寻找元素")
    def swipe_to_find_element(self, target, direction="down", max_swipes=5, swipe_interval=1.0):
        """
        在页面上反复滑动，直到找到目标图像

        这是图像识别中常见的操作：某些元素不在当前可视区域，
        需要通过滑动才能出现。

        Args:
            target: Template 对象
            direction: 滑动方向
            max_swipes: 最大滑动次数
            swipe_interval: 每次滑动间隔

        Returns:
            找到返回坐标，未找到返回 None
        """
        log.info(f"滑动寻找元素: {target}, 方向: {direction}, 最大 {max_swipes} 次")
        for i in range(max_swipes):
            if self.is_exists(target):
                log.info(f"在第 {i} 次滑动后找到目标")
                return target
            self.swipe_screen(direction)
            self.wait_seconds(swipe_interval)

        log.warning(f"滑动 {max_swipes} 次后仍未找到目标: {target}")
        return None