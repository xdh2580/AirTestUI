"""
纯图像识别登录回归测试用例
示例: 仅使用 airtest Template 图像识别，不使用 Poco
适用于：游戏、WebView、无法获取 UI 树的场景
"""
import allure
import pytest

from pages.common.image_home_page import ImageHomePage
from utils.logger import get_logger
from utils.data_loader import parametrize_data

log = get_logger("TestImageLogin")


@allure.feature("登录模块")
@allure.story("图像识别登录")
@pytest.mark.common
@pytest.mark.regression
class TestImageHome:
    """
    纯图像识别home页面回归测试

    与 TestAndroidLogin 的区别:
    - 不使用 poco fixture，页面对象不传入 poco 实例
    - 所有元素定位均通过 airtest Template 图像识别
    - 适用于无法获取 UI 树的场景（游戏、WebView 等）
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        """初始化纯图像识别页面对象（不传入 poco）"""
        self.home_page = ImageHomePage()

    @allure.title("图像识别 - home页面加载")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.p0
    @pytest.mark.smoke
    def test_image_home_success(self):
        """验证纯图像识别模式下的home页面加载"""
        # Step 1: 等待并验证home页面已加载
        self.home_page.wait_home_page_loaded(timeout=10)
        self.home_page.assert_home_page_loaded()


    