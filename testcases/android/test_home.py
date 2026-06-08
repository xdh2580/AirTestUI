"""
Android 首页功能回归测试用例
"""
import allure
import pytest

from pages.android.home_page import AndroidHomePage
from utils.logger import get_logger

log = get_logger("TestAndroidHome")


@allure.feature("首页模块")
@allure.story("Android 首页")
@pytest.mark.android
@pytest.mark.regression
class TestAndroidHome:
    """Android 首页功能回归测试"""

    @pytest.fixture(autouse=True)
    def setup(self, poco):
        self.home_page = AndroidHomePage(poco=poco)

    @allure.title("首页加载验证")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    @pytest.mark.smoke
    def test_home_page_loaded(self):
        """验证首页正常加载"""
        assert self.home_page.is_home_page_displayed(), "首页应正常显示"

    @allure.title("首页标题验证")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_home_page_title(self):
        """验证首页标题正确"""
        title = self.home_page.get_page_title()
        # 根据实际APP调整断言
        assert title is not None, "首页标题不应为空"

    @allure.title("导航到个人中心")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_navigate_to_profile(self):
        """验证可以导航到个人中心"""
        self.home_page.navigate_to_profile()
        # 根据实际APP添加断言
