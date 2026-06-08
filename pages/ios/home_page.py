"""
iOS 首页页面对象
"""
import allure

from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("IOSHomePage")


class IOSHomePage(BasePage):
    """iOS 首页"""

    def __init__(self, poco=None):
        super().__init__(poco=poco)

    @allure.step("验证首页已加载")
    def is_home_page_displayed(self) -> bool:
        """检查首页是否已显示"""
        if self._poco:
            try:
                return self.poco()("home_tab").exists()
            except Exception:
                pass
        return False

    @allure.step("获取首页标题")
    def get_page_title(self) -> str:
        """获取首页标题文本"""
        if self._poco:
            try:
                return self.poco_get_text("page_title")
            except Exception:
                pass
        return ""

    @allure.step("导航到个人中心")
    def navigate_to_profile(self):
        """进入个人中心"""
        if self._poco:
            self.poco_click("profile_tab")
