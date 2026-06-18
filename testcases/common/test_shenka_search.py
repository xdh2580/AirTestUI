# -*- coding: utf-8 -*-
"""
搜索功能测试用例
模块: 搜索 (SKHG-SEARCH-01 ~ SEARCH-05)
"""
import pytest
import allure
from pages.common.shenka_home_page import ShenkaHomePage
from pages.common.shenka_search_page import ShenkaSearchPage
from pages.common.shenka_card_page import ShenkaCardPage
from pages.common.shenka_filter_page import ShenkaFilterPage


@allure.epic("银联云闪付申卡小程序")
@allure.feature("搜索")
@pytest.mark.common
@pytest.mark.regression
class TestShenkaSearch:
    """搜索功能测试集"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = ShenkaSearchPage()
        self.home_page = ShenkaHomePage()
        self.card_page = ShenkaCardPage()
        self.filter_page = ShenkaFilterPage()

    # ------------------------------------------------------------------
    @allure.story("SKHG-SEARCH-01")
    @allure.title("关键词搜索可以正常显示对应卡片")
    @allure.description("1. 进入搜索页面\n2. 输入关键词搜索\n3. 查看是否能找到对应卡片")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_01_keyword_search(self):
        """
        SKHG-SEARCH-01: 关键词搜索
        """
        # 重新加载小程序
        # 1. 点击搜索入口
        self.page.reload_miniapp()
        self.home_page.click_search_entry()
        self.page.wait_seconds(1)
        assert self.page.is_search_page_loaded(), "搜索页面应已加载"
        # 2. 输入关键词（示例，按实际需求修改）
        self.page.input_search_keyword("招商")
        self.page.wait_seconds(1)
        # 3. 验证搜索结果是否显示
        assert self.page.is_search_result_displayed(), "应已显示搜索结果"

    # ------------------------------------------------------------------
    @allure.story("SKHG-SEARCH-02")
    @allure.title("点击热门搜索可以正常跳转到对应卡片申请页")
    @allure.description("1. 进入搜索页面\n2. 点击热门搜索")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_02_hot_search(self):
        """
        SKHG-SEARCH-02: 热门搜索
        """
        # 1. 进入搜索页
        self.page.reload_miniapp()
        self.page.wait_seconds(3)
        self.home_page.click_search_entry()
        self.page.wait_seconds(1)
        # 2. 点击热门搜索条目
        self.page.click_hot_search_item()
        self.page.wait_seconds(3)
        # 3. 验证跳转到卡片申请页
        assert self.card_page.is_card_apply_page_displayed(), "点击热门搜索应跳转到对应卡片申请页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-SEARCH-03")
    @allure.title("点击主题精选可以正常跳转到对应主题卡片推荐页")
    @allure.description("1. 进入搜索页面\n2. 点击主题精选下每一个主题")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_03_theme_select(self):
        """
        SKHG-SEARCH-03: 主题精选跳转
        """
        # 1. 进入搜索页
        self.page.reload_miniapp()
        self.page.wait_seconds(3)
        self.home_page.click_search_entry()
        self.page.wait_seconds(1)
        # 2. 点击主题精选中某主题
        self.page.click_theme_item()
        self.page.wait_seconds(2)
        # 3. 验证跳转到主题卡片推荐页
        assert self.filter_page.is_filter_all_card_page_displayed(), "点击主题应跳转到对应主题推荐页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-SEARCH-04")
    @allure.title("点击取消按钮搜索页面可以正常关闭")
    @allure.description("1. 进入搜索页面\n2. 点击取消按钮")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_04_cancel(self):
        """
        SKHG-SEARCH-04: 取消关闭搜索页
        """
        # 1. 进入搜索页
        self.page.click_back_arrow()
        self.page.wait_seconds(1)
        assert self.page.is_search_page_loaded(), "搜索页应已加载"
        # 2. 点击取消
        self.page.click_cancel()
        self.page.wait_seconds(1)
        # 3. 验证搜索页已关闭
        assert self.home_page.is_home_loaded(), "点击取消后搜索页应回到申卡首页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-SEARCH-05")
    @allure.title("点击历史记录删除图标可以正常删除历史搜索记录")
    @allure.description("1. 进入搜索页面\n2. 点击历史记录右侧的删除图标")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_05_delete_history(self):
        """
        SKHG-SEARCH-05: 删除历史搜索记录
        前提：需要先有历史搜索记录（已在前面test搜索过一次）
        """
        # 1. 进入搜索页
        self.home_page.click_search_entry()
        self.page.wait_seconds(1)
        # 2. 点击历史记录删除图标
        self.page.click_history_delete()
        self.page.wait_seconds(1)
        # 3. 验证历史记录已删除
        assert not self.page.is_history_exists(), "历史搜索记录应已被删除"
