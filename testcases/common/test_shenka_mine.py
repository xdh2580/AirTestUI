# -*- coding: utf-8 -*-
"""
我的申卡测试用例
模块: 我的申卡 (SKHG-MINE-01 ~ MINE-15)
"""
import pytest
import allure
from pages.common.shenka_mine_page import ShenkaMinePage


@allure.epic("银联云闪付申卡小程序")
@allure.feature("我的申卡")
@pytest.mark.common
@pytest.mark.regression
class TestShenkaMine:
    """我的申卡测试集"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = ShenkaMinePage()

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
        已有图片：tpl1780644841764.png（我的申卡Tab等待标志）
                  tpl1780644925504.png（我的申卡Tab按钮）
                  tpl1780644956627.png（我的申卡页面标志）
        """
        # 1. 点击我的申卡Tab
        self.page.click_mine_tab()
        self.page.wait_seconds(2)
        # 2. 验证已进入我的申卡页面
        assert self.page.is_mine_page_loaded(), "应已正常切换到我的申卡页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-02")
    @allure.title("点击奖励明细可以正常跳转到奖励明细页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击奖励明细")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充奖励明细页面标志截图后启用", strict=False)
    def test_mine_02_reward_detail(self):
        """
        SKHG-MINE-02: 奖励明细
        已有图片：tpl1780644964606.png（奖励明细入口）
        缺少图片：shenka_mine_reward_page.png（奖励明细页标志）
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
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
    @pytest.mark.xfail(reason="TODO_IMG: 需补充激活页面标志截图后启用", strict=False)
    def test_mine_03_activate(self):
        """
        SKHG-MINE-03: 在线激活
        已有图片：tpl1780644977195.png（在线激活入口）
        缺少图片：shenka_mine_activate_page.png（激活页标志）
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
        self.page.click_activate()
        self.page.wait_seconds(2)
        assert self.page.is_activate_page_displayed(), "点击在线激活后应已跳转到激活页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-04")
    @allure.title("点击收藏关注可以正常跳转到收藏关注页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击收藏关注")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充收藏关注页面标志截图后启用", strict=False)
    def test_mine_04_collect_follow(self):
        """
        SKHG-MINE-04: 收藏关注
        已有图片：tpl1780644983769.png（收藏关注入口）
        缺少图片：shenka_mine_collect_page.png（收藏关注页标志）
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
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
    @pytest.mark.xfail(reason="TODO_IMG: 需补充收藏相关截图后启用", strict=False)
    def test_mine_05_cancel_collect(self):
        """
        SKHG-MINE-05: 取消收藏
        缺少图片：shenka_mine_collect_page.png、shenka_mine_collect_item.png、
                  shenka_mine_cancel_collect_btn.png、shenka_mine_collect_empty.png
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
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
    @pytest.mark.xfail(reason="TODO_IMG: 需补充收藏页PK按钮截图后启用", strict=False)
    def test_mine_06_collect_pk(self):
        """
        SKHG-MINE-06: 收藏页PK
        缺少图片：shenka_mine_collect_page.png、shenka_mine_collect_pk_btn.png
        前提：需要先收藏至少两张卡片
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
        self.page.click_collect_follow()
        self.page.wait_seconds(1)
        # 点击右上角PK按钮
        self.page.click_collect_pk_btn()
        self.page.wait_seconds(2)
        # 在收藏页内选择卡片后可跳转PK页
        assert self.page.is_pk_page_displayed(), "在收藏页点击PK并选择卡片后应跳转到PK页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-07")
    @allure.title("点击企微助手可以正常跳转到企微助手二维码添加页")
    @allure.description("1. 进入我的申卡页面\n2. 点击企微助手")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充企微助手页面标志截图后启用", strict=False)
    def test_mine_07_wecom(self):
        """
        SKHG-MINE-07: 企微助手
        已有图片：tpl1780645007235.png（企微助手入口）
        缺少图片：shenka_mine_wecom_page.png（企微助手页面标志）
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
        self.page.click_wecom()
        self.page.wait_seconds(3)
        assert self.page.is_wecom_page_displayed(), "点击企微助手后应跳转到企微助手二维码添加页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-08")
    @allure.title("点击一键申卡可以正常跳转到一键申卡页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击一键申卡")
    @allure.severity(allure.severity_level.NORMAL)
    def test_mine_08_onekey_apply(self):
        """
        SKHG-MINE-08: 一键申卡入口
        已有图片：tpl1780645043689.png（一键申卡入口）、tpl1780645056148.png（授权声明页）
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
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
    @pytest.mark.xfail(reason="TODO_IMG: 需补充推荐结果立即申请按钮截图后启用", strict=False)
    def test_mine_09_onekey_flow(self):
        """
        SKHG-MINE-09: 一键申卡完整流程
        已有图片：tpl1780645043689.png（一键申卡入口）、tpl1780645056148.png（授权页）
                  tpl1780645076774.png（立即体验按钮）、tpl1780645142684.png（生成推荐按钮）
                  tpl1780645153442.png（推荐结果页）
        缺少图片：shenka_mine_onekey_apply_btn.png（推荐结果中立即申请按钮）
        注意：选项选择步骤需根据实际页面结构补充截图
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
        # 进入一键申卡
        self.page.click_onekey_apply()
        self.page.wait_seconds(2)
        # 点击立即体验（授权同意）
        self.page.click_onekey_start()
        self.page.wait_seconds(2)
        # 点击生成推荐（实际应先按提示选择各选项，此处简化）
        self.page.click_generate_recommend()
        self.page.wait_seconds(3)
        # 验证推荐结果已生成
        assert self.page.is_onekey_result_generated(), "一键申卡应已生成推荐卡片"
        # 点击推荐结果中的立即申请
        self.page.click_onekey_apply_card()
        self.page.wait_seconds(2)

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-10")
    @allure.title("点击卡片PK可以正常跳转到卡片PK页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击卡片PK")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充卡片PK页面标志截图后启用", strict=False)
    def test_mine_10_card_pk(self):
        """
        SKHG-MINE-10: 卡片PK入口
        已有图片：tpl1780645117460.png（卡片PK入口）
        缺少图片：shenka_mine_pk_page.png（PK页面标志）
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
        self.page.click_card_pk()
        self.page.wait_seconds(2)
        assert self.page.is_pk_page_displayed(), "点击卡片PK后应已跳转到卡片PK页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-11")
    @allure.title("点击个人资料可以正常跳转到个人资料页面")
    @allure.description("1. 进入我的申卡页面\n2. 点击个人资料")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充个人资料页面标志截图后启用", strict=False)
    def test_mine_11_profile(self):
        """
        SKHG-MINE-11: 个人资料入口
        已有图片：tpl1780645122884.png（个人资料入口）
        缺少图片：shenka_mine_profile_page.png（个人资料页标志）
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
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
    @pytest.mark.xfail(reason="TODO_IMG: 需补充完善信息按钮截图后启用", strict=False)
    def test_mine_12_edit_profile(self):
        """
        SKHG-MINE-12: 进入资料完善页
        缺少图片：shenka_mine_profile_page.png、shenka_mine_profile_edit_btn.png、
                  shenka_mine_profile_edit_page.png
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
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
    @pytest.mark.xfail(reason="TODO_IMG: 需补充保存按钮和成功标志截图后启用", strict=False)
    def test_mine_13_save_profile(self):
        """
        SKHG-MINE-13: 完善并保存个人资料
        缺少图片：系列个人资料字段截图、shenka_mine_profile_save_btn.png、
                  shenka_mine_profile_saved.png
        注意：各信息字段（姓名、职业等）需单独截图配置
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
        self.page.click_profile()
        self.page.wait_seconds(2)
        self.page.click_edit_profile()
        self.page.wait_seconds(2)
        # 填写并保存信息
        self.page.fill_and_save_profile()
        self.page.wait_seconds(2)
        assert self.page.is_profile_saved(), "完善个人资料并保存后应提示保存成功"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-14")
    @allure.title("在个人资料完善页点击一键申卡可以正常跳转到一键申卡页面")
    @allure.description(
        "1. 进入我的申卡-个人资料页面\n"
        "2. 进入个人资料完善填写页面\n"
        "3. 点击页面下方的一键申卡按钮"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充完善页一键申卡按钮截图后启用", strict=False)
    def test_mine_14_profile_onekey_apply(self):
        """
        SKHG-MINE-14: 完善页一键申卡按钮
        缺少图片：完善页一键申卡按钮截图、shenka_mine_onekey_page.png
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
        self.page.click_profile()
        self.page.wait_seconds(2)
        self.page.click_edit_profile()
        self.page.wait_seconds(2)
        # 点击一键申卡
        self.page.click_profile_onekey_apply()
        self.page.wait_seconds(2)
        assert self.page.is_onekey_page_loaded(), "在完善页点击一键申卡后应跳转到一键申卡页面"

    # ------------------------------------------------------------------
    @allure.story("SKHG-MINE-15")
    @allure.title("点击快速申卡区域的卡片可以直接跳转到对应卡片申卡详情页")
    @allure.description(
        "1. 进入我的申卡-个人资料页面\n"
        "2. 点击页面下方的快速申卡区域内的任意卡片"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充快速申卡区域卡片截图后启用", strict=False)
    def test_mine_15_quick_apply_card(self):
        """
        SKHG-MINE-15: 快速申卡
        缺少图片：shenka_mine_profile_page.png、shenka_mine_quick_card_item.png
        """
        self.page.click_mine_tab()
        self.page.wait_mine_page_loaded()
        self.page.click_profile()
        self.page.wait_seconds(2)
        # 点击快速申卡区域某张卡片
        self.page.click_quick_card()
        self.page.wait_seconds(2)
        # 验证已跳转到卡片申卡详情页（复用卡片详情页的标志）
        from pages.common.shenka_card_page import ShenkaCardPage
        card_page = ShenkaCardPage()
        assert card_page.is_card_detail_loaded(), "点击快速申卡区域卡片后应直接跳转到对应卡片申卡详情页"
