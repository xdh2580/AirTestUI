"""
选择城市页面对象 - 纯图像识别
对应模块: 选择城市 (SKHG-CITY-01 ~ CITY-04)
"""
import allure
from airtest.core.api import Template

from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("ShenkaCityPage")

RES = "common/shenka"


class ShenkaCityPage(BasePage):
    """选择城市页面对象（纯图像识别）"""

    def __init__(self):
        super().__init__(poco=None)

        # 城市选择页面加载标志
        self.city_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_city_page.png"), threshold=0.8)

        # 城市列表中某城市条目（此图也用于验证首页显示城市）
        self.city_item = Template(
            self.resource_path(f"{RES}/shenka_city_item.png"), threshold=0.6)

        # 城市搜索输入框
        self.city_search_input = Template(
            self.resource_path(f"{RES}/shenka_city_search_input.png"), threshold=0.8)

        # 搜索结果（此图也用于验证首页显示城市）
        self.city_search_result = Template(
            self.resource_path(f"{RES}/shenka_city_search_result.png"), threshold=0.6)

        # 定位成功后城市标志
        self.city_located_indicator = Template(
            self.resource_path(f"{RES}/shenka_city_located.png"), threshold=0.7)

    # ---- 页面验证 ----

    @allure.step("判断城市选择页面是否已加载")
    def is_city_page_loaded(self) -> bool:
        """
        TODO_IMG: 需补充城市选择页面加载标志截图 shenka_city_page.png
        """
        return self.is_exists(self.city_page_indicator)

    @allure.step("判断城市是否已切换（手动选择）")
    def is_city_changed(self) -> bool:
        """
        判断城市切换后首页是否已刷新/变化
        TODO_IMG: 需补充城市切换后页面变化标志截图 shenka_city_changed_indicator.png
        """
        return self.is_exists(self.city_item)

    @allure.step("判断城市是否已切换（搜索后选择）")
    def is_city_changed_by_search(self) -> bool:
        """
        搜索后选择某城市后验证
        """
        return self.is_exists(self.city_search_result)

    @allure.step("判断搜索城市结果是否出现")
    def is_search_result_displayed(self) -> bool:
        """
        TODO_IMG: 需补充搜索城市结果条目截图 shenka_city_search_result.png
        """
        return self.is_exists(self.city_search_result)

    @allure.step("判断当前城市是否已定位")
    def is_city_located(self) -> bool:
        """
        判断当前城市是否已定位
        """
        return self.is_exists(self.city_located_indicator)

    # ---- 页面操作 ----

    @allure.step("点击城市列表中的某城市")
    def click_city_item(self):
        """
        点击城市列表中的某城市进行切换
        """
        log.info("点击城市条目")
        self.click(self.city_item)

    @allure.step("在城市搜索框中输入城市名: {city_name}")
    def search_city(self, city_name: str):
        """
        在城市搜索框输入城市名进行搜索
        """
        log.info(f"搜索城市: {city_name}")
        self.input_text(city_name, self.city_search_input)

    @allure.step("点击搜索结果中的城市")
    def click_search_result(self):
        """
        点击搜索结果中的城市
        """
        log.info("点击搜索结果城市")
        self.click(self.city_search_result)

