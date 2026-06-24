"""
我的申卡页面对象 - 纯图像识别
对应模块: 我的申卡 (SKHG-MINE-01 ~ MINE-15)
"""
import allure
from airtest.core.api import Template

from base.base_page import BasePage
from utils.logger import get_logger

log = get_logger("ShenkaMinePage")

RES = "common/shenka"


class ShenkaMinePage(BasePage):
    """我的申卡页面对象（纯图像识别）"""

    def __init__(self):
        super().__init__(poco=None)

        # ---------- 已有图片资源 ----------
        # 我的申卡Tab按钮（等待出现）
        self.mine_tab_indicator = Template(
            self.resource_path(f"{RES}/shenka_mine_tab_indicator.png"),
            record_pos=(-0.133, -0.387), resolution=(1216, 2640), threshold=0.8,
        )
        # 我的申卡Tab（点击）
        self.mine_tab_btn = Template(
            self.resource_path(f"{RES}/shenka_mine_tab_btn.png"),
            record_pos=(-0.444, -0.387), resolution=(1216, 2640), threshold=0.8,
        )
        # 我的申卡页面加载标志
        self.mine_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_mine_page_indicator.png"),
            record_pos=(0.137, 0.93), resolution=(1216, 2640), threshold=0.8,
        )
        # 奖励明细入口
        self.btn_reward = Template(
            self.resource_path(f"{RES}/shenka_mine_btn_reward.png"),
            record_pos=(0.135, 0.935), resolution=(1216, 2640), threshold=0.8,
        )
        # 在线激活入口
        self.btn_activate = Template(
            self.resource_path(f"{RES}/shenka_mine_btn_activate.png"),
            record_pos=(-0.003, 0.919), resolution=(1216, 2640), threshold=0.8,
        )
        # 收藏关注入口
        self.btn_collect_follow = Template(
            self.resource_path(f"{RES}/shenka_mine_btn_collect_follow.png"),
            record_pos=(-0.441, 0.172), resolution=(1216, 2640), threshold=0.8,
        )
        # 企微助手入口
        self.btn_wecom = Template(
            self.resource_path(f"{RES}/shenka_mine_btn_wecom.png"),
            record_pos=(-0.437, -0.896), resolution=(1216, 2640), threshold=0.8,
        )
        # 一键申卡入口（我的申卡页）
        self.btn_onekey_apply = Template(
            self.resource_path(f"{RES}/shenka_mine_btn_onekey_apply.png"),
            record_pos=(0.08, 0.061), resolution=(1216, 2640), threshold=0.8,
        )
        # 一键申卡授权声明页面标志
        self.onekey_auth_page = Template(
            self.resource_path(f"{RES}/shenka_mine_onekey_auth_page.png"),
            record_pos=(0.071, 0.061), resolution=(1216, 2640), threshold=0.8,
        )
        # 立即体验/授权同意按钮
        self.btn_onekey_start = Template(
            self.resource_path(f"{RES}/shenka_mine_btn_onekey_start.png"),
            record_pos=(0.053, -0.768), resolution=(1216, 2640), threshold=0.8,
        )
        # 卡片PK入口
        self.btn_card_pk = Template(
            self.resource_path(f"{RES}/shenka_mine_btn_card_pk.png"),
            record_pos=(0.422, -0.748), resolution=(1216, 2640), threshold=0.8,
        )
        # 个人资料入口
        self.btn_profile = Template(
            self.resource_path(f"{RES}/shenka_mine_btn_profile.png"),
            record_pos=(0.424, -0.744), resolution=(1216, 2640), threshold=0.8,
        )
        # 一键申卡生成推荐按钮
        self.btn_generate_recommend = Template(
            self.resource_path(f"{RES}/shenka_mine_btn_generate_recommend.png"),
            record_pos=(0.184, 0.903), resolution=(1216, 2640), threshold=0.8,
        )
        # 一键申卡推荐结果页标志
        self.onekey_result_page = Template(
            self.resource_path(f"{RES}/shenka_mine_onekey_result_page.png"),
            record_pos=(0.179, 0.906), resolution=(1216, 2640), threshold=0.8,
        )

        # ---------- 待补充图片资源（TODO_IMG）----------
        # 我的申卡Tab（首页底部导航Tab）
        # self.mine_nav_tab = Template(
        #     self.resource_path(f"{RES}/shenka_mine_tab.png"), threshold=0.8)

        # 奖励明细页面标志
        # self.reward_page_indicator = Template(
        #     self.resource_path(f"{RES}/shenka_mine_reward_page.png"), threshold=0.8)

        # 激活页面标志
        # self.activate_page_indicator = Template(
        #     self.resource_path(f"{RES}/shenka_mine_activate_page.png"), threshold=0.8)

        # 收藏关注页面标志
        self.collect_page_indicator = Template(
            self.resource_path(f"{RES}/shenka_mine_collect_page_indicator.png"), threshold=0.8)

        # 已收藏卡片条目（用于左滑操作）
        # self.collect_item = Template(
        #     self.resource_path(f"{RES}/shenka_mine_collect_item.png"), threshold=0.8)

        # 左滑后取消收藏按钮
        # self.cancel_collect_btn = Template(
        #     self.resource_path(f"{RES}/shenka_mine_cancel_collect_btn.png"), threshold=0.8)

        # 收藏页右上角PK按钮
        # self.collect_pk_btn = Template(
        #     self.resource_path(f"{RES}/shenka_mine_collect_pk_btn.png"), threshold=0.8)

        # 企微助手二维码页面
        # self.wecom_page_indicator = Template(
        #     self.resource_path(f"{RES}/shenka_mine_wecom_page.png"), threshold=0.8)

        # 一键申卡主页面标志
        # self.onekey_page_indicator = Template(
        #     self.resource_path(f"{RES}/shenka_mine_onekey_page.png"), threshold=0.8)

        # 推荐结果页立即申请按钮
        # self.onekey_apply_btn = Template(
        #     self.resource_path(f"{RES}/shenka_mine_onekey_apply_btn.png"), threshold=0.8)

        # 卡片PK页面标志
        # self.pk_page_indicator = Template(
        #     self.resource_path(f"{RES}/shenka_mine_pk_page.png"), threshold=0.8)

        # 个人资料页面标志
        # self.profile_page_indicator = Template(
        #     self.resource_path(f"{RES}/shenka_mine_profile_page.png"), threshold=0.8)

        # 完善信息按钮
        # self.btn_edit_profile = Template(
        #     self.resource_path(f"{RES}/shenka_mine_profile_edit_btn.png"), threshold=0.8)

        # 个人资料完善填写页面标志
        # self.profile_edit_page = Template(
        #     self.resource_path(f"{RES}/shenka_mine_profile_edit_page.png"), threshold=0.8)

        # 保存按钮
        # self.btn_save_profile = Template(
        #     self.resource_path(f"{RES}/shenka_mine_profile_save_btn.png"), threshold=0.8)

        # 保存成功标志
        # self.profile_saved_indicator = Template(
        #     self.resource_path(f"{RES}/shenka_mine_profile_saved.png"), threshold=0.7)

        # 快速申卡区域某卡片
        # self.quick_card_item = Template(
        #     self.resource_path(f"{RES}/shenka_mine_quick_card_item.png"), threshold=0.8)

    # ---- 页面验证 ----
    @allure.step("判断我的收藏页是否已跳转")
    def is_my_collect_page_displayed(self) -> bool:
        return self.is_exists(self.collect_page_indicator)

    @allure.step("等待我的申卡页加载")
    def wait_mine_page_loaded(self, timeout=15):
        """等待我的申卡页面加载完成"""
        log.info("等待我的申卡页加载")
        return self.wait_for_element(self.mine_page_indicator, timeout=timeout)

    @allure.step("判断我的申卡页是否已加载")
    def is_mine_page_loaded(self) -> bool:
        return self.is_exists(self.mine_page_indicator)

    @allure.step("判断奖励明细页是否已跳转")
    def is_reward_page_displayed(self) -> bool:
        """TODO_IMG: 需补充奖励明细页面标志截图 shenka_mine_reward_page.png"""
        raise NotImplementedError("TODO_IMG: 需补充奖励明细页面标志截图 shenka_mine_reward_page.png")

    @allure.step("判断激活页是否已跳转")
    def is_activate_page_displayed(self) -> bool:
        """TODO_IMG: 需补充激活页面标志截图 shenka_mine_activate_page.png"""
        raise NotImplementedError("TODO_IMG: 需补充激活页面标志截图 shenka_mine_activate_page.png")

    @allure.step("判断收藏关注页是否已跳转")
    def is_collect_page_displayed(self) -> bool:
        """TODO_IMG: 需补充收藏关注页面标志截图 shenka_mine_collect_page.png"""
        raise NotImplementedError("TODO_IMG: 需补充收藏关注页面标志截图 shenka_mine_collect_page.png")

    @allure.step("判断收藏关注页取消收藏是否成功")
    def is_collect_item_removed(self) -> bool:
        """TODO_IMG: 需补充收藏取消后空状态截图 shenka_mine_collect_empty.png"""
        raise NotImplementedError("TODO_IMG: 需补充收藏取消后空状态截图 shenka_mine_collect_empty.png")

    @allure.step("判断企微助手页是否已跳转")
    def is_wecom_page_displayed(self) -> bool:
        """TODO_IMG: 需补充企微助手页面标志截图 shenka_mine_wecom_page.png"""
        raise NotImplementedError("TODO_IMG: 需补充企微助手页面标志截图 shenka_mine_wecom_page.png")

    @allure.step("判断一键申卡页面是否已加载")
    def is_onekey_page_loaded(self) -> bool:
        """通过授权声明页标志判断"""
        return self.is_exists(self.onekey_auth_page)

    @allure.step("判断一键申卡推荐结果是否生成")
    def is_onekey_result_generated(self) -> bool:
        return self.is_exists(self.onekey_result_page)

    @allure.step("判断卡片PK页是否已跳转")
    def is_pk_page_displayed(self) -> bool:
        """TODO_IMG: 需补充卡片PK页面标志截图 shenka_mine_pk_page.png"""
        raise NotImplementedError("TODO_IMG: 需补充卡片PK页面标志截图 shenka_mine_pk_page.png")

    @allure.step("判断个人资料页是否已跳转")
    def is_profile_page_displayed(self) -> bool:
        """TODO_IMG: 需补充个人资料页面标志截图 shenka_mine_profile_page.png"""
        raise NotImplementedError("TODO_IMG: 需补充个人资料页面标志截图 shenka_mine_profile_page.png")

    @allure.step("判断个人资料完善页是否已跳转")
    def is_profile_edit_page_displayed(self) -> bool:
        """TODO_IMG: 需补充个人资料完善填写页面标志截图 shenka_mine_profile_edit_page.png"""
        raise NotImplementedError("TODO_IMG: 需补充个人资料完善填写页面标志截图 shenka_mine_profile_edit_page.png")

    @allure.step("判断个人资料是否已保存成功")
    def is_profile_saved(self) -> bool:
        """TODO_IMG: 需补充保存成功标志截图 shenka_mine_profile_saved.png"""
        raise NotImplementedError("TODO_IMG: 需补充保存成功标志截图 shenka_mine_profile_saved.png")

    # ---- 页面操作 ----

    @allure.step("点击我的申卡Tab")
    def click_mine_tab(self):
        """点击底部导航我的申卡Tab，切换到我的申卡页"""
        log.info("点击我的申卡Tab")
        self.wait_for_element(self.mine_tab_indicator)
        self.click(self.mine_tab_btn)

    @allure.step("点击奖励明细")
    def click_reward(self):
        """点击我的申卡页奖励明细入口"""
        log.info("点击奖励明细")
        self.wait_for_element(self.mine_page_indicator)
        self.click(self.btn_reward)

    @allure.step("点击在线激活")
    def click_activate(self):
        """点击我的申卡页在线激活入口"""
        log.info("点击在线激活")
        self.click(self.btn_activate)

    @allure.step("点击收藏关注")
    def click_collect_follow(self):
        """点击我的申卡页收藏关注入口"""
        log.info("点击收藏关注")
        self.click(self.btn_collect_follow)

    @allure.step("左滑已收藏卡片并点击取消收藏")
    def swipe_and_cancel_collect(self):
        """
        左滑已收藏的卡片，然后点击出现的取消收藏按钮
        TODO_IMG: 需补充收藏卡片条目截图 shenka_mine_collect_item.png
                  左滑后取消收藏按钮截图 shenka_mine_cancel_collect_btn.png
        """
        log.info("左滑取消收藏")
        raise NotImplementedError(
            "TODO_IMG: 需补充 shenka_mine_collect_item.png 和 shenka_mine_cancel_collect_btn.png"
        )

    @allure.step("在收藏页点击PK按钮")
    def click_collect_pk_btn(self):
        """
        点击收藏关注页右上角卡片PK按钮
        TODO_IMG: 需补充收藏页PK按钮截图 shenka_mine_collect_pk_btn.png
        """
        log.info("点击收藏页PK按钮")
        raise NotImplementedError("TODO_IMG: 需补充收藏页PK按钮截图 shenka_mine_collect_pk_btn.png")

    @allure.step("点击企微助手")
    def click_wecom(self):
        """点击我的申卡页企微助手入口"""
        log.info("点击企微助手")
        self.click(self.btn_wecom)

    @allure.step("点击一键申卡")
    def click_onekey_apply(self):
        """点击我的申卡页一键申卡入口"""
        log.info("点击一键申卡")
        self.click(self.btn_onekey_apply)

    @allure.step("点击立即体验（授权同意声明）")
    def click_onekey_start(self):
        """点击一键申卡授权声明页的立即体验/同意按钮"""
        log.info("点击立即体验")
        self.wait_for_element(self.onekey_auth_page)
        self.click(self.btn_onekey_start)

    @allure.step("点击生成推荐")
    def click_generate_recommend(self):
        """按提示选项后点击生成推荐"""
        log.info("点击生成推荐")
        self.click(self.btn_generate_recommend)

    @allure.step("点击推荐结果中的立即申请")
    def click_onekey_apply_card(self):
        """
        点击一键申卡推荐结果中的立即申请
        TODO_IMG: 需补充推荐结果立即申请按钮截图 shenka_mine_onekey_apply_btn.png
        """
        log.info("点击推荐结果立即申请")
        raise NotImplementedError("TODO_IMG: 需补充推荐结果立即申请按钮截图 shenka_mine_onekey_apply_btn.png")

    @allure.step("点击卡片PK")
    def click_card_pk(self):
        """点击我的申卡页卡片PK入口"""
        log.info("点击卡片PK")
        self.click(self.btn_card_pk)

    @allure.step("点击个人资料")
    def click_profile(self):
        """点击我的申卡页个人资料入口"""
        log.info("点击个人资料")
        self.click(self.btn_profile)

    @allure.step("点击完善信息按钮")
    def click_edit_profile(self):
        """
        点击个人资料页上方完善信息按钮
        TODO_IMG: 需补充完善信息按钮截图 shenka_mine_profile_edit_btn.png
        """
        log.info("点击完善信息")
        raise NotImplementedError("TODO_IMG: 需补充完善信息按钮截图 shenka_mine_profile_edit_btn.png")

    @allure.step("完善个人信息并保存")
    def fill_and_save_profile(self):
        """
        在个人资料完善页面填写各类信息并保存
        TODO_IMG: 需补充保存按钮截图 shenka_mine_profile_save_btn.png
        注意：各信息字段需根据实际页面结构单独截图和配置
        """
        log.info("完善并保存个人资料")
        raise NotImplementedError("TODO_IMG: 需补充保存按钮截图 shenka_mine_profile_save_btn.png")

    @allure.step("点击完善页底部一键申卡按钮")
    def click_profile_onekey_apply(self):
        """
        点击个人资料完善填写页底部一键申卡按钮
        TODO_IMG: 复用 shenka_mine_onekey_page.png 验证；按钮截图需额外补充
        """
        log.info("点击完善页一键申卡")
        raise NotImplementedError("TODO_IMG: 需补充完善页一键申卡按钮截图")

    @allure.step("点击快速申卡区域的某张卡片")
    def click_quick_card(self):
        """
        点击个人资料页下方快速申卡区域的任意卡片
        TODO_IMG: 需补充快速申卡区域卡片截图 shenka_mine_quick_card_item.png
        """
        log.info("点击快速申卡区域卡片")
        raise NotImplementedError("TODO_IMG: 需补充快速申卡区域卡片截图 shenka_mine_quick_card_item.png")
