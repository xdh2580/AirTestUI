# -*- coding: utf-8 -*-
"""
搜索功能测试用例
模块: 搜索 (SKHG-SEARCH-01 ~ SEARCH-05)

【整体状态】
所有用例均为 xfail，因为搜索模块相关截图全部缺失（TODO_IMG）。
"""
import pytest
import allure
from pages.common.shenka_search_page import ShenkaSearchPage


@allure.epic("银联云闪付申卡小程序")
@allure.feature("搜索")
@pytest.mark.common
@pytest.mark.regression
class TestShenkaSearch:
    """搜索功能测试集"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = ShenkaSearchPage()

    # ------------------------------------------------------------------
    @allure.story("SKHG-SEARCH-01")
    @allure.title("关键词搜索可以正常显示对应卡片")
    @allure.description("1. 进入搜索页面\n2. 输入关键词搜索\n3. 查看是否能找到对应卡片")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充搜索相关截图后启用", strict=False)
    def test_search_01_keyword_search(self):
        """
        SKHG-SEARCH-01: 关键词搜索
        缺少图片：shenka_search_entry.png、shenka_search_input.png、shenka_search_result_page.png
        """
        # 1. 点击搜索入口
        self.page.click_search_entry()
        self.page.wait_seconds(1)
        assert self.page.is_search_page_loaded(), "搜索页面应已加载"
        # 2. 输入关键词（示例，按实际需求修改）
        self.page.input_search_keyword("招商")
        self.page.wait_seconds(2)
        # 3. 验证跳转到卡片申请页
        assert self.page.is_card_apply_page_displayed(), "应已跳转到对应卡片申请页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-SEARCH-02")
    @allure.title("点击热门搜索可以正常跳转到对应卡片申请页")
    @allure.description("1. 进入搜索页面\n2. 点击热门搜索")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充搜索相关截图后启用", strict=False)
    def test_search_02_hot_search(self):
        """
        SKHG-SEARCH-02: 热门搜索
        缺少图片：shenka_search_entry.png、shenka_search_hot_item.png、shenka_search_result_page.png
        """
        # 1. 进入搜索页
        self.page.click_search_entry()
        self.page.wait_seconds(1)
        # 2. 点击热门搜索条目
        self.page.click_hot_search_item()
        self.page.wait_seconds(2)
        # 3. 验证跳转到卡片申请页
        assert self.page.is_card_apply_page_displayed(), "点击热门搜索应跳转到对应卡片申请页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-SEARCH-03")
    @allure.title("点击主题精选可以正常跳转到对应主题卡片推荐页")
    @allure.description("1. 进入搜索页面\n2. 点击主题精选下每一个主题")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充搜索相关截图后启用", strict=False)
    def test_search_03_theme_select(self):
        """
        SKHG-SEARCH-03: 主题精选跳转
        缺少图片：shenka_search_entry.png、shenka_search_theme_item.png、shenka_search_theme_result.png
        """
        # 1. 进入搜索页
        self.page.click_search_entry()
        self.page.wait_seconds(1)
        # 2. 点击主题精选中某主题
        self.page.click_theme_item()
        self.page.wait_seconds(2)
        # 3. 验证跳转到主题卡片推荐页
        assert self.page.is_theme_result_page_displayed(), "点击主题应跳转到对应主题推荐页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-SEARCH-04")
    @allure.title("点击取消按钮搜索页面可以正常关闭")
    @allure.description("1. 进入搜索页面\n2. 点击取消按钮")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充搜索相关截图后启用", strict=False)
    def test_search_04_cancel(self):
        """
        SKHG-SEARCH-04: 取消关闭搜索页
        缺少图片：shenka_search_entry.png、shenka_search_cancel_btn.png、shenka_search_page.png
        """
        # 1. 进入搜索页
        self.page.click_search_entry()
        self.page.wait_seconds(1)
        assert self.page.is_search_page_loaded(), "搜索页应已加载"
        # 2. 点击取消
        self.page.click_cancel()
        self.page.wait_seconds(1)
        # 3. 验证搜索页已关闭
        assert self.page.is_search_page_closed(), "点击取消后搜索页应已关闭"

    # ------------------------------------------------------------------
    @allure.story("SKHG-SEARCH-05")
    @allure.title("点击历史记录删除图标可以正常删除历史搜索记录")
    @allure.description("1. 进入搜索页面\n2. 点击历史记录右侧的删除图标")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充搜索相关截图后启用", strict=False)
    def test_search_05_delete_history(self):
        """
        SKHG-SEARCH-05: 删除历史搜索记录
        前提：需要先有历史搜索记录（可在 setup 中先搜索一次）
        缺少图片：shenka_search_entry.png、shenka_search_history_delete.png、shenka_search_history_empty.png
        """
        # 1. 进入搜索页
        self.page.click_search_entry()
        self.page.wait_seconds(1)
        # 2. 点击历史记录删除图标
        self.page.click_history_delete()
        self.page.wait_seconds(1)
        # 3. 验证历史记录已删除
        assert self.page.is_history_deleted(), "历史搜索记录应已被删除"
