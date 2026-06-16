"""
申卡首页页面对象 - 纯图像识别
对应模块: 首页 (SKHG-HOME-01 ~ HOME-07)

【资源缺失说明】
- 以下元素需要补充截图（标注 TODO_IMG）：
  - 卡片轮播图区域 (shenka_home_carousel.png)
  - 权益文案展开按钮 (shenka_home_rights_btn.png)
  - 权益详情展开后的标志 (shenka_home_rights_detail.png)
  - 申卡活动（云闪付专享券）文案按钮 (shenka_home_activity_btn.png)
  - 申卡有礼展开标志 (shenka_home_activity_detail.png)
  - 点击查看活动详情链接标志 (shenka_home_activity_link.png)
  - 活动H5页面标志 (shenka_home_h5_page.png)
  - 申请信用卡入口（云闪付小程序中） (yunshan_apply_entry.png)

- 以下元素已有图片（来自 myfirstscript）：
  - shenka_home_recommend_tab.png: 申卡首页推荐Tab（等待标志）
  - shenka_home_recommend_tab_click.png: 申卡首页推荐Tab（点击）
  - shenka_card_btn_apply_card.png: 下一个页面等待标志
"""
import allure
from airtest.core.api import Template

from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("ShenkaHomePage")

RES = "common/shenka"


