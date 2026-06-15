# -*- coding: utf-8 -*-
"""
选择城市测试用例
模块: 选择城市 (SKHG-CITY-01 ~ CITY-04)

【整体状态】
所有用例均为 xfail，因为城市选择模块相关截图全部缺失（TODO_IMG）。
补充截图、解注释 page 文件中对应元素定义、去掉 @pytest.mark.xfail 后即可运行。
"""
import pytest
import allure
from pages.common.shenka_city_page import ShenkaCityPage


@allure.epic("银联云闪付申卡小程序")
@allure.feature("选择城市")
@pytest.mark.common
@pytest.mark.regression
class TestShenkaCity:
    """选择城市测试集"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = ShenkaCityPage()

    # ------------------------------------------------------------------
    @allure.story("SKHG-CITY-01")
    @allure.title("点击城市入口可正常进入城市选择页面")
    @allure.description("1. 在申卡首页点击城市入口\n2. 查看城市选择页面是否正常跳转")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充城市相关截图后启用", strict=False)
    def test_city_01_enter_city_page(self):
        """
        SKHG-CITY-01: 进入城市选择页
        缺少图片：shenka_city_entry.png、shenka_city_page.png
        """
        # 1. 点击城市入口
        self.page.click_city_entry()
        self.page.wait_seconds(1)
        # 2. 验证城市选择页已加载
        assert self.page.is_city_page_loaded(), "城市选择页面应已正常加载"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CITY-02")
    @allure.title("点击城市列表中的城市可正常切换城市并刷新卡片")
    @allure.description("1. 进入城市选择页面\n2. 点击城市列表中的某城市\n3. 查看首页卡片是否刷新")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充城市相关截图后启用", strict=False)
    def test_city_02_select_city(self):
        """
        SKHG-CITY-02: 切换城市
        缺少图片：shenka_city_entry.png、shenka_city_item.png、shenka_city_changed_indicator.png
        """
        # 1. 进入城市选择页
        self.page.click_city_entry()
        self.page.wait_seconds(1)
        # 2. 点击某城市
        self.page.click_city_item()
        self.page.wait_seconds(2)
        # 3. 验证城市已切换（首页刷新）
        assert self.page.is_city_changed(), "切换城市后首页卡片应已刷新"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CITY-03")
    @allure.title("搜索城市可以正常找到并选择对应城市")
    @allure.description("1. 进入城市选择页面\n2. 在搜索框输入城市名\n3. 点击搜索结果中的城市")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充城市搜索相关截图后启用", strict=False)
    def test_city_03_search_city(self):
        """
        SKHG-CITY-03: 搜索城市
        缺少图片：shenka_city_entry.png、shenka_city_search_input.png、shenka_city_search_result.png
        """
        # 1. 进入城市选择页
        self.page.click_city_entry()
        self.page.wait_seconds(1)
        # 2. 搜索城市（示例城市名，实际按需修改）
        self.page.search_city("上海")
        self.page.wait_seconds(1)
        # 3. 验证搜索结果出现
        assert self.page.is_search_result_displayed(), "应显示搜索城市结果"
        # 4. 点击搜索结果
        self.page.click_search_result()
        self.page.wait_seconds(2)
        # 5. 验证城市已切换
        assert self.page.is_city_changed(), "选择搜索结果城市后应已切换城市"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CITY-04")
    @allure.title("定位当前城市功能可正常使用")
    @allure.description("1. 进入城市选择页面\n2. 点击定位当前城市\n3. 查看城市是否已自动切换")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充城市相关截图后启用", strict=False)
    def test_city_04_locate_city(self):
        """
        SKHG-CITY-04: 定位城市
        缺少图片：shenka_city_entry.png、shenka_city_locate_btn.png、shenka_city_located.png
        """
        # 1. 进入城市选择页
        self.page.click_city_entry()
        self.page.wait_seconds(1)
        # 2. 点击定位当前城市
        self.page.click_locate_city()
        self.page.wait_seconds(3)
        # 3. 验证城市已自动切换
        assert self.page.is_city_changed(), "定位城市后应已自动切换到当前城市"
