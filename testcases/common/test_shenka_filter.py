# -*- coding: utf-8 -*-
"""
筛选/查询功能测试用例
模块: 查询（筛选）(SKHG-FILTER-01 ~ FILTER-08)
"""
import pytest
import allure
from pages.common.shenka_filter_page import ShenkaFilterPage


@allure.epic("银联云闪付申卡小程序")
@allure.feature("查询筛选")
@pytest.mark.common
@pytest.mark.regression
class TestShenkaFilter:
    """筛选功能测试集"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = ShenkaFilterPage()

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-01")
    @allure.title("直接切换查询条件可以正常筛选卡片")
    @allure.description("1. 进入申卡小程序首页\n2. 直接切换查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充筛选相关截图后启用", strict=False)
    def test_filter_01_direct_switch(self):
        """
        SKHG-FILTER-01: 直接切换筛选条件
        已有图片：tpl1780644406826.png（滑动区域），可直接滑动切换筛选条件
        缺少图片：shenka_filter_result.png（验证筛选结果）
        """
        # 前提：已在申卡首页
        # 1. 切换筛选条件（滑动筛选栏）
        self.page.switch_filter_condition()
        self.page.wait_seconds(2)
        # 2. 验证筛选已生效（卡片列表已刷新）
        assert self.page.is_filter_result_refreshed(), "切换筛选条件后卡片应已刷新"

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-02")
    @allure.title("切换全部银行查询条件可以正常筛选银行")
    @allure.description("1. 进入申卡小程序首页\n2. 切换全部银行的查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充筛选相关截图后启用", strict=False)
    def test_filter_02_bank_filter(self):
        """
        SKHG-FILTER-02: 银行筛选
        缺少图片：shenka_filter_bank_btn.png、shenka_filter_bank_item.png、shenka_filter_result.png
        """
        # 1. 选择银行筛选条件
        self.page.select_bank_filter()
        self.page.wait_seconds(2)
        # 2. 验证筛选已生效
        assert self.page.is_filter_result_refreshed(), "选择银行后卡片应已刷新"

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-03")
    @allure.title("切换卡等级查询条件可以正常筛选卡等级")
    @allure.description("1. 进入申卡小程序首页\n2. 切换卡等级的查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充筛选相关截图后启用", strict=False)
    def test_filter_03_level_filter(self):
        """
        SKHG-FILTER-03: 卡等级筛选
        缺少图片：shenka_filter_level_btn.png、shenka_filter_level_item.png、shenka_filter_result.png
        """
        self.page.select_level_filter()
        self.page.wait_seconds(2)
        assert self.page.is_filter_result_refreshed(), "选择卡等级后卡片应已刷新"

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-04")
    @allure.title("切换卡主题查询条件可以正常筛选卡主题")
    @allure.description("1. 进入申卡小程序首页\n2. 切换卡主题的查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充筛选相关截图后启用", strict=False)
    def test_filter_04_theme_filter(self):
        """
        SKHG-FILTER-04: 卡主题筛选
        缺少图片：shenka_filter_theme_btn.png、shenka_filter_theme_item.png、shenka_filter_result.png
        """
        self.page.select_theme_filter()
        self.page.wait_seconds(2)
        assert self.page.is_filter_result_refreshed(), "选择卡主题后卡片应已刷新"

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-05")
    @allure.title("切换年费查询条件可以正常筛选年费")
    @allure.description("1. 进入申卡小程序首页\n2. 切换年费的查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充筛选相关截图后启用", strict=False)
    def test_filter_05_fee_filter(self):
        """
        SKHG-FILTER-05: 年费筛选
        缺少图片：shenka_filter_fee_btn.png、shenka_filter_fee_item.png、shenka_filter_result.png
        """
        self.page.select_fee_filter()
        self.page.wait_seconds(2)
        assert self.page.is_filter_result_refreshed(), "选择年费条件后卡片应已刷新"

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-06")
    @allure.title("点击更多查询条件可以正常筛选各类服务及标签")
    @allure.description("1. 在申卡页面\n2. 点击更多的查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充筛选相关截图后启用", strict=False)
    def test_filter_06_more_filter(self):
        """
        SKHG-FILTER-06: 更多筛选
        缺少图片：shenka_filter_more_btn.png、shenka_filter_more_panel.png、
                  shenka_filter_tag_item.png、shenka_filter_result.png
        """
        # 1. 点击更多筛选
        self.page.click_more_filter()
        self.page.wait_seconds(1)
        # 2. 验证更多筛选浮窗已弹出
        assert self.page.is_more_filter_panel_displayed(), "更多筛选浮窗应已弹出"
        # 3. 选择某标签
        self.page.select_tag_item()
        self.page.wait_seconds(2)
        # 4. 验证筛选已生效
        assert self.page.is_filter_result_refreshed(), "选择服务标签后卡片应已刷新"

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-07")
    @allure.title("在筛选浮窗中选择选项后点击重置可以清除选择")
    @allure.description(
        "1. 在筛选卡主题、年费和更多浮窗中选择某一个或者多个选择项\n"
        "2. 点击重置按钮"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充筛选相关截图后启用", strict=False)
    def test_filter_07_reset(self):
        """
        SKHG-FILTER-07: 重置筛选条件
        缺少图片：shenka_filter_theme_btn.png、shenka_filter_reset_btn.png
        """
        # 1. 先选择某筛选条件
        self.page.select_theme_filter()
        self.page.wait_seconds(1)
        # 2. 点击重置
        self.page.click_reset()
        self.page.wait_seconds(1)
        # 3. 验证筛选选项已重置
        assert self.page.is_filter_reset(), "点击重置后筛选选项应已被清除"

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-08")
    @allure.title("点击特色服务Tag可以在原有筛选条件下二次筛选")
    @allure.description(
        "1. 进入申卡小程序首页\n"
        "2. 点击筛选组件下方的各种特色服务的tag（全部卡片，精选，免年费等）"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充筛选相关截图后启用", strict=False)
    def test_filter_08_special_tag(self):
        """
        SKHG-FILTER-08: 特色服务Tag二次筛选
        缺少图片：shenka_filter_special_tag.png、shenka_filter_result.png
        """
        # 1. 点击特色服务Tag
        self.page.click_special_tag()
        self.page.wait_seconds(2)
        # 2. 验证筛选已生效
        assert self.page.is_filter_result_refreshed(), "点击特色服务Tag后卡片应已二次筛选刷新"
