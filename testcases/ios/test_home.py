"""
iOS 首页功能回归测试用例
"""
import allure
import pytest

from pages.ios.home_page import IOSHomePage
from utils.logger import get_logger

log = get_logger("TestIOSHome")


@allure.feature("首页模块")
@allure.story("iOS 首页")
@pytest.mark.ios
@pytest.mark.regression
class TestIOSHome:
    """iOS 首页功能回归测试"""

    @pytest.fixture(autouse=True)
    def setup(self, poco):
        self.home_page = IOSHomePage(poco=poco)

    @allure.title("iOS 首页加载验证")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    @pytest.mark.smoke
    def test_home_page_loaded(self):
        """验证 iOS 首页正常加载"""
        assert self.home_page.is_home_page_displayed(), "首页应正常显示"

    @allure.title("iOS 导航到个人中心")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_navigate_to_profile(self):
        """验证 iOS 导航到个人中心"""
        self.home_page.navigate_to_profile()
