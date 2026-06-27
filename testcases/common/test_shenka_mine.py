# -*- coding: utf-8 -*-
"""
我的申卡测试用例
模块: 我的申卡 (SKHG-MINE-01 ~ MINE-15)
"""
from re import S
import pytest
import allure
from pages.common.shenka_mine_page import ShenkaMinePage
from pages.common.shenka_home_page import ShenkaHomePage


@allure.epic("银联云闪付申卡小程序")
@allure.feature("我的申卡")
@pytest.mark.common
@pytest.mark.regression
class TestShenkaMine:
    """我的申卡测试集"""

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """方法级别：每个测试方法执行前确保在"我的申卡"页面"""
        self.page = ShenkaMinePage()
        self.home_page = ShenkaHomePage()
        self.page.reload_miniapp()
        self.page.wait_seconds(3)
        self.home_page.click_mine_tab()
        self.page.wait_seconds(3)
        self.page.wait_mine_page_loaded()

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-01")
    @allure.title("在申卡页面点击我的申卡可以正常切换至我的申卡页面")
    @allure.description(
        "1. 在申卡页面点击我的申卡\n"
        "2. 查看是否可以正常切换至我的申卡页面"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_mine_01_enter_mine_page(self):
        """
        SKHG-MINE-01: 进入我的申卡
        """
        # 验证已进入我的申卡页面
        assert self.page.is_mine_page_loaded(), "应已正常切换到我的申卡页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-02")
    @allure.title("点击奖励明细可以正常跳转到奖励明细页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击奖励明细")
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_02_reward_detail(self):
        """
        SKHG-MINE-02: 奖励明细
        """
        # 1. 点击奖励明细
        self.page.click_reward()
        self.page.wait_seconds(2)
        # 2. 验证已跳转到奖励明细页
        assert self.page.is_reward_page_displayed(), "点击奖励明细后应已跳转到奖励明细页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-03")
    @allure.title("点击在线激活可以正常跳转到激活页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击在线激活")
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_03_activate(self):
        """
        SKHG-MINE-03: 在线激活
        """
        self.page.click_activate()
        self.page.wait_seconds(2)
        assert self.page.is_activate_page_displayed(), "点击在线激活后应已跳转到激活页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-04")
    @allure.title("点击收藏关注可以正常跳转到收藏关注页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击收藏关注")
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_04_collect_follow(self):
        """
        SKHG-MINE-04: 收藏关注
        """
        self.page.click_collect_follow()
        self.page.wait_seconds(2)
        assert self.page.is_collect_page_displayed(), "点击收藏关注后应已跳转到收藏关注页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-05")
    @allure.title("在收藏关注页左滑卡片后可以正常取消收藏")
    @allure.description(
        "1. 进入我的申卡页面\n"
        "2. 点击收藏关注进入收藏关注页面\n"
        "3. 左滑已收藏的页面，点击取消收藏"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="暂时先跳过该用例")
    def test_mine_05_cancel_collect(self):
        """
        SKHG-MINE-05: 取消收藏
        """
        self.page.click_collect_follow()
        self.page.wait_seconds(1)
        # 左滑并取消收藏
        self.page.swipe_and_cancel_collect()
        self.page.wait_seconds(1)
        assert self.page.is_collect_item_removed(), "左滑取消收藏后该卡片应已从收藏列表移除"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-06")
    @allure.title("收藏关注页可以选择收藏的卡片进行PK")
    @allure.description(
        "1. 进入我的申卡页面并收藏两张及以上卡片\n"
        "2. 点击收藏关注进入收藏关注页面\n"
        "3. 点击页面右上角卡片PK按钮"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_06_collect_pk(self):
        """
        SKHG-MINE-06: 收藏页PK
        """
        self.page.click_collect_follow()
        self.page.wait_seconds(1)
        # 点击右上角PK按钮
        self.page.click_collect_pk_btn()
        self.page.wait_seconds(1)
        self.page.click_checkbox()
        self.page.wait_seconds(1)
        self.page.click_checkbox()
        self.page.wait_seconds(1)
        self.page.click_collect_start_pk_btn()
        self.page.wait_seconds(2)
        from pages.common.shenka_card_page import ShenkaCardPage
        card_page = ShenkaCardPage()
        assert card_page.is_pk_result_page_loaded(), "在收藏页内选择卡片pk后应已跳转到PK结果页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-07")
    @allure.title("点击企微助手可以正常跳转到企微助手二维码添加页")
    @allure.description("1. 进入我的申卡页面\n2. 点击企微助手")
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_07_wecom(self):
        """
        SKHG-MINE-07: 企微助手
        """
        self.page.click_wecom()
        self.page.wait_seconds(3)
        assert self.page.is_wecom_page_displayed(), "点击企微助手后应跳转到企微助手二维码添加页"
        if self.page.is_wecom_page_displayed():
            self.page.click_cancel_button()

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-08")
    @allure.title("点击一键申卡可以正常跳转到一键申卡页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击一键申卡")
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_08_onekey_apply(self):
        """
        SKHG-MINE-08: 一键申卡入口
        """
        self.page.click_onekey_apply()
        self.page.wait_seconds(2)
        assert self.page.is_onekey_page_loaded(), "点击一键申卡后应已跳转到一键申卡页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-09")
    @allure.title("一键申卡流程可以正常生成推荐并跳转申请页")
    @allure.description(
        "1. 进入我的申卡-一键申卡页面\n"
        "2. 授权同意声明后点击立即体验\n"
        "3. 按提示选择选项，点击生成推荐"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_mine_09_onekey_flow(self):
        """
        SKHG-MINE-09: 一键申卡完整流程
        """
        # 进入一键申卡
        self.page.click_onekey_apply()
        self.page.wait_seconds(2)
        # 完成一键申卡流程
        self.page.do_onekey_apply_flow()
        # 验证推荐结果已生成
        assert self.page.is_onekey_result_generated(), "一键申卡应已生成推荐卡片"
        if self.page.is_onekey_result_generated():
            #在推荐结果页直接申卡
            self.page.click(self.page.onekey_result_page)
            self.page.wait_seconds(2)
            self.page.click_checkbox()
            self.page.click(self.page.onekey_result_page)
            self.page.wait_seconds(1)
            self.page.click_confirm_button()
            self.page.wait_seconds(5)
            assert True

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-10")
    @allure.title("点击卡片PK可以正常跳转到卡片PK页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击卡片PK")
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_10_card_pk(self):
        """
        SKHG-MINE-10: 卡片PK入口
        """
        self.page.click_card_pk()
        self.page.wait_seconds(2)
        assert self.page.is_pk_page_displayed(), "点击卡片PK后应已跳转到卡片PK页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-11")
    @allure.title("点击个人资料可以正常跳转到个人资料页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击个人资料")
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_11_profile(self):
        """
        SKHG-MINE-11: 个人资料入口
        """
        self.page.click_profile()
        self.page.wait_seconds(2)
        assert self.page.is_profile_page_displayed(), "点击个人资料后应已跳转到个人资料页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-12")
    @allure.title("点击完善信息按钮可以跳转到个人资料完善页面")
    @allure.description(
        "1. 进入我的申卡-个人资料页面\n"
        "2. 点击页面上方的完善信息按钮"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_12_edit_profile(self):
        """
        SKHG-MINE-12: 进入资料完善页
        """
        self.page.click_profile()
        self.page.wait_seconds(2)
        # 点击完善信息
        self.page.click_edit_profile()
        self.page.wait_seconds(2)
        assert self.page.is_profile_edit_page_displayed(), "点击完善信息后应已跳转到个人资料完善填写页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-13")
    @allure.title("在个人资料完善页完善信息并保存可以正常修改")
    @allure.description(
        "1. 进入我的申卡-个人资料页面\n"
        "2. 进入个人资料完善填写页面\n"
        "3. 在页面内完善各类信息，点击保存"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="暂时先跳过该用例")
    def test_mine_13_save_profile(self):
        """
        SKHG-MINE-13: 完善并保存个人资料
        """

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-14")
    @allure.title("在个人资料完善页点击一键申卡可以正常跳转到一键申卡页面")
    @allure.description(
        "1. 进入我的申卡-个人资料页面\n"
        "2. 进入个人资料完善填写页面\n"
        "3. 点击页面下方的一键申卡按钮"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="暂时先跳过该用例")
    def test_mine_14_profile_onekey_apply(self):
        """
        SKHG-MINE-14: 完善页一键申卡按钮
        """

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-15")
    @allure.title("点击快速申卡区域的卡片可以直接跳转到对应卡片申卡详情页")
    @allure.description(
        "1. 进入我的申卡-个人资料页面\n"
        "2. 点击页面下方的快速申卡区域内的任意卡片"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_15_quick_apply_card(self):
        """
        SKHG-MINE-15: 快速申卡
        """
        self.page.click_profile()
        self.page.wait_seconds(2)
        # 点击快速申卡区域某张卡片
        self.page.click_quick_card()
        self.page.wait_seconds(2)
        # 验证已跳转到卡片申卡详情页（复用卡片详情页的标志）
        from pages.common.shenka_card_page import ShenkaCardPage
        card_page = ShenkaCardPage()
        assert card_page.is_card_apply_page_displayed(), "点击快速申卡区域卡片后应直接跳转到对应卡片申卡详情页"
