"""
筛选页面对象 - 纯图像识别
对应模块: 查询（筛选）(SKHG-FILTER-01 ~ FILTER-08)

【资源缺失说明】
脚本中有部分筛选相关图片可用（切换筛选条件步骤），需要补充的截图如下：
已有（来自 myfirstscript，申请流程中的筛选操作）：
  - shenka_filter_swipe_area.png: 筛选组件区域（滑动起点）
  - shenka_filter_condition_btn.png: 某筛选条件按钮

需补充（TODO_IMG）：
  - 默认筛选条件Tab（全部）(shenka_filter_all_tab.png)
  - 银行筛选下拉入口 (shenka_filter_bank_btn.png)
  - 某银行选项 (shenka_filter_bank_item.png)
  - 卡等级筛选入口 (shenka_filter_level_btn.png)
  - 某卡等级选项 (shenka_filter_level_item.png)
  - 卡主题筛选入口 (shenka_filter_theme_btn.png)
  - 某卡主题选项 (shenka_filter_theme_item.png)
  - 年费筛选入口 (shenka_filter_fee_btn.png)
  - 某年费选项 (shenka_filter_fee_item.png)
  - 更多筛选入口按钮 (shenka_filter_more_btn.png)
  - 更多筛选浮窗标志 (shenka_filter_more_panel.png)
  - 某服务/标签选项 (shenka_filter_tag_item.png)
  - 重置按钮 (shenka_filter_reset_btn.png)
  - 筛选结果刷新标志 (shenka_filter_result.png)
  - 特色服务Tag（如精选、免年费等）(shenka_filter_special_tag.png)
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

        # ---------- 已有图片资源 ----------
        # 筛选条件滑动区域（用于滑动切换筛选条件）
        self.filter_swipe_area = Template(
            self.resource_path(f"{RES}/shenka_filter_swipe_area.png"),
            record_pos=(0.0, 0.165), resolution=(1216, 2640),
            threshold=0.7,
        )
        # 某筛选条件按钮（申请流程中出现的）
        self.filter_condition_btn = Template(
            self.resource_path(f"{RES}/shenka_filter_condition_btn.png"),
            record_pos=(-0.34, 0.449), resolution=(1216, 2640),
            threshold=0.8,
        )

        self.filter_all_card_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_filter_all_card_page_indicator.png"))

        self.filter_all_card_page_indicator2 = Template(
            self.resource_path(f"{RES}/shenka_filter_all_card_page_indicator2.png"))

        # ---------- 待补充图片资源（TODO_IMG）----------
        # 全部/默认筛选Tab
        # self.filter_all_tab = Template(
        #     self.resource_path(f"{RES}/shenka_filter_all_tab.png"), threshold=0.8)

        # 银行筛选入口
        # self.filter_bank_btn = Template(
        #     self.resource_path(f"{RES}/shenka_filter_bank_btn.png"), threshold=0.8)
        # self.filter_bank_item = Template(
        #     self.resource_path(f"{RES}/shenka_filter_bank_item.png"), threshold=0.8)

        # 卡等级筛选入口
        # self.filter_level_btn = Template(
        #     self.resource_path(f"{RES}/shenka_filter_level_btn.png"), threshold=0.8)
        # self.filter_level_item = Template(
        #     self.resource_path(f"{RES}/shenka_filter_level_item.png"), threshold=0.8)

        # 卡主题筛选入口
        # self.filter_theme_btn = Template(
        #     self.resource_path(f"{RES}/shenka_filter_theme_btn.png"), threshold=0.8)
        # self.filter_theme_item = Template(
        #     self.resource_path(f"{RES}/shenka_filter_theme_item.png"), threshold=0.8)

        # 年费筛选入口
        # self.filter_fee_btn = Template(
        #     self.resource_path(f"{RES}/shenka_filter_fee_btn.png"), threshold=0.8)
        # self.filter_fee_item = Template(
        #     self.resource_path(f"{RES}/shenka_filter_fee_item.png"), threshold=0.8)

        # 更多筛选
        # self.filter_more_btn = Template(
        #     self.resource_path(f"{RES}/shenka_filter_more_btn.png"), threshold=0.8)
        # self.filter_more_panel = Template(
        #     self.resource_path(f"{RES}/shenka_filter_more_panel.png"), threshold=0.7)
        # self.filter_tag_item = Template(
        #     self.resource_path(f"{RES}/shenka_filter_tag_item.png"), threshold=0.8)

        # 重置按钮
        # self.filter_reset_btn = Template(
        #     self.resource_path(f"{RES}/shenka_filter_reset_btn.png"), threshold=0.8)

        # 筛选结果变化标志（用于验证筛选生效）
        # self.filter_result_indicator = Template(
        #     self.resource_path(f"{RES}/shenka_filter_result.png"), threshold=0.7)

        # 特色服务Tag（如精选、免年费等）
        # self.special_tag = Template(
        #     self.resource_path(f"{RES}/shenka_filter_special_tag.png"), threshold=0.8)

    # ---- 页面验证 ----
    @allure.step("判断是否在所有卡片的筛选页面")
    def is_filter_all_card_page_displayed(self) -> bool:
        """
        判断是否在"所有卡片"的筛选页面
        """
        return self.is_exists(self.filter_all_card_page_indicator) and self.is_exists(self.filter_all_card_page_indicator2)

    @allure.step("判断筛选结果是否已刷新")
    def is_filter_result_refreshed(self) -> bool:
        """
        判断筛选操作后卡片列表是否已刷新
        TODO_IMG: 需补充筛选结果刷新标志截图 shenka_filter_result.png
        """
        raise NotImplementedError("TODO_IMG: 需补充筛选结果刷新标志截图 shenka_filter_result.png")

    @allure.step("判断更多筛选浮窗是否已弹出")
    def is_more_filter_panel_displayed(self) -> bool:
        """
        TODO_IMG: 需补充更多筛选浮窗标志截图 shenka_filter_more_panel.png
        """
        raise NotImplementedError("TODO_IMG: 需补充更多筛选浮窗标志截图 shenka_filter_more_panel.png")

    @allure.step("判断筛选选项是否已被重置")
    def is_filter_reset(self) -> bool:
        """
        点击重置后，所有已选筛选项应被清空
        TODO_IMG: 需补充重置后状态截图验证（与筛选结果刷新标志相同或单独截）
        """
        raise NotImplementedError("TODO_IMG: 需补充重置后状态标志截图")

    # ---- 页面操作 ----

    @allure.step("切换筛选条件（直接切换）")
    def switch_filter_condition(self):
        """
        直接切换查询条件（左右滑动筛选条件栏）
        已有图片：shenka_filter_swipe_area.png（滑动起点），可参考使用
        """
        log.info("切换筛选条件（滑动筛选栏）")
        # 使用已有图片作为滑动起点
        self.wait_for_element(self.filter_swipe_area)
        from airtest.core.api import swipe
        swipe(self.filter_swipe_area, vector=[-0.0059, -0.3885])

    @allure.step("选择银行筛选条件")
    def select_bank_filter(self):
        """
        切换全部银行的查询条件
        TODO_IMG: 需补充银行筛选入口截图 shenka_filter_bank_btn.png
        """
        log.info("选择银行筛选条件")
        raise NotImplementedError("TODO_IMG: 需补充银行筛选入口截图 shenka_filter_bank_btn.png")

    @allure.step("选择卡等级筛选条件")
    def select_level_filter(self):
        """
        TODO_IMG: 需补充卡等级筛选入口截图 shenka_filter_level_btn.png
        """
        log.info("选择卡等级筛选条件")
        raise NotImplementedError("TODO_IMG: 需补充卡等级筛选入口截图 shenka_filter_level_btn.png")

    @allure.step("选择卡主题筛选条件")
    def select_theme_filter(self):
        """
        TODO_IMG: 需补充卡主题筛选入口截图 shenka_filter_theme_btn.png
        """
        log.info("选择卡主题筛选条件")
        raise NotImplementedError("TODO_IMG: 需补充卡主题筛选入口截图 shenka_filter_theme_btn.png")

    @allure.step("选择年费筛选条件")
    def select_fee_filter(self):
        """
        TODO_IMG: 需补充年费筛选入口截图 shenka_filter_fee_btn.png
        """
        log.info("选择年费筛选条件")
        raise NotImplementedError("TODO_IMG: 需补充年费筛选入口截图 shenka_filter_fee_btn.png")

    @allure.step("点击更多筛选")
    def click_more_filter(self):
        """
        点击更多的查询条件入口，弹出更多筛选浮窗
        TODO_IMG: 需补充更多筛选按钮截图 shenka_filter_more_btn.png
        """
        log.info("点击更多筛选")
        raise NotImplementedError("TODO_IMG: 需补充更多筛选按钮截图 shenka_filter_more_btn.png")

    @allure.step("选择某标签/服务选项")
    def select_tag_item(self):
        """
        在更多筛选浮窗中选择某标签
        TODO_IMG: 需补充标签选项截图 shenka_filter_tag_item.png
        """
        log.info("选择标签选项")
        raise NotImplementedError("TODO_IMG: 需补充标签选项截图 shenka_filter_tag_item.png")

    @allure.step("点击重置按钮")
    def click_reset(self):
        """
        点击重置按钮，清除所有已选筛选条件
        TODO_IMG: 需补充重置按钮截图 shenka_filter_reset_btn.png
        """
        log.info("点击重置按钮")
        raise NotImplementedError("TODO_IMG: 需补充重置按钮截图 shenka_filter_reset_btn.png")

    @allure.step("点击特色服务Tag")
    def click_special_tag(self):
        """
        点击筛选组件下方的特色服务Tag（如精选、免年费等）
        TODO_IMG: 需补充特色服务Tag截图 shenka_filter_special_tag.png
        """
        log.info("点击特色服务Tag")
        raise NotImplementedError("TODO_IMG: 需补充特色服务Tag截图 shenka_filter_special_tag.png")
