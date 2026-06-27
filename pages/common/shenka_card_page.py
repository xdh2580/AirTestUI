"""
卡片详情页面对象 - 纯图像识别
对应模块: 卡片详情 (SKHG-CARD-01 ~ CARD-13)
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

        # 卡片申请页面加载标志
        self.card_apply_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_card_apply_page_indicator.png"), threshold=0.8)
        # 权益详情旁的"详情"字样按钮（点击弹浮窗）
        self.apply_page_rights_detail = Template(
            self.resource_path(f"{RES}/shenka_card_btn_rights_detail.png"))
        # 收藏图标（未收藏状态）
        self.btn_collect = Template(
            self.resource_path(f"{RES}/shenka_card_btn_collect.png"))
        # 已收藏图标/按钮
        self.indicator_already_collected = Template(
            self.resource_path(f"{RES}/shenka_card_indicator_already_collected.png"))
        # 去PK按钮
        self.btn_go_pk = Template(
            self.resource_path(f"{RES}/shenka_card_btn_go_pk.png"))
        # PK页面加载标志
        self.pk_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_card_pk_page_indicator.png"))
        # PK页面，添加卡片
        self.pk_page_add_card = Template(
            self.resource_path(f"{RES}/shenka_card_pk_page_add_card.png"))
        # PK选择卡页面标志
        self.pk_select_card_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_card_pk_select_card_page_indicator.png"))
        # PK选择卡页的Tab-我的收藏（未选中状态）
        self.pk_page_select_card_tab_my_collect = Template(
            self.resource_path(f"{RES}/shenka_card_pk_page_select_card_tab_my_collect.png"))
        # PK选择卡页的Tab-我的收藏（已选中状态）
        self.pk_page_select_card_tab_my_collect_selected = Template(
            self.resource_path(f"{RES}/shenka_card_pk_page_select_card_tab_my_collect_selected.png"))
        # PK选择卡页的Tab-热卡推荐（未选中状态）
        self.pk_page_select_card_tab_hot_recommend = Template(
            self.resource_path(f"{RES}/shenka_card_pk_page_select_card_tab_hot_recommend.png"))
        # PK选择卡页的Tab-热卡推荐（已选中状态）
        self.pk_page_select_card_tab_hot_recommend_selected = Template(
            self.resource_path(f"{RES}/shenka_card_pk_page_select_card_tab_hot_recommend_selected.png"))
        # PK选择卡列表中某张卡片
        self.pk_card_item_check_box = Template(
            self.resource_path(f"{RES}/shenka_card_pk_card_item_check_box.png"))
        # 开始PK按钮
        self.btn_start_pk = Template(
            self.resource_path(f"{RES}/shenka_card_btn_start_pk.png"))
        # PK结果页标志(两个去申请按钮)
        self.pk_result_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_card_pk_result_page_indicator.png"))
        # PK结果页去申请按钮
        self.pk_goto_apply_btn = Template(
            self.resource_path(f"{RES}/shenka_card_pk_goto_apply_btn.png"))
        # pk页面点击去申请按钮触发的三要素确认页面
        self.apply_confirm_popup = Template(
            self.resource_path(f"{RES}/shenka_card_apply_confirm_popup.png"))
        # 收藏成功提示
        self.collect_success_tip = Template(
            self.resource_path(f"{RES}/shenka_card_collect_success_tip.png"))
        # 收藏成功弹窗中"去看看"按钮
        self.btn_goto_collect = Template(
            self.resource_path(f"{RES}/shenka_card_goto_collect.png"))
        # 取消收藏后提示"已取消收藏"
        self.cancel_collect_tip = Template(
            self.resource_path(f"{RES}/shenka_card_cancel_collect_tip.png"), threshold=0.7)
        # 权益详情浮窗标志(在PK页面点击卡片弹出)
        self.rights_popup = Template(
            self.resource_path(f"{RES}/shenka_card_rights_popup_in_pk_page.png"))
        # 权益详情浮窗关闭按钮
        self.rights_popup_close_btn = Template(
            self.resource_path(f"{RES}/shenka_card_rights_popup_close_btn.png"))
        # PK页面查看更多卡片按钮
        self.pk_page_more_cards = Template(
            self.resource_path(f"{RES}/shenka_card_pk_more_btn.png"), threshold=0.8)
        # 全部卡片页面标志
        self.all_cards_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_card_all_cards_page.png"), threshold=0.8)
        # pk页去申请-三要素弹窗下一步按钮
        self.apply_confirm_agree_next_btn = Template(
            self.resource_path(f"{RES}/shenka_card_apply_confirm_agree_next_btn.png"))
        # pk页去申请-三要素弹窗下一步之后-确认按钮
        self.apply_confirm_agree_confirm_btn = Template(
            self.resource_path(f"{RES}/shenka_card_apply_confirm_agree_confirm_btn.png"), threshold=0.8)

    # ---- 页面验证 ----
    @allure.step("判断卡片申请页面是否已加载")
    def is_card_apply_page_displayed(self) -> bool:
        return self.is_exists(self.card_apply_page_indicator)

    @allure.step("判断权益详情浮窗是否已弹出")
    def is_rights_popup_displayed_in_pk_page(self) -> bool:
        return self.is_exists(self.rights_popup)    

    @allure.step("判断卡片是否已收藏")
    def is_card_collected(self) -> bool:
        return self.is_exists(self.indicator_already_collected)

    @allure.step("判断收藏成功提示是否出现")
    def is_collect_success_displayed(self) -> bool:
        return self.is_exists(self.collect_success_tip)

    @allure.step("判断取消收藏提示是否出现")
    def is_cancel_collect_displayed(self) -> bool:
        return self.wait_for_element(self.cancel_collect_tip, timeout=3, interval=0.2)

    @allure.step("判断PK页面是否已加载")
    def is_pk_page_loaded(self) -> bool:
        return self.is_exists(self.pk_page_indicator)

    @allure.step("判断卡片pk选择卡片页面的tab是否已切换-我的收藏")
    def is_pk_tab_my_collect_displayed(self) -> bool:
        return self.is_exists(self.pk_page_select_card_tab_my_collect_selected)

    @allure.step("判断卡片pk选择卡片页面的tab是否已切换-热卡推荐")
    def is_pk_tab_hot_recommend_displayed(self) -> bool:
        return self.is_exists(self.pk_page_select_card_tab_hot_recommend_selected)

    @allure.step("判断PK选择卡片页是否已弹出")
    def is_pk_select_page_displayed(self) -> bool:
        return self.is_exists(self.pk_select_card_page_indicator)

    @allure.step("判断PK结果页是否已加载")
    def is_pk_result_page_loaded(self) -> bool:
        """
        判断PK结果页是否已加载（滑到底部，通过两个去申请按钮判断）
        """
        # 向上滑动屏幕5次，保证能滑到底部
        for _ in range(5):
            self.swipe_screen(direction="up")
        return self.is_exists(self.pk_result_page_indicator)

    @allure.step("判断pk页点击去申请后，三要素确认页面是否出现")
    def is_apply_confirm_popup_displayed(self) -> bool:
        return self.is_exists(self.apply_confirm_popup)

    @allure.step("判断银行申请页是否已跳转")
    def is_bank_apply_page_displayed(self) -> bool:
        return not self.is_exists(self.apply_confirm_agree_confirm_btn)

    @allure.step("判断全部卡片页是否已跳转")
    def is_all_cards_page_displayed(self) -> bool:
        return self.is_exists(self.all_cards_page_indicator)

    # ---- 页面操作 ----

    @allure.step("点击银行专享权益旁的详情")
    def click_rights_detail(self):
        """点击银行专享权益旁"详情"字样，弹出权益浮窗"""
        log.info("点击权益详情按钮")
        self.click(self.apply_page_rights_detail)

    @allure.step("点击收藏图标")
    def click_collect(self):
        """点击收藏图标收藏/取消收藏卡片"""
        log.info("点击收藏图标")
        self.wait_seconds(1)
        self.click(self.btn_collect)
    
    @allure.step("点击取消收藏图标")
    def click_cancel_collect(self):
        """点击取消收藏图标取消收藏卡片"""
        log.info("点击取消收藏图标")
        self.wait_seconds(1)
        self.click(self.indicator_already_collected)

    @allure.step("点击收藏成功弹窗中的去看看")
    def click_goto_collect(self):
        """
        点击收藏成功提示中的"去看看"按钮，跳转到我的收藏
        """
        log.info("点击去看看")
        self.click(self.btn_goto_collect)

    @allure.step("点击去PK")
    def click_go_pk(self):
        """点击去PK按钮"""
        log.info("点击去PK")
        self.click(self.btn_go_pk)

    @allure.step("点击PK页已选卡片图片（查看权益）")
    def click_pk_selected_card(self):
        """
        点击PK页中已选卡片的图片，弹窗显示权益信息
        采用相对坐标点击已选卡片图片
        """
        log.info("点击PK已选卡片图片")
        self.click_by_ratio(0.253, 0.192)

    @allure.step("关闭权益详情浮窗（在PK页面）")
    def close_rights_popup(self):
        """关闭权益详情浮窗"""
        log.info("关闭权益详情浮窗（在PK页面）")
        self.click(self.rights_popup_close_btn)

    @allure.step("点击PK页添加卡片（进入选择页）")
    def click_pk_add_card(self):
        """点击PK页右侧添加卡片，进入选择卡片页，默认左边已选一张卡"""
        log.info("点击PK添加卡片")
        self.click(self.pk_page_add_card)

    @allure.step("切换PK选择卡片页的Tab: 我的收藏")
    def click_pk_tab_my_collect(self):
        """切换 PK 选择卡片页的 Tab: 我的收藏"""
        log.info("切换PK选择页Tab: 我的收藏")
        self.click(self.pk_page_select_card_tab_my_collect)

    @allure.step("切换PK选择卡片页的Tab: 热卡推荐")
    def click_pk_tab_hot_recommend(self):
        """切换 PK 选择卡片页的 Tab: 热卡推荐"""
        log.info("切换PK选择页Tab: 热卡推荐")
        self.click(self.pk_page_select_card_tab_hot_recommend)

    @allure.step("在PK选择页选择某张卡片")
    def select_pk_card_item(self):
        """在PK选择卡片页中选择某张卡进行PK"""
        log.info("选择PK卡片")
        self.click(self.pk_card_item_check_box)

    @allure.step("点击开始PK")
    def click_start_pk(self):
        """点击开始PK按钮"""
        log.info("点击开始PK")
        self.click(self.btn_start_pk)

    @allure.step("点击PK结果页去申请按钮")
    def click_pk_goto_apply(self):
        """点击PK结果页中某张卡的去申请按钮"""
        log.info("点击PK结果页去申请")
        self.click(self.pk_goto_apply_btn)

    @allure.step("点击PK页查看更多卡片")
    def click_pk_more_cards(self):
        """
        点击PK页底部"查看更多卡片"跳转到全部卡片页
        TODO_IMG: 需补充查看更多卡片按钮截图 shenka_card_pk_more_btn.png
        """
        log.info("点击PK页查看更多卡片")
        self.click(self.pk_page_more_cards)

    @allure.step("同意三要素确认弹窗-并确认")
    def confirm_apply_popup(self):
        """点击pk页面-去申请-三要素确认弹窗中的下一步提交申请"""
        log.info("同意三要素确认并提交申请")
        self.click_checkbox()
        self.wait_seconds(1)
        self.click(self.apply_confirm_agree_next_btn)
        self.wait_seconds(1)
        self.click(self.apply_confirm_agree_confirm_btn)
