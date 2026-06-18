"""
搜索页面对象 - 纯图像识别
对应模块: 搜索 (SKHG-SEARCH-01 ~ SEARCH-05)
"""
import allure
from airtest.core.api import Template
from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("ShenkaSearchPage")

RES = "common/shenka"


class ShenkaSearchPage(BasePage):
    """搜索页面对象（纯图像识别）"""

    def __init__(self):
        super().__init__(poco=None)

        # 搜索页面加载标志
        self.search_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_search_page.png"), threshold=0.8)
        self.search_page_indicator2 = Template(
            self.resource_path(f"{RES}/shenka_search_page2.png"), threshold=0.8)

        # 搜索框（可输入状态）
        self.search_input = Template(
            self.resource_path(f"{RES}/shenka_search_input.png"), threshold=0.8)

        # 热门搜索条目
        self.hot_search_item = Template(
            self.resource_path(f"{RES}/shenka_search_hot_item.png"), threshold=0.8)

        # 搜索结果（招商银行）
        self.search_result = Template(
            self.resource_path(f"{RES}/shenka_search_result_page.png"))

        # 主题精选中某主题条目(餐饮时尚)
        self.theme_item = Template(
            self.resource_path(f"{RES}/shenka_search_theme_item.png"), threshold=0.8)

        # 取消按钮
        self.cancel_btn = Template(
            self.resource_path(f"{RES}/shenka_search_cancel_btn.png"), threshold=0.8)

        # 历史记录删除图标
        self.history_delete_icon = Template(
            self.resource_path(f"{RES}/shenka_search_history_delete.png"), threshold=0.8)

        # 存在历史记录标志
        self.history_indicator = Template(
            self.resource_path(f"{RES}/shenka_search_history_indicator.png"), threshold=0.7)

    # ---- 页面验证 ----

    @allure.step("判断搜索页面是否已加载")
    def is_search_page_loaded(self) -> bool:
        """
        热门搜索和主题精选都要显示
        """
        return self.is_exists(self.search_page_indicator) and self.is_exists(self.search_page_indicator2)

    @allure.step("判断是否已显示搜索结果")
    def is_search_result_displayed(self) -> bool: 
        """
        判断是否已显示搜索结果
        """
        return self.is_exists(self.search_result)

    @allure.step("判断是否有历史记录")
    def is_history_exists(self) -> bool:
        """
        判断是否存在历史记录标志，不存在则表示无历史记录
        """
        return self.is_exists(self.history_indicator)

    # ---- 页面操作 ----
    @allure.step("点击热门搜索条目")
    def click_hot_search_item(self):
        """
        点击热门搜索列表中的条目
        """
        log.info("点击热门搜索条目")
        self.click(self.hot_search_item)

    @allure.step("在搜索框中输入关键词: {keyword}")
    def input_search_keyword(self, keyword: str):
        """
        在搜索框输入关键词
        """
        log.info(f"输入搜索关键词: {keyword}")
        self.input_text(keyword, self.search_input)

    @allure.step("点击主题精选中的某主题")
    def click_theme_item(self):
        """
        点击主题精选列表中的某主题条目
        """
        log.info("点击主题精选条目")
        self.click(self.theme_item)

    @allure.step("点击取消按钮")
    def click_cancel(self):
        """
        点击搜索页取消按钮，关闭搜索页
        """
        log.info("点击取消按钮")
        self.click(self.cancel_btn)

    @allure.step("点击历史记录删除图标")
    def click_history_delete(self):
        """
        点击历史记录右侧删除图标，删除历史搜索记录
        """
        log.info("点击历史记录删除图标")
        self.click(self.history_delete_icon)
