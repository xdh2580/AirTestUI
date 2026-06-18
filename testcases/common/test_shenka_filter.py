# -*- coding: utf-8 -*-
"""
筛选/查询功能测试用例
模块: 查询（筛选）(SKHG-FILTER-01 ~ FILTER-08)
"""
import pytest
import allure
from pages.common.shenka_filter_page import ShenkaFilterPage
from pages.common.shenka_home_page import ShenkaHomePage


@allure.epic("银联云闪付申卡小程序")
@allure.feature("查询筛选")
@pytest.mark.common
@pytest.mark.regression
class TestShenkaFilter:
    """筛选功能测试集"""

    # ==================== Fixtures ====================

    @pytest.fixture(autouse=True, scope="class")
    def class_setup(self, request):
        request.cls.page = ShenkaFilterPage()
        request.cls.home_page = ShenkaHomePage()

    # ==================== 辅助方法 ====================

    def _lower_half_region(self):
        """返回屏幕下方 50% 区域的坐标 (x, y, w, h)"""
        w, h = self.page._get_screen_size()
        return 0, h // 2, w, h // 2

    def _navigate_to_filter_area(self):
        """重新进入小程序并滑动到筛选区域"""
        self.page.reload_miniapp()
        self.page.wait_seconds(3)
        self.home_page.swipe_to_filter_area()
        self.page.wait_seconds(2)

    def _verify_filter_changed(self, action, threshold=0.10):
        """截取下方 50% → 执行 action → 截取 → 断言变化"""
        x, y, w, h = self._lower_half_region()
        self.page.assert_area_changed(x, y, w, h, action, threshold,
            msg="筛选后卡片区域应刷新")

    # ==================== 用例 ====================

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-01")
    @allure.title("直接切换查询条件可以正常筛选卡片")
    @allure.description("1. 进入申卡小程序首页\n2. 直接切换查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_filter_01_direct_switch(self):
        """
        SKHG-FILTER-01: 直接切换筛选条件
        通过截取屏幕下方 50% 区域，对比筛选前后变化来验证筛选生效
        """
        self._navigate_to_filter_area()
        self._verify_filter_changed(
            action=lambda: self.page.click_filter_condition_jx(),
        )

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-02")
    @allure.title("切换全部银行查询条件可以正常筛选银行")
    @allure.description("1. 进入申卡小程序首页\n2. 切换全部银行的查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_02_bank_filter(self):
        """SKHG-FILTER-02: 银行筛选"""
        self._navigate_to_filter_area()
        self._verify_filter_changed(
            action=lambda: (
                self.page.select_bank_filter(),
                self.page.wait_seconds(1),
                self.page.select_bank_item(),
            ),
        )

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-03")
    @allure.title("切换卡等级查询条件可以正常筛选卡等级")
    @allure.description("1. 进入申卡小程序首页\n2. 切换卡等级的查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_03_level_filter(self):
        """SKHG-FILTER-03: 卡等级筛选"""
        self._navigate_to_filter_area()
        self._verify_filter_changed(
            action=lambda: (
                self.page.select_card_level_filter(),
                self.page.wait_seconds(1),
                self.page.select_card_level_item(),
            ),
        )

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-04")
    @allure.title("切换卡主题查询条件可以正常筛选卡主题")
    @allure.description("1. 进入申卡小程序首页\n2. 切换卡主题的查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_04_theme_filter(self):
        """SKHG-FILTER-04: 卡主题筛选"""
        self._navigate_to_filter_area()
        self._verify_filter_changed(
            action=lambda: (
                self.page.select_card_theme_filter(),
                self.page.wait_seconds(1),
                self.page.select_card_theme_item(),
                self.page.click_filter_confirm_btn(),
            ),
        )

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-05")
    @allure.title("切换年费查询条件可以正常筛选年费")
    @allure.description("1. 进入申卡小程序首页\n2. 切换年费的查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_05_fee_filter(self):
        """SKHG-FILTER-05: 年费筛选"""
        self._navigate_to_filter_area()
        self._verify_filter_changed(
            action=lambda: (
                self.page.select_year_fee_filter(),
                self.page.wait_seconds(1),
                self.page.select_year_fee_item(),
                self.page.click_filter_confirm_btn(),
            ),
        )

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-06")
    @allure.title("点击更多查询条件可以正常筛选各类服务及标签")
    @allure.description("1. 在申卡页面\n2. 点击更多的查询条件查看是否可以正常筛选")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_06_more_filter(self):
        """SKHG-FILTER-06: 更多筛选"""
        self._navigate_to_filter_area()
        self._verify_filter_changed(
            action=lambda: (
                self.page.click_more_filter(),
                self.page.wait_seconds(1),
                self.page.select_more_filter_item(),
                self.page.click_filter_confirm_btn(),
            ),
        )

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-07")
    @allure.title("在筛选浮窗中选择选项后点击重置可以清除选择")
    @allure.description(
        "1. 在筛选卡主题、年费和更多浮窗中选择某一个或者多个选择项\n"
        "2. 点击重置按钮"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_07_reset(self):
        """SKHG-FILTER-07: 重置筛选条件（接续上条用例，已在筛选区域）"""
        self._verify_filter_changed(
            action=lambda: (
                self.page.click_more_filter(),
                self.page.wait_seconds(1),
                self.page.click_reset_btn(),
                self.page.click_filter_confirm_btn(),
            ),
        )

    # ------------------------------------------------------------------
    @allure.story("SKHG-FILTER-08")
    @allure.title("点击特色服务Tag可以在原有筛选条件下二次筛选")
    @allure.description(
        "1. 进入申卡小程序首页\n"
        "2. 点击筛选组件下方的各种特色服务的tag（全部卡片，精选，免年费等）"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_08_special_tag(self):
        """SKHG-FILTER-08: 特色服务Tag二次筛选（接续上条用例，已在筛选区域）"""
        self._verify_filter_changed(
            action=lambda: (
                self.page.select_card_level_filter(),
                self.page.wait_seconds(1),
                self.page.select_card_level_item(),
                self.page.click_more_filter(),
                self.page.wait_seconds(1),
                self.page.select_more_filter_item(),
                self.page.click_filter_confirm_btn(),
            ),
        )
