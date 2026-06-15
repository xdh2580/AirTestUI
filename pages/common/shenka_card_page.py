"""
卡片详情页面对象 - 纯图像识别
对应模块: 卡片详情 (SKHG-CARD-01 ~ CARD-13)

【资源缺失说明】
已有图片（来自 myfirstscript，申请流转过程中包含卡片详情和PK相关操作）：
  以下是 myfirstscript 中对应卡片详情/PK页的已有图片（按操作顺序推断）：
  - shenka_card_detail_page.png: 卡片详情页面标志（等待）
  - shenka_card_detail_clickable.png: 卡片详情页面标志（点击某处）
  - shenka_card_btn_rights_detail.png: 某确认/下一步按钮
  - shenka_card_btn_back.png: 返回/小按钮（未在代码中引用）
  - shenka_card_btn_collect.png: 收藏图标（未收藏）
  - shenka_card_btn_go_pk.png: 去PK按钮
  - shenka_card_pk_page_indicator.png: PK页面标志（等待）
  - shenka_card_pk_selected_card.png: 已选卡片图片（点击弹权益）
  - shenka_card_pk_select_page.png: PK选择卡页面标志
  - shenka_card_pk_tab_item.png: 浏览历史/我的收藏/热门推荐某Tab
  - shenka_card_pk_card_item.png: PK选择卡列表中某卡片
  - shenka_card_pk_select_btn.png: 选择卡片按钮
  - shenka_card_btn_start_pk.png: 开始PK按钮
  - shenka_card_pk_result_page.png: PK结果页标志
  - shenka_card_pk_goto_apply_btn.png: PK结果页去申请按钮
  - shenka_card_apply_confirm_popup.png: 三要素确认弹窗标志（立即申请触发）
  - shenka_card_apply_confirm_agree_btn.png: 三要素确认弹窗同意按钮
  - shenka_card_bank_apply_page.png: 跳转到银行申请页标志

需补充（TODO_IMG）：
  - 首页某卡片条目（点击进入详情）(shenka_card_list_item.png)
  - 收藏成功提示标志 (shenka_card_collect_success.png)
  - 去看看按钮（收藏成功弹窗中）(shenka_card_goto_collect.png)
  - 我的收藏页面标志 (shenka_card_my_collect_page.png)
  - 取消收藏后提示 (shenka_card_cancel_collect_tip.png)
  - 权益详情/申卡有礼浮窗 (shenka_card_rights_popup.png)
  - PK页查看更多卡片按钮 (shenka_card_pk_more_btn.png)
  - 全部卡片页面标志 (shenka_card_all_cards_page.png)
"""
import allure
from airtest.core.api import Template

from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("ShenkaCardPage")

RES = "common/shenka"


