# -*- coding: utf-8 -*-
"""
申卡首页测试用例
模块: 首页 (SKHG-HOME-01 ~ HOME-07)
"""
import pytest
import allure
from pages.common.shenka_home_page import ShenkaHomePage


@allure.epic("银联云闪付申卡小程序")
@allure.feature("首页")
@pytest.mark.common
@pytest.mark.regression
class TestShenkaHome:
    """申卡首页测试集"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = ShenkaHomePage()

    # ------------------------------------------------------------------
    @allure.story("SKHG-HOME-01")
    @allure.title("申卡页面正常跳转")
    @allure.description(
        "1. 在云闪付小程序点击申请信用卡\n"
        "2. 查看申卡页面是否正常跳转"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_home_01_enter_shenka_page(self):
        """
        SKHG-HOME-01: 申卡页面正常跳转
        前置条件：已在云闪付小程序首页，conftest.navigate_to_target_page 已完成入口点击
        验证申卡首页能正常加载
        """
        # 申卡页面已在 session 级前置 fixture 中打开
        assert self.page.is_home_loaded(), "申卡首页应已正常加载（推荐Tab可见）"

    # ------------------------------------------------------------------
    @allure.story("SKHG-HOME-02")
    @allure.title("申卡首页推荐和附属卡Tab可以正常切换")
    @allure.description("1. 查看申卡首页推荐和附属卡是否可以切换")
    @allure.severity(allure.severity_level.NORMAL)
    def test_home_02_switch_tab(self):
        """
        SKHG-HOME-02: 推荐/附属卡Tab切换
        缺少图片：shenka_home_fushuka_tab.png、shenka_home_fushuka_selected.png
        补充截图后，去掉 @pytest.mark.xfail 即可运行
        """
        # 1. 点击附属卡Tab
        self.page.click_fushuka_tab()
        self.page.wait_seconds(1)
        # 2. 验证附属卡Tab已选中
        assert self.page.is_fushuka_tab_selected(), "附属卡Tab应已被选中"
        # 3. 点回推荐Tab
        self.page.click_recommend_tab()
        self.page.wait_seconds(1)
        # 4. 验证推荐Tab可见
        assert self.page.is_recommend_tab_visible(), "推荐Tab应已被选中"

    # ------------------------------------------------------------------
    @allure.story("SKHG-HOME-03")
    @allure.title("申请信用卡过程可以正常流转")
    @allure.description(
        "1. 进入申卡小程序首页\n"
        "2. 点击立即申请\n"
        "3. 查看申请信用过程是否可以正常流转"
    )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_home_03_apply_flow(self):
        """
        SKHG-HOME-03: 申请信用卡流转
        此用例是 myfirstscript 中脚本的核心流程入口
        """
        # 1. 点击立即申请
        self.page.click_apply_now()
        self.page.wait_seconds(2)
        # 2. 确认授权/同意弹窗
        self.page.confirm_apply()
        self.page.wait_seconds(10)
        # 3. 验证申请流程已启动（页面已跳转）
        # 注意：申请流程很长，此处仅验证成功跳转离开了首页（立即申请按钮消失）
        assert not self.page.is_home_loaded(), "点击立即申请后应已离开首页"

    # ------------------------------------------------------------------
    @allure.story("SKHG-HOME-04")
    @allure.title("申卡首页信用卡轮播图可以左右滑动")
    @allure.description("1. 查看申卡首页信用卡轮播图是否可以左右滑动")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="TODO_IMG: 需补充轮播图区域截图后启用", strict=False)
    @pytest.mark.skip
    def test_home_04_carousel_slide(self):
        """
        SKHG-HOME-04: 轮播图左右滑动
        缺少图片：shenka_home_carousel.png、shenka_home_carousel_moved.png
        补充截图后，去掉 @pytest.mark.xfail 即可运行
        """
        # 0. 确保回到首页（上一个用例可能已跳转离开）
        self.page.navigate_to_home()
        # 1. 向左滑动轮播图
        self.page.swipe_carousel_left()
        self.page.wait_seconds(1)
        # 2. 验证轮播图已滑动（图片变化）
        assert self.page.is_carousel_slidable(), "轮播图应可以左右滑动"

    # ------------------------------------------------------------------
    @allure.story("SKHG-HOME-05")
    @allure.title("点击权益文案可以展开显示权益详情")
    @allure.description("1. 点击卡片下方的权益文案")
    @allure.severity(allure.severity_level.NORMAL)
    def test_home_05_rights_expand(self):
        """
        SKHG-HOME-05: 权益详情展开
        缺少图片：shenka_home_rights_btn.png、shenka_home_rights_detail.png
        """
        self.page.navigate_to_home()
        self.page.wait_seconds(5)
        # 1. 点击权益文案按钮
        self.page.click_rights_btn()
        self.page.wait_seconds(1)
        # 2. 验证权益详情已展开
        assert self.page.is_rights_detail_expanded(), "权益详情应已展开"

    # ------------------------------------------------------------------
    @allure.story("SKHG-HOME-06")
    @allure.title("点击申卡活动可以展开申卡有礼活动详情")
    @allure.description("1. 点击卡片下方的申卡活动（云闪付专享券）")
    @allure.severity(allure.severity_level.NORMAL)
    def test_home_06_activity_expand(self):
        """
        SKHG-HOME-06: 申卡有礼活动展开
        缺少图片：shenka_home_activity_btn.png、shenka_home_activity_detail.png
        """
        self.page.navigate_to_home()
        self.page.wait_seconds(5)
        # 1. 点击申卡活动文案
        self.page.click_activity_btn()
        self.page.wait_seconds(1)
        # 2. 验证申卡有礼已展开
        assert self.page.is_activity_detail_expanded(), "申卡有礼活动详情应已展开"

    # ------------------------------------------------------------------
    @allure.story("SKHG-HOME-07")
    @allure.title("点击查看活动详情链接可跳转到申卡活动H5页面")
    @allure.description(
        "1. 点击申卡活动展开申卡有礼页面\n"
        "2. 点击详情里的[点击查看活动详情>>]链接字样"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_home_07_activity_h5_jump(self):
        """
        SKHG-HOME-07: 活动H5页面跳转
        缺少图片：shenka_home_activity_btn.png、shenka_home_activity_link.png、shenka_home_h5_page.png
        """
        # 1. 接续上一条，已展开申卡有礼
        # self.page.click_activity_btn()
        # self.page.wait_seconds(1)
        # 2. 点击查看活动详情链接
        self.page.click_activity_detail_link()
        self.page.wait_seconds(3)
        # 3. 验证已跳转到H5页面
        assert self.page.is_h5_page_displayed(), "应已跳转到申卡活动H5页面"
