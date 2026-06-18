"""
筛选页面对象 - 纯图像识别
对应模块: 查询（筛选）(SKHG-FILTER-01 ~ FILTER-08)
"""
import allure
from airtest.core.api import Template

from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("ShenkaFilterPage")

RES = "common/shenka"


class ShenkaFilterPage(BasePage):
    """筛选/查询页面对象（纯图像识别）"""

    def __init__(self):
        super().__init__(poco=None)
        # 筛选条件按钮（精选，未选中状态）
        self.filter_condition_jx = Template(
            self.resource_path(f"{RES}/shenka_filter_condition_jx.png"))

        # 筛选银行按钮（未筛选状态，全部银行）
        self.filter_bank_btn = Template(
            self.resource_path(f"{RES}/shenka_filter_bank_btn.png"))

        # 筛选银行选项（北京银行，未选中状态）
        self.filter_bank_item = Template(
            self.resource_path(f"{RES}/shenka_filter_bank_item.png"))

        # 筛选卡等级按钮（未筛选状态）
        self.filter_card_level_btn = Template(
            self.resource_path(f"{RES}/shenka_filter_card_level_btn.png"))

        # 筛选卡等级选项（金卡）
        self.filter_card_level_item = Template(
            self.resource_path(f"{RES}/shenka_filter_card_level_item.png"))

        # 筛选确认按钮
        self.filter_confirm_btn = Template(
            self.resource_path(f"{RES}/shenka_filter_confirm_btn.png"))

        # 筛选重置按钮  
        self.filter_reset_btn = Template(
            self.resource_path(f"{RES}/shenka_filter_reset_btn.png"))
        
        # 筛选卡主题按钮（未筛选状态）
        self.filter_card_theme_btn = Template(
            self.resource_path(f"{RES}/shenka_filter_card_theme_btn.png"))

        # 筛选卡主题选项（某主题，居家生活，未选中状态）
        self.filter_card_theme_item = Template(
            self.resource_path(f"{RES}/shenka_filter_card_theme_item.png"))
        
        # 筛选年费按钮（未筛选状态）
        self.filter_year_fee_btn = Template(
            self.resource_path(f"{RES}/shenka_filter_year_fee_btn.png"))

        # 筛选年费选项（不免年费，未选中状态）
        self.filter_year_fee_item = Template(
            self.resource_path(f"{RES}/shenka_filter_year_fee_item.png"))

        # 筛选更多按钮
        self.select_more_filter = Template(
            self.resource_path(f"{RES}/shenka_filter_more_btn.png"))

        # 更多筛选选项（开卡有礼）
        self.filter_more_item = Template(
            self.resource_path(f"{RES}/shenka_filter_more_item.png"))

        

    # ---- 页面验证 ----


    # ---- 页面操作 ----

    @allure.step("点击筛选条件按钮（精选）")
    def click_filter_condition_jx(self):
        """
        点击筛选条件按钮（精选）
        """
        log.info("点击筛选条件按钮（精选）")
        self.click(self.filter_condition_jx)

    @allure.step("点击选择银行筛选条件")
    def select_bank_filter(self):
        """
        切换全部银行的查询条件
        """
        log.info("点击选择银行筛选条件")
        self.click(self.filter_bank_btn)

    @allure.step("银行筛选列表选择某个银行选项")
    def select_bank_item(self):
        """
        银行筛选列表选择某个银行选项
        """
        log.info("选择某银行选项")
        self.click(self.filter_bank_item)

    @allure.step("选择卡等级筛选条件")
    def select_card_level_filter(self):
        """
        点击卡等级的筛选按钮
        """
        log.info("选择卡等级筛选条件")
        self.click(self.filter_card_level_btn)
    
    @allure.step("卡等级筛选列表选择某个卡等级选项")
    def select_card_level_item(self):
        """
        卡等级筛选列表选择某个卡等级选项
        """
        log.info("选择某卡等级选项")
        self.click(self.filter_card_level_item)
    
    @allure.step("选择卡主题筛选条件")
    def select_card_theme_filter(self):
        """
        点击卡主题的筛选按钮
        """
        log.info("选择卡主题筛选条件")
        self.click(self.filter_card_theme_btn)

    @allure.step("卡主题筛选列表选择某个卡主题选项")
    def select_card_theme_item(self):
        """
        卡主题筛选列表选择某个卡主题选项
        """
        log.info("选择某卡主题选项")
        self.click(self.filter_card_theme_item)

    @allure.step("点击筛选确认按钮")
    def click_filter_confirm_btn(self):
        """
        点击筛选确认按钮
        """
        log.info("点击筛选确认按钮")
        self.click(self.filter_confirm_btn)
    
    @allure.step("点击重置按钮")
    def click_reset_btn(self):
        """
        点击重置按钮
        """
        log.info("点击重置按钮")
        self.click(self.filter_reset_btn)

    @allure.step("选择年费筛选条件")
    def select_year_fee_filter(self):
        """
        点击年费的筛选按钮
        """
        log.info("选择年费筛选条件")
        self.click(self.filter_year_fee_btn)

    @allure.step("年费筛选列表选择某个年费选项")
    def select_year_fee_item(self):
        """
        年费筛选列表选择某个年费选项
        """
        log.info("选择某年费选项")
        self.click(self.filter_year_fee_item)

    @allure.step("点击更多筛选按钮")
    def click_more_filter(self):
        """
        点击更多筛选按钮
        """
        log.info("点击更多筛选按钮")
        self.click(self.select_more_filter)

    @allure.step("更多筛选列表选择某个选项")
    def select_more_filter_item(self):
        """
        更多筛选列表选择某个选项
        """
        log.info("选择某选项")
        self.click(self.filter_more_item)
    