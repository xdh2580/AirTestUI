"""
纯图像识别登录回归测试用例
示例: 仅使用 airtest Template 图像识别，不使用 Poco
适用于：游戏、WebView、无法获取 UI 树的场景
"""
import allure
import pytest

from pages.android.image_login_page import ImageLoginPage
from utils.logger import get_logger
from utils.data_loader import parametrize_data

log = get_logger("TestImageLogin")


@allure.feature("登录模块")
@allure.story("图像识别登录")
@pytest.mark.android
@pytest.mark.regression
class TestImageLogin:
    """
    纯图像识别登录回归测试

    与 TestAndroidLogin 的区别:
    - 不使用 poco fixture，页面对象不传入 poco 实例
    - 所有元素定位均通过 airtest Template 图像识别
    - 适用于无法获取 UI 树的场景（游戏、WebView 等）
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        """初始化纯图像识别页面对象（不传入 poco）"""
        self.login_page = ImageLoginPage()

    @allure.title("图像识别 - 正常登录流程")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.p0
    @pytest.mark.smoke
    def test_image_login_success(self):
        """验证纯图像识别模式下的正常登录流程"""
        # Step 1: 等待并验证登录页面已加载
        self.login_page.wait_login_page_loaded(timeout=10)
        self.login_page.assert_login_page_loaded()

        # Step 2: 输入账号密码并点击登录
        self.login_page.login("testuser", "testpass123")

        # Step 3: 验证登录成功 - 等待首页标志出现
        self.login_page.assert_login_success(timeout=20)

    @allure.title("图像识别 - 登录失败错误密码")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_image_login_wrong_password(self):
        """验证错误密码登录后出现错误提示弹窗"""
        # 确认登录页面已加载
        self.login_page.assert_login_page_loaded()

        # 执行登录
        self.login_page.login("testuser", "wrong_password")
        self.login_page.wait_seconds(2)  # 等待错误提示弹出

        # 验证错误提示弹窗出现
        self.login_page.assert_login_failed()

        # 验证仍在登录页面
        self.login_page.assert_still_on_login_page()

    @allure.title("图像识别 - 勾选记住密码登录")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_image_login_with_remember(self):
        """验证勾选记住密码后的登录流程"""
        self.login_page.wait_login_page_loaded()
        self.login_page.login("testuser", "testpass123", remember=True)
        self.login_page.assert_login_success()

    @allure.title("图像识别 - 登录页面元素完整性")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p2
    def test_image_login_page_elements(self):
        """验证登录页面所有关键图像元素均可见"""
        # 等待页面加载
        self.login_page.wait_login_page_loaded()

        #逐个验证页面关键图像元素
        assert self.login_page.is_exists(
            self.login_page.img_logo
        ), "登录页 Logo 应可见"

        assert self.login_page.is_exists(
            self.login_page.img_username_field
        ), "用户名输入框应可见"

        assert self.login_page.is_exists(
            self.login_page.img_password_field
        ), "密码输入框应可见"

        assert self.login_page.is_exists(
            self.login_page.img_login_button
        ), "登录按钮应可见"

        # 截图记录当前页面状态
        self.login_page.take_page_screenshot("login_page_elements_check")

    @allure.title("图像识别 - 清空输入框后重新输入")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p2
    def test_image_clear_and_reinput(self):
        """验证清空输入框后可以重新输入内容"""
        self.login_page.wait_login_page_loaded()

        # 先输入一段文本
        self.login_page.input_username("wrong_user")

        # 清空输入框
        self.login_page.clear_input_field(char_count=10)

        # 重新输入正确的用户名
        self.login_page.input_username("testuser")
        self.login_page.input_password("testpass123")
        self.login_page.click_login()

        # 验证登录成功
        self.login_page.assert_login_success()


@allure.feature("登录模块")
@allure.story("图像识别 - 数据驱动")
@pytest.mark.android
@pytest.mark.regression
class TestImageLoginDDT:
    """
    数据驱动的纯图像识别登录测试

    演示如何将 YAML 测试数据与纯图像识别页面对象结合
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        self.login_page = ImageLoginPage()

    @allure.title("图像识别数据驱动 - {case[case_name]}")
    @pytest.mark.parametrize(
        "case",
        parametrize_data("test_data.yaml", "login_cases"),
    )
    def test_image_login_ddt(self, case):
        """数据驱动登录测试"""
        self.login_page.wait_login_page_loaded()

        self.login_page.login(case["username"], case["password"])

        if case["expected_result"] == "success":
            self.login_page.assert_login_success()
        else:
            self.login_page.wait_seconds(2)
            self.login_page.assert_still_on_login_page()