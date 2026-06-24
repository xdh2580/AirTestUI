# -*- coding: utf-8 -*-
"""
卡片详情测试用例
模块: 卡片详情 (SKHG-CARD-01 ~ CARD-13)
"""
import pytest
import allure
from pages.common.shenka_card_page import ShenkaCardPage
from pages.common.shenka_home_page import ShenkaHomePage
from pages.common.shenka_mine_page import ShenkaMinePage


@allure.epic("银联云闪付申卡小程序")
@allure.feature("卡片详情")
@pytest.mark.common
@pytest.mark.regression
class TestShenkaCard:
    """卡片详情测试集"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = ShenkaCardPage()
        self.home_page = ShenkaHomePage()
        self.mine_page = ShenkaMinePage() 

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-01")
    @allure.title("点击首页卡片可以正常跳转到卡片详情页")
    @allure.description("1. 在首页点击选择任意一张卡片\n2. 查看能否正常跳转到卡片详情页")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_card_01_enter_detail(self):
        """
        SKHG-CARD-01: 进入卡片详情页
        """
        # 1. 点击首页卡片条目
        self.page.reload_miniapp()
        self.home_page.click_card_item()
        self.page.wait_seconds(2)
        # 2. 验证已进入卡片详情页
        assert self.page.is_card_apply_page_displayed(), "应已正常跳转到卡片详情页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-02")
    @allure.title("点击银行专享权益详情可以弹出权益及申卡有礼浮窗")
    @allure.description(
        "1. 进入任一卡片详情页\n"
        "2. 点击银行专享权益旁的详情字样"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_card_02_rights_popup(self):
        """
        SKHG-CARD-02: 权益详情浮窗
        """
        # 延续上条状态，已在申卡详情页
        # 1. 点击权益详情按钮
        self.page.click_rights_detail()
        self.page.wait_seconds(1)
        # 2. 验证权益浮窗已弹出
        assert self.home_page.is_rights_detail_expanded(), "应弹出权益详情及申卡有礼浮窗"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-03")
    @allure.title("点击收藏图标可以成功收藏卡片并提示收藏成功")
    @allure.description("1. 进入任一卡片详情页\n2. 点击收藏图标")
    @allure.severity(allure.severity_level.NORMAL)
    def test_card_03_collect(self):
        """
        SKHG-CARD-03: 收藏卡片
        """
         # 1. 点击首页卡片条目
        self.page.reload_miniapp()
        self.home_page.click_card_item()
        self.page.wait_seconds(2)
        # 1. 点击收藏图标，如果已收藏，先取消
        if self.page.is_card_collected():
            self.page.click_cancel_collect()
            self.page.wait_seconds(1)
        self.page.click_collect()
        self.page.wait_seconds(0.5)
        # 2. 验证收藏成功提示出现
        assert self.page.is_collect_success_displayed(), "点击收藏后应出现收藏成功提示"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-04")
    @allure.title("收藏成功后点击去看看可以跳转到我的收藏页面")
    @allure.description(
        "1. 进入任一卡片详情页\n"
        "2. 点击收藏图标\n"
        "3. 在弹出的提示中点击去看看"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_card_04_goto_my_collect(self):
        """
        SKHG-CARD-04: 收藏后跳转我的收藏
        """
        # 1. 接续上条，先取消收藏
        self.page.wait_seconds(2)
        self.page.click_cancel_collect()
        self.page.wait_seconds(1)
        self.page.click_collect()
        # 2. 点击去看看
        self.page.click_goto_collect()
        self.page.wait_seconds(2)
        # 3. 验证已跳转到我的收藏页
        assert self.mine_page.is_my_collect_page_displayed(), "点击去看看后应已跳转到我的收藏页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-05")
    @allure.title("取消收藏卡片可以成功取消并提示已取消收藏")
    @allure.description("1. 进入任一卡片详情页\n2. 取消收藏卡片")
    @allure.severity(allure.severity_level.NORMAL)
    def test_card_05_cancel_collect(self):
        """
        SKHG-CARD-05: 取消收藏
        前提：该卡片已被收藏（可在 conftest 或 setup 中先收藏一次）
        """
         # 1. 点击首页卡片条目
        self.page.reload_miniapp()
        self.home_page.click_card_item()
        self.page.wait_seconds(2)
        if self.page.is_card_collected():
            self.page.click_cancel_collect()
            self.page.wait_seconds(0.5)
        else:
            self.page.click_collect()
            self.page.wait_seconds(5)
            self.page.click_cancel_collect()
            self.page.wait_seconds(0.5)
        # 2. 验证已取消收藏提示出现
        assert self.page.is_cancel_collect_displayed(), "取消收藏后应提示已取消收藏"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-06")
    @allure.title("点击去PK可以跳转到卡片PK页面")
    @allure.description("1. 进入任一卡片详情页\n2. 点击去PK")
    @allure.severity(allure.severity_level.NORMAL)
    def test_card_06_go_pk(self):
        """
        SKHG-CARD-06: 进入PK页面
        """
        # 1. 接续上条状态，点击去PK
        self.page.click_go_pk()
        self.page.wait_seconds(2)
        # 2. 验证已进入PK页面
        assert self.page.is_pk_page_loaded(), "点击去PK后应已跳转到卡片PK页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-07")
    @allure.title("PK页面点击已选卡片图片可以弹窗显示权益和基本信息")
    @allure.description(
        "1. 在任意卡片详情页点击去PK并进入到卡片PK页面\n"
        "2. 点击已选卡片的图片"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_card_07_pk_card_info_popup(self):
        """
        SKHG-CARD-07: PK页查看卡片权益弹窗
        """
        # 接续上条状态，点击已选卡片图片
        self.page.click_pk_selected_card()
        self.page.wait_seconds(1)
        # 验证权益弹窗已弹出
        assert self.page.is_rights_popup_displayed_in_pk_page(), "点击PK页已选卡片图片后应弹出权益信息"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-08")
    @allure.title("PK页点击添加卡片可以弹出选择卡片页")
    @allure.description(
        "1. 在任意卡片详情页点击去PK并进入到卡片PK页面\n"
        "2. 点击右侧添加卡片"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_card_08_pk_add_card(self):
        """
        SKHG-CARD-08: PK页添加卡片
        已有图片：tpl1780644658580.png（PK选择卡片页标志）
        """
        # 接续上条状态，先关闭权益详情弹窗
        self.page.close_rights_popup()
        # 点击添加卡片
        self.page.click_pk_add_card()
        self.page.wait_seconds(1)
        # 验证选择卡片页已弹出
        assert self.page.is_pk_select_page_displayed(), "点击添加卡片后应弹出选择卡片页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-09")
    @allure.title("PK选择卡片页三个Tab均可正常点击切换且卡片可选择")
    @allure.description(
        "1. 进入PK选择卡片页\n"
        "2. 选择浏览历史、我的收藏、热门推荐下方的卡片进行PK"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_card_09_pk_tab_switch(self):
        """
        SKHG-CARD-09: PK选择页Tab切换
        """
        #延续上条状态，点击Tab切换
        self.page.click_pk_tab_my_collect()
        self.page.wait_seconds(1)
        assert self.page.is_pk_tab_my_collect_displayed(), "选择卡片后应仍可操作选择页-我的收藏"
        self.page.click_pk_tab_hot_recommend()
        self.page.wait_seconds(1)
        assert self.page.is_pk_tab_hot_recommend_displayed(), "选择卡片后应仍可操作选择页-热卡推荐"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-10")
    @allure.title("PK页选两张卡点击开始PK后PK页面正确展示")
    @allure.description("1. 进入到卡片PK页面\n2. 任意选两张卡点击开始PK")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_card_10_start_pk(self):
        """
        SKHG-CARD-10: 开始PK
        已有图片：tpl1780644751070.png（开始PK按钮）、tpl1780644787909.png（PK结果页）
        """
        # 延续上条状态，已选中热卡推荐tab
        # 添加第二张卡（第一张已选）
        self.page.select_pk_card_item()
        self.page.wait_seconds(1)
        # 点击开始PK
        self.page.click_start_pk()
        self.page.wait_seconds(2)
        # 验证PK结果页已加载
        assert self.page.is_pk_result_page_loaded(), "点击开始PK后应已跳转到PK结果页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-11")
    @allure.title("PK结果页点击去申请可以跳转到对应卡片申请页")
    @allure.description(
        "1. 进入到卡片PK页面\n"
        "2. 点击已选择的卡片下方的去申请按钮"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_card_11_pk_goto_apply(self):
        """
        SKHG-CARD-11: PK结果页去申请
        已有图片：tpl1780644794697.png（去申请按钮）
        """
        # 延续上条状态，已滑动到pk页面最底部
        self.page.wait_seconds(1)
        # 点击去申请
        self.page.click_pk_goto_apply()
        self.page.wait_seconds(2)
        # 验证已跳转到三要素确认
        assert self.page.is_apply_confirm_popup_displayed()

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-12")
    @allure.title("PK页点击查看更多卡片可以跳转到全部卡片页面")
    @allure.description(
        "1. 进入到卡片PK页面\n"
        "2. 点击页面最下方的查看更多卡片"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_card_12_pk_more_cards(self):
        """
        SKHG-CARD-12: PK页查看更多卡片
        缺少图片：shenka_card_pk_more_btn.png、shenka_card_all_cards_page.png
        """
        # 延续上条状态，先返回到pk页面
        self.page.click_back_arrow()
        self.page.wait_seconds(2)
        # 滑动到最底部
        self.page.swipe_screen(direction="up")
        self.page.swipe_screen(direction="up")
        self.page.swipe_screen(direction="up")
        self.page.wait_seconds(1)
        # 点击查看更多卡片
        self.page.click_pk_more_cards()
        # 验证已跳转到全部卡片页
        assert self.page.is_all_cards_page_displayed(), "应已跳转到全部卡片页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-CARD-13")
    @allure.title("点击立即申请可以弹出三要素确认弹窗并跳转到银行申请页")
    @allure.description(
        "1. 进入任一卡片详情页\n"
        "2. 点击立即申请按钮"
    )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_card_13_apply_card(self):
        """
        SKHG-CARD-13: 立即申请
        已有图片：tpl1780644304033.png（立即申请按钮）、tpl1780646315201.png（三要素确认弹窗）
                  tpl1780646274720.png（同意按钮）、tpl1780646296583.png（银行申请页）
        """
        # 1. 延续上条状态
        self.page.click_back_arrow()
        self.page.wait_seconds(2)
        self.page.swipe_screen(direction="up")
        self.page.swipe_screen(direction="up")
        self.page.swipe_screen(direction="up")
        self.page.wait_seconds(1)
        self.page.click_pk_goto_apply()
        # 2. 验证三要素确认弹窗出现
        assert self.page.is_apply_confirm_popup_displayed(), "点击去申请后应弹出三要素确认弹窗"
        # 3. 同意确认
        self.page.confirm_apply_popup()
        self.page.wait_seconds(8)
        # 4. 验证已跳转到银行申请页
        assert self.page.is_bank_apply_page_displayed(), "同意三要素后应已跳转到银行卡片申请页"