class ShenkaHomePage(BasePage):
    """申卡首页页面对象（纯图像识别）"""

    def __init__(self):
        super().__init__(poco=None)

        # ---------- 已有图片资源 ----------
        # 申卡首页推荐Tab(已选中状态) - 等待页面加载的锚点
        self.home_recommend_tab = Template(
            self.resource_path(f"{RES}/shenka_home_recommend_tab.png"))
        # 申卡首页推荐Tab - 未选中状态
        self.home_recommend_tab_click = Template(
            self.resource_path(f"{RES}/shenka_home_recommend_tab_click.png"),)
        # 立即申请按钮（申请流转入口）
        self.btn_apply_now = Template(
            self.resource_path(f"{RES}/shenka_home_btn_apply_now.png"))
        # 申请流程中三要素确认按钮（同意）
        self.btn_apply_confirm = Template(
            self.resource_path(f"{RES}/shenka_home_btn_apply_confirm.png"))

        # ---------- 待补充图片资源（TODO_IMG） ----------
        # 推荐/附属卡 Tab 切换标志（用于 HOME-02）
        # self.tab_tuijian = Template(
        #     self.resource_path(f"{RES}/shenka_home_recommend_tab.png"))
        self.tab_fushuka = Template(
            self.resource_path(f"{RES}/shenka_home_fushuka_tab.png"))
        self.tab_fushuka_selected = Template(
            self.resource_path(f"{RES}/shenka_home_fushuka_selected.png"))

        # 轮播图区域（用于 HOME-04 滑动验证）
        # self.carousel_area = Template(
        #     self.resource_path(f"{RES}/shenka_home_carousel.png"))
        # self.carousel_moved = Template(
        #     self.resource_path(f"{RES}/shenka_home_carousel_moved.png"))

        # 权益文案按钮（用于 HOME-05）
        # self.btn_rights = Template(
        #     self.resource_path(f"{RES}/shenka_home_rights_btn.png"))
        self.rights_detail_indicator = Template(
            self.resource_path(f"{RES}/shenka_home_rights_detail.png"))

        # 申卡活动文案按钮（用于 HOME-06/07）
        self.btn_activity = Template(
            self.resource_path(f"{RES}/shenka_home_activity_btn.png"))
        self.activity_detail_indicator = Template(
            self.resource_path(f"{RES}/shenka_home_activity_detail.png"))
        self.link_activity_detail = Template(
            self.resource_path(f"{RES}/shenka_home_activity_link.png"))
        self.h5_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_home_h5_page.png"))

        # 申请信用卡入口（云闪付小程序中，用于 HOME-01）
        # self.apply_entry_in_yunshansfu = Template(
        #     self.resource_path(f"{RES}/yunshan_apply_entry.png"))

        # 选择城市入口
        self.select_city_entry = Template(
            self.resource_path(f"{RES}/shenka_home_select_city_entry.png"))

    # ---- 页面验证 ----

    @allure.step("等待申卡首页加载")
    def wait_home_loaded(self, timeout=15):
        """等待申卡首页加载完成（等待推荐Tab出现）"""
        log.info("等待申卡首页加载")
        return self.wait_for_element(self.home_recommend_tab, timeout=timeout)

    @allure.step("判断申卡首页是否已加载")
    def is_home_loaded(self) -> bool:
        """判断申卡首页是否已加载"""
        return self.is_exists(self.home_recommend_tab)

    @allure.step("判断推荐Tab是否可见")
    def is_recommend_tab_visible(self) -> bool:
        """判断推荐Tab是否可见（用于 HOME-02 切换验证）"""
        return self.is_exists(self.home_recommend_tab)

    @allure.step("判断附属卡Tab是否已选中")
    def is_fushuka_tab_selected(self) -> bool:
        """
        判断附属卡Tab是否已切换选中
        """
        return self.is_exists(self.tab_fushuka_selected)

    @allure.step("判断轮播图是否可滑动")
    def is_carousel_slidable(self) -> bool:
        """
        判断轮播图是否可滑动
        TODO_IMG: 需提供轮播图区域截图 shenka_home_carousel.png 及滑动后变化截图
        """
        raise NotImplementedError("TODO_IMG: 需补充轮播图区域截图 shenka_home_carousel.png")

    @allure.step("判断权益详情是否已展开")
    def is_rights_detail_expanded(self) -> bool:
        """
        判断权益详情是否已展开
        TODO_IMG: 需提供权益详情展开后的标志截图 shenka_home_rights_detail.png
        """
        return self.is_exists(self.rights_detail_indicator)

    @allure.step("判断申卡有礼详情是否已展开")
    def is_activity_detail_expanded(self) -> bool:
        """
        判断申卡有礼活动详情是否已展开
        """
        return self.is_exists(self.activity_detail_indicator)

    @allure.step("判断是否跳转到活动H5页面")
    def is_h5_page_displayed(self) -> bool:
        """
        判断是否跳转到申卡活动H5页面
        """
        return self.is_exists(self.h5_page_indicator)

    # ---- 页面操作 ----

    @allure.step("点击附属卡Tab")
    def click_fushuka_tab(self):
        """
        点击附属卡Tab（切换到附属卡页签）
        """
        log.info("点击附属卡Tab")
        self.click(self.tab_fushuka)

    @allure.step("点击推荐Tab")
    def click_recommend_tab(self):
        """点击推荐Tab（切换回推荐页签）"""
        log.info("点击推荐Tab")
        self.click(self.home_recommend_tab_click)

    @allure.step("向左滑动轮播图")
    def swipe_carousel_left(self):
        """
        向左滑动轮播图
        TODO_IMG: 需先确认轮播图在页面中的大概位置，再通过 swipe 操作
        当前使用屏幕通用向左滑动，可能需要调整坐标
        """
        log.info("向左滑动轮播图")
        self.swipe_screen("left")

    @allure.step("向右滑动轮播图")
    def swipe_carousel_right(self):
        """向右滑动轮播图"""
        log.info("向右滑动轮播图")
        self.swipe_screen("right")

    @allure.step("点击权益文案（展开权益详情）")
    def click_rights_btn(self):
        """
        点击卡片权益文案展开详情,此处用相对坐标
        """
        log.info("点击权益文案")
        self.click_by_ratio(0.5, 0.485)

    @allure.step("点击申卡活动文案（展开申卡有礼）")
    def click_activity_btn(self):
        """
        点击申卡活动（云闪付专享券）文案，展开申卡有礼
        """
        log.info("点击申卡活动文案")
        self.click(self.btn_activity)

    @allure.step("点击查看活动详情链接")
    def click_activity_detail_link(self):
        """
        点击申卡有礼页面中的"点击查看活动详情>>"链接
        TODO_IMG: 需补充活动详情链接截图 shenka_home_activity_link.png
        """
        log.info("点击查看活动详情链接")
        self.click(self.link_activity_detail)

    @allure.step("点击立即申请按钮")
    def click_apply_now(self):
        """点击立即申请按钮（开始申请信用卡流程）"""
        log.info("点击立即申请")
        self.wait_for_element(self.btn_apply_now)
        self.click(self.btn_apply_now)

    @allure.step("确认申请授权")
    def confirm_apply(self):
        """点击申请流程中的确认/同意按钮"""
        log.info("确认申请授权")
        self.wait_for_element(self.btn_apply_confirm)
        self.click(self.btn_apply_confirm)

    @allure.step("点击城市选择")
    def click_select_city_entry(self):
        """点击城市选择入口"""
        log.info("点击城市选择入口")
        self.wait_for_element(self.select_city_entry)
        self.click(self.select_city_entry)
