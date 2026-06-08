"""
Android 首页页面对象
示例: 登录后的主页
"""
import allure
from airtest.core.api import Template

from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("AndroidHomePage")


class AndroidHomePage(BasePage):
    """Android 首页"""

    def __init__(self, poco=None):
        super().__init__(poco=poco)
        self._img_home_tab = Template(self.resource_path("android/tab_home.png"))

    @allure.step("验证首页已加载")
    def is_home_page_displayed(self) -> bool:
        """检查首页是否已显示"""
        if self._poco:
            try:
                return self.poco()("home_tab").exists()
            except Exception:
                pass
        return self.is_exists(self._img_home_tab)

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
        """点击底部导航进入个人中心"""
        if self._poco:
            self.poco_click("profile_tab")
        else:
            self.click(Template(self.resource_path("android/tab_profile.png")))

    @allure.step("搜索功能")
    def search(self, keyword: str):
        """执行搜索"""
        if self._poco:
            self.poco_click("search_icon")
            self.poco_set_text("search_input", keyword)
        else:
            self.click(Template(self.resource_path("android/icon_search.png")))
            self.input_text(keyword)
