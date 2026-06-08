"""
iOS 登录页面对象
示例: 演示 iOS 页面对象封装
"""
import allure

from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("IOSLoginPage")


class IOSLoginPage(BasePage):
    """
    iOS 登录页面

    iOS 主要使用 Poco UI树定位，
    也可配合 airtest 图像识别作为补充
    """

    def __init__(self, poco=None):
        super().__init__(poco=poco)

    @allure.step("输入用户名: {username}")
    def input_username(self, username: str):
        """输入用户名"""
        if self._poco:
            self.poco_set_text("username_field", username)
        else:
            log.info(f"输入用户名: {username}")

    @allure.step("输入密码")
    def input_password(self, password: str):
        """输入密码"""
        if self._poco:
            self.poco_set_text("password_field", password)
        else:
            log.info("输入密码: ******")

    @allure.step("点击登录按钮")
    def click_login_button(self):
        """点击登录按钮"""
        if self._poco:
            self.poco_click("login_button")
        else:
            log.info("点击登录按钮")

    @allure.step("执行登录流程")
    def login(self, username: str, password: str):
        """完整登录流程"""
        log.info(f"iOS 执行登录: {username}")
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

    @allure.step("验证登录页面已加载")
    def is_login_page_displayed(self) -> bool:
        """检查登录页面是否已显示"""
        if self._poco:
            try:
                return self.poco()("login_button").exists()
            except Exception:
                pass
        return False