class ShenkaCardPage(BasePage):
    """卡片详情页面对象（纯图像识别）"""

    def __init__(self):
        super().__init__(poco=None)

        # ---------- 已有图片资源 ----------
        # 卡片详情页面加载标志（等待）
        self.card_detail_page = Template(
            self.resource_path(f"{RES}/shenka_card_detail_page.png"),
            record_pos=(-0.003, 0.919), resolution=(1216, 2640), threshold=0.8,
        )
        # 卡片详情页面（可交互）
        self.card_detail_clickable = Template(
            self.resource_path(f"{RES}/shenka_card_detail_clickable.png"),
            record_pos=(0.002, 0.918), resolution=(1216, 2640), threshold=0.8,
        )
        # 权益详情旁的"详情"字样按钮（点击弹浮窗）
        self.btn_rights_detail = Template(
            self.resource_path(f"{RES}/shenka_card_btn_rights_detail.png"),
            record_pos=(0.002, 0.922), resolution=(1216, 2640), threshold=0.8,
        )
        # 收藏图标（未收藏状态）
        self.btn_collect = Template(
            self.resource_path(f"{RES}/shenka_card_btn_collect.png"),
            record_pos=(-0.42, -0.764), resolution=(1216, 2640), threshold=0.8,
        )
        # 去PK按钮
        self.btn_go_pk = Template(
            self.resource_path(f"{RES}/shenka_card_btn_go_pk.png"),
            record_pos=(-0.005, 0.366), resolution=(1216, 2640), threshold=0.8,
        )
        # PK页面加载标志
        self.pk_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_card_pk_page_indicator.png"),
            record_pos=(-0.005, 0.926), resolution=(1216, 2640), threshold=0.8,
        )
        # PK页已选卡片图片（点击可弹出权益）
        self.pk_selected_card = Template(
            self.resource_path(f"{RES}/shenka_card_pk_selected_card.png"),
            record_pos=(-0.441, 0.174), resolution=(1216, 2640), threshold=0.8,
        )
        # PK选择卡片页面标志
        self.pk_select_page = Template(
            self.resource_path(f"{RES}/shenka_card_pk_select_page.png"),
            record_pos=(-0.382, 0.603), resolution=(1216, 2640), threshold=0.8,
        )
        # PK选择卡页的Tab切换（浏览历史/我的收藏/热门推荐）
        self.pk_tab_item = Template(
            self.resource_path(f"{RES}/shenka_card_pk_tab_item.png"),
            record_pos=(-0.384, 0.611), resolution=(1216, 2640), threshold=0.8,
        )
        # PK选择卡列表中某张卡片
        self.pk_card_item = Template(
            self.resource_path(f"{RES}/shenka_card_pk_card_item.png"),
            record_pos=(-0.359, -0.501), resolution=(1216, 2640), threshold=0.8,
        )
        # 选择卡片确认按钮
        self.pk_select_btn = Template(
            self.resource_path(f"{RES}/shenka_card_pk_select_btn.png"),
            record_pos=(-0.388, -0.438), resolution=(1216, 2640), threshold=0.8,
        )
        # 开始PK按钮
        self.btn_start_pk = Template(
            self.resource_path(f"{RES}/shenka_card_btn_start_pk.png"),
            record_pos=(-0.032, 0.613), resolution=(1216, 2640), threshold=0.8,
        )
        # PK结果页标志
        self.pk_result_page = Template(
            self.resource_path(f"{RES}/shenka_card_pk_result_page.png"),
            record_pos=(-0.109, -0.247), resolution=(1216, 2640), threshold=0.8,
        )
        # PK结果页去申请按钮
        self.pk_goto_apply_btn = Template(
            self.resource_path(f"{RES}/shenka_card_pk_goto_apply_btn.png"),
            record_pos=(-0.111, -0.247), resolution=(1216, 2640), threshold=0.8,
        )
        # 立即申请按钮触发的三要素确认弹窗
        self.apply_confirm_popup = Template(
            self.resource_path(f"{RES}/shenka_card_apply_confirm_popup.png"),
            record_pos=(0.064, 0.199), resolution=(1216, 2640), threshold=0.8,
        )
        # 三要素弹窗同意按钮
        self.apply_confirm_agree_btn = Template(
            self.resource_path(f"{RES}/shenka_card_apply_confirm_agree_btn.png"),
            record_pos=(0.345, 0.206), resolution=(1216, 2640), threshold=0.8,
        )
        # 跳转到银行申请页标志
        self.bank_apply_page = Template(
            self.resource_path(f"{RES}/shenka_card_bank_apply_page.png"),
            record_pos=(-0.141, -0.39), resolution=(1216, 2640), threshold=0.7,
        )
        # 立即申请按钮（卡片详情底部）
        self.btn_apply_card = Template(
            self.resource_path(f"{RES}/shenka_card_btn_apply_card.png"),
            record_pos=(-0.007, 0.683), resolution=(1216, 2640), threshold=0.8,
        )

        # ---------- 待补充图片资源（TODO_IMG）----------
        # 首页卡片列表中某张卡片条目
        # self.card_list_item = Template(
        #     self.resource_path(f"{RES}/shenka_card_list_item.png"), threshold=0.8)

        # 收藏成功提示
        # self.collect_success_tip = Template(
        #     self.resource_path(f"{RES}/shenka_card_collect_success.png"), threshold=0.7)

        # 收藏成功弹窗中"去看看"按钮
        # self.btn_goto_collect = Template(
        #     self.resource_path(f"{RES}/shenka_card_goto_collect.png"), threshold=0.8)

        # 我的收藏页面标志
        # self.my_collect_page = Template(
        #     self.resource_path(f"{RES}/shenka_card_my_collect_page.png"), threshold=0.8)

        # 取消收藏后提示"已取消收藏"
        # self.cancel_collect_tip = Template(
        #     self.resource_path(f"{RES}/shenka_card_cancel_collect_tip.png"), threshold=0.7)

        # 权益详情/申卡有礼浮窗标志
        # self.rights_popup = Template(
        #     self.resource_path(f"{RES}/shenka_card_rights_popup.png"), threshold=0.7)

        # PK页面查看更多卡片按钮
        # self.btn_pk_more_cards = Template(
        #     self.resource_path(f"{RES}/shenka_card_pk_more_btn.png"), threshold=0.8)

        # 全部卡片页面标志
        # self.all_cards_page = Template(
        #     self.resource_path(f"{RES}/shenka_card_all_cards_page.png"), threshold=0.8)

    # ---- 页面验证 ----

    @allure.step("等待卡片详情页加载")
    def wait_card_detail_loaded(self, timeout=15):
        """等待卡片详情页加载完成"""
        log.info("等待卡片详情页加载")
        return self.wait_for_element(self.card_detail_page, timeout=timeout)

    @allure.step("判断卡片详情页是否已加载")
    def is_card_detail_loaded(self) -> bool:
        return self.is_exists(self.card_detail_page)

    @allure.step("判断权益详情浮窗是否已弹出")
    def is_rights_popup_displayed(self) -> bool:
        """
        TODO_IMG: 需补充权益详情浮窗截图 shenka_card_rights_popup.png
        """
        raise NotImplementedError("TODO_IMG: 需补充权益详情浮窗截图 shenka_card_rights_popup.png")

    @allure.step("判断收藏成功提示是否出现")
    def is_collect_success_displayed(self) -> bool:
        """
        TODO_IMG: 需补充收藏成功提示截图 shenka_card_collect_success.png
        """
        raise NotImplementedError("TODO_IMG: 需补充收藏成功提示截图 shenka_card_collect_success.png")

    @allure.step("判断取消收藏提示是否出现")
    def is_cancel_collect_displayed(self) -> bool:
        """
        TODO_IMG: 需补充取消收藏提示截图 shenka_card_cancel_collect_tip.png
        """
        raise NotImplementedError("TODO_IMG: 需补充取消收藏提示截图 shenka_card_cancel_collect_tip.png")

    @allure.step("判断我的收藏页是否已打开")
    def is_my_collect_page_displayed(self) -> bool:
        """
        TODO_IMG: 需补充我的收藏页面标志截图 shenka_card_my_collect_page.png
        """
        raise NotImplementedError("TODO_IMG: 需补充我的收藏页面标志截图 shenka_card_my_collect_page.png")

    @allure.step("判断PK页面是否已加载")
    def is_pk_page_loaded(self) -> bool:
        return self.is_exists(self.pk_page_indicator)

    @allure.step("判断PK选择卡片页是否已弹出")
    def is_pk_select_page_displayed(self) -> bool:
        return self.is_exists(self.pk_select_page)

    @allure.step("判断PK结果页是否已加载")
    def is_pk_result_page_loaded(self) -> bool:
        return self.is_exists(self.pk_result_page)

    @allure.step("判断三要素确认弹窗是否出现")
    def is_apply_confirm_popup_displayed(self) -> bool:
        return self.is_exists(self.apply_confirm_popup)

    @allure.step("判断银行申请页是否已跳转")
    def is_bank_apply_page_displayed(self) -> bool:
        return self.is_exists(self.bank_apply_page)

    @allure.step("判断全部卡片页是否已跳转")
    def is_all_cards_page_displayed(self) -> bool:
        """
        TODO_IMG: 需补充全部卡片页面标志截图 shenka_card_all_cards_page.png
        """
        raise NotImplementedError("TODO_IMG: 需补充全部卡片页面标志截图 shenka_card_all_cards_page.png")

    # ---- 页面操作 ----

    @allure.step("点击首页卡片条目（进入详情）")
    def click_card_item(self):
        """
        点击首页列表中的某张卡片进入详情页
        TODO_IMG: 需补充卡片列表条目截图 shenka_card_list_item.png
        """
        log.info("点击卡片条目进入详情")
        raise NotImplementedError("TODO_IMG: 需补充卡片列表条目截图 shenka_card_list_item.png")

    @allure.step("点击银行专享权益旁的详情")
    def click_rights_detail(self):
        """点击银行专享权益旁"详情"字样，弹出权益浮窗"""
        log.info("点击权益详情按钮")
        self.wait_for_element(self.btn_rights_detail)
        self.click(self.btn_rights_detail)

    @allure.step("点击收藏图标")
    def click_collect(self):
        """点击收藏图标收藏/取消收藏卡片"""
        log.info("点击收藏图标")
        self.wait_seconds(1)
        self.click(self.btn_collect)

    @allure.step("点击收藏成功弹窗中的去看看")
    def click_goto_collect(self):
        """
        点击收藏成功提示中的"去看看"按钮，跳转到我的收藏
        TODO_IMG: 需补充去看看按钮截图 shenka_card_goto_collect.png
        """
        log.info("点击去看看")
        raise NotImplementedError("TODO_IMG: 需补充去看看按钮截图 shenka_card_goto_collect.png")

    @allure.step("点击去PK")
    def click_go_pk(self):
        """点击去PK按钮"""
        log.info("点击去PK")
        self.wait_for_element(self.btn_go_pk)
        self.click(self.btn_go_pk)

    @allure.step("点击PK页已选卡片图片（查看权益）")
    def click_pk_selected_card(self):
        """点击PK页中已选卡片的图片，弹窗显示权益信息"""
        log.info("点击PK已选卡片图片")
        self.wait_for_element(self.pk_page_indicator)
        self.click(self.pk_selected_card)

    @allure.step("点击PK页添加卡片（进入选择页）")
    def click_pk_add_card(self):
        """点击PK页右侧添加卡片，进入选择卡片页"""
        log.info("点击PK添加卡片")
        self.wait_for_element(self.pk_page_indicator)
        self.click(self.pk_select_page)

    @allure.step("切换PK选择卡片页的Tab: {tab_name}")
    def click_pk_tab(self, tab_name: str = "浏览历史"):
        """
        切换 PK 选择卡片页中的 Tab（浏览历史/我的收藏/热门推荐）
        注意：当前仅有一张Tab截图，三个Tab需各自截图并配置
        """
        log.info(f"切换PK选择页Tab: {tab_name}")
        self.wait_for_element(self.pk_select_page)
        self.click(self.pk_tab_item)

    @allure.step("在PK选择页选择某张卡片")
    def select_pk_card(self):
        """在PK选择卡片页中选择某张卡进行PK"""
        log.info("选择PK卡片")
        self.wait_for_element(self.pk_card_item)
        self.click(self.pk_card_item)

    @allure.step("点击开始PK")
    def click_start_pk(self):
        """点击开始PK按钮"""
        log.info("点击开始PK")
        self.wait_for_element(self.btn_start_pk)
        self.click(self.btn_start_pk)

    @allure.step("点击PK结果页去申请按钮")
    def click_pk_goto_apply(self):
        """点击PK结果页中某张卡的去申请按钮"""
        log.info("点击PK结果页去申请")
        self.wait_for_element(self.pk_result_page)
        self.click(self.pk_goto_apply_btn)

    @allure.step("点击PK页查看更多卡片")
    def click_pk_more_cards(self):
        """
        点击PK页底部"查看更多卡片"跳转到全部卡片页
        TODO_IMG: 需补充查看更多卡片按钮截图 shenka_card_pk_more_btn.png
        """
        log.info("点击PK页查看更多卡片")
        raise NotImplementedError("TODO_IMG: 需补充查看更多卡片按钮截图 shenka_card_pk_more_btn.png")

    @allure.step("点击立即申请按钮")
    def click_apply_card(self):
        """点击卡片详情页底部立即申请按钮"""
        log.info("点击立即申请")
        self.wait_for_element(self.btn_apply_card)
        self.click(self.btn_apply_card)

    @allure.step("同意三要素确认弹窗")
    def confirm_apply_popup(self):
        """点击三要素确认弹窗中的同意按钮"""
        log.info("同意三要素确认")
        self.wait_for_element(self.apply_confirm_popup)
        self.click(self.apply_confirm_agree_btn)
