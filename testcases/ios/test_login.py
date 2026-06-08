"""
iOS 登录功能回归测试用例
"""
import allure
import pytest

from pages.ios.login_page import IOSLoginPage
from pages.ios.home_page import IOSHomePage
from utils.logger import get_logger

log = get_logger("TestIOSLogin")


@allure.feature("登录模块")
@allure.story("iOS 登录")
@pytest.mark.ios
@pytest.mark.regression
class TestIOSLogin:
    """iOS 登录功能回归测试"""

    @pytest.fixture(autouse=True)
    def setup(self, poco):
        self.login_page = IOSLoginPage(poco=poco)

    @allure.title("iOS 正常登录")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.p0
    @pytest.mark.smoke
    def test_login_success(self):
        """验证 iOS 正常登录流程"""
        self.login_page.login("testuser", "testpass123")

        home_page = IOSHomePage(poco=self.login_page._poco)
        assert home_page.is_home_page_displayed(), "登录后应跳转到首页"

    @allure.title("iOS 登录失败 - 错误密码")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_login_with_wrong_password(self):
        """验证错误密码无法登录"""
        self.login_page.login("testuser", "wrong_password")
        assert self.login_page.is_login_page_displayed(), "登录失败应停留在登录页面"
