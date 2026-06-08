"""
Android 登录功能回归测试用例
示例: 演示如何编写测试用例
"""
import allure
import pytest

from pages.android.login_page import AndroidLoginPage
from pages.android.home_page import AndroidHomePage
from utils.logger import get_logger
from utils.data_loader import parametrize_data

log = get_logger("TestAndroidLogin")


@allure.feature("登录模块")
@allure.story("Android 登录")
@pytest.mark.android
@pytest.mark.regression
class TestAndroidLogin:
    """Android 登录功能回归测试"""

    @pytest.fixture(autouse=True)
    def setup(self, poco):
        """每个用例前初始化页面对象"""
        self.login_page = AndroidLoginPage(poco=poco)

    @allure.title("正常登录 - 有效账号密码")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.p0
    @pytest.mark.smoke
    def test_login_success(self, app_launcher):
        """验证使用有效账号密码可以成功登录"""
        # When: 执行登录
        self.login_page.login("testuser", "testpass123")

        # Then: 验证首页已加载
        home_page = AndroidHomePage(poco=self.login_page._poco)
        assert home_page.is_home_page_displayed(), "登录后应跳转到首页"

    @allure.title("登录失败 - 错误密码")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_login_with_wrong_password(self):
        """验证使用错误密码登录失败"""
        # When: 使用错误密码登录
        self.login_page.login("testuser", "wrong_password")

        # Then: 验证仍在登录页面，且有错误提示
        assert self.login_page.is_login_page_displayed(), "登录失败应停留在登录页面"

    @allure.title("登录失败 - 空用户名")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_login_with_empty_username(self):
        """验证空用户名无法登录"""
        # When: 用户名为空时尝试登录
        self.login_page.login("", "testpass123")

        # Then: 登录按钮应不可点击或仍在登录页
        assert self.login_page.is_login_page_displayed(), "空用户名应无法登录"

    @allure.title("登录页面UI验证")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.p2
    def test_login_page_ui_elements(self):
        """验证登录页面UI元素完整"""
        # Then: 验证页面关键元素
        assert self.login_page.is_login_page_displayed(), "登录页面应正常显示"
        assert self.login_page.is_login_button_enabled(), "登录按钮应可点击"
