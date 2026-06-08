"""
Android 登录页面对象
示例: 演示如何使用 BasePage 封装页面对象
"""
import allure
from airtest.core.api import Template

from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("AndroidLoginPage")


class AndroidLoginPage(BasePage):
    """
    Android 登录页面

    演示两种元素定位方式:
    1. 图像识别: 使用 airtest Template
    2. UI树定位: 使用 Poco 节点名
    """

    def __init__(self, poco=None):
        super().__init__(poco=poco)

        # 图像识别元素（需要准备对应的截图文件放到 resources/android/ 目录）
        self._img_logo = Template(self.resource_path("android/img_login_logo.png"))
        self._btn_login = Template(self.resource_path("android/btn_login.png"))

    # ---- 页面操作 ----

    @allure.step("输入用户名: {username}")
    def input_username(self, username: str):
        """输入用户名"""
        if self._poco:
            self.poco_set_text("username_input", username)
        else:
            # Poco 节点名根据实际APP调整，这里使用图像识别兜底
            log.info(f"输入用户名: {username}")
            from airtest.core.api import touch, text
            # 点击用户名输入框区域（需根据实际APP调整坐标或图像）
            # touch(self._img_username_field)
            # text(username)

    @allure.step("输入密码")
    def input_password(self, password: str):
        """输入密码"""
        if self._poco:
            self.poco_set_text("password_input", password)
        else:
            log.info("输入密码: ******")

    @allure.step("点击登录按钮")
    def click_login_button(self):
        """点击登录按钮"""
        if self._poco:
            self.poco_click("login_button")
        else:
            self.click(self._btn_login)

    @allure.step("执行登录流程")
    def login(self, username: str, password: str):
        """
        完整登录流程

        Args:
            username: 用户名
            password: 密码
        """
        log.info(f"执行登录: {username}")
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

    # ---- 页面验证 ----

    @allure.step("验证登录页面已加载")
    def is_login_page_displayed(self) -> bool:
        """检查登录页面是否已显示"""
        if self._poco:
            try:
                return self.poco()("login_button").exists()
            except Exception:
                pass
        return self.is_exists(self._img_logo)

    @allure.step("验证登录错误提示")
    def get_error_message(self) -> str:
        """获取登录错误提示文本"""
        if self._poco:
            try:
                return self.poco_get_text("error_message")
            except Exception:
                pass
        return ""

    @allure.step("验证登录按钮是否可点击")
    def is_login_button_enabled(self) -> bool:
        """检查登录按钮是否可点击"""
        if self._poco:
            try:
                btn = self.poco()("login_button")
                return btn.exists() and btn.attr("enabled")
            except Exception:
                pass
        return True
