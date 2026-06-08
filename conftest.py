"""
pytest 全局 conftest.py
定义 fixture、hook 和多设备并发机制
"""
import os
import time
import traceback

import pytest
import allure

from airtest.core.api import init_device, connect_device, set_current, device as get_current_device

from config.settings import settings, get_env, ROOT_DIR
from base.driver_manager import driver_manager, DeviceInfo
from base.app_launcher import AppLauncher
from utils.logger import get_logger
from utils.screenshot import take_screenshot, attach_screenshot_to_allure
from utils.notification import send_notification, build_report_message

log = get_logger("Conftest")

# 全局测试结果统计
_test_results = {
    "total": 0,
    "passed": 0,
    "failed": 0,
    "skipped": 0,
    "errors": 0,
    "start_time": None,
    "end_time": None,
}


# ==================== Hook 函数 ====================

def pytest_configure(config):
    """pytest 初始化配置"""
    _test_results["start_time"] = time.time()

    # 设置 Allure 环境信息
    allure_dir = config.getoption("--alluredir", default=None)
    if allure_dir:
        env_file = os.path.join(allure_dir, "environment.properties")
        os.makedirs(allure_dir, exist_ok=True)
        with open(env_file, "w", encoding="utf-8") as f:
            f.write(f"Environment={get_env()}\n")
            f.write(f"Platform=Android+iOS\n")
            f.write(f"Framework=AirTestUI\n")


def pytest_collection_modifyitems(items):
    """收集用例后，标记平台信息"""
    for item in items:
        # 根据 testcases 目录自动标记平台
        if "android" in str(item.fspath):
            item.add_marker(pytest.mark.android)
        elif "ios" in str(item.fspath):
            item.add_marker(pytest.mark.ios)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    测试执行结果钩子
    - 失败时自动截图
    - 记录 Allure 步骤
    - 统计测试结果
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        _test_results["total"] += 1

        if report.passed:
            _test_results["passed"] += 1
        elif report.failed:
            _test_results["failed"] += 1
            # 失败自动截图
            _attach_failure_screenshot(item, report)
        elif report.skipped:
            _test_results["skipped"] += 1

    elif report.when == "setup" and report.failed:
        _test_results["errors"] += 1


def pytest_sessionfinish(session, exitstatus):
    """测试会话结束"""
    _test_results["end_time"] = time.time()
    duration = _test_results["end_time"] - _test_results["start_time"]

    summary = {
        "total": _test_results["total"],
        "passed": _test_results["passed"],
        "failed": _test_results["failed"],
        "skipped": _test_results["skipped"],
        "duration": f"{duration:.1f}s",
        "env": get_env(),
    }

    log.info(
        f"测试完成: 总计 {summary['total']}, "
        f"通过 {summary['passed']}, "
        f"失败 {summary['failed']}, "
        f"跳过 {summary['skipped']}, "
        f"耗时 {summary['duration']}"
    )

    # 发送通知
    try:
        title, content = build_report_message(summary)
        send_notification(title, content)
    except Exception as e:
        log.error(f"发送通知失败: {e}")


def _attach_failure_screenshot(item, report):
    """失败用例自动截图并附加到 Allure"""
    try:
        filepath = take_screenshot(f"fail_{item.nodeid.replace('::', '_')}")
        if filepath:
            attach_screenshot_to_allure(
                name=f"失败截图 - {item.name}",
                filepath=filepath,
            )
    except Exception as e:
        log.warning(f"失败截图捕获异常: {e}")

    # 附加失败日志到 Allure
    if report.longrepr:
        allure.attach(
            str(report.longrepr),
            name="失败详情",
            attachment_type=allure.attachment_type.TEXT,
        )


# ==================== Fixture ====================

def _get_worker_id() -> int:
    """获取当前 worker ID（用于多设备并发）"""
    worker = os.environ.get("PYTEST_XDIST_WORKER", "master")
    if worker == "master":
        return 0
    # gw0 -> 0, gw1 -> 1, ...
    return int(worker.replace("gw", ""))


@pytest.fixture(scope="session")
def worker_id():
    """当前 worker ID fixture"""
    return _get_worker_id()


@pytest.fixture(scope="session")
def device_info(worker_id):
    """
    设备信息 fixture
    根据 worker_id 从设备池中分配设备
    """
    device = driver_manager.allocate_device(worker_id)
    yield device
    driver_manager.release_device(worker_id)


@pytest.fixture(scope="session")
def airtest_device(device_info):
    """
    Airtest 设备实例 fixture
    """
    from airtest.core.api import set_current
    if device_info.device:
        set_current(device_info.device)
    return device_info.device


@pytest.fixture(scope="session")
def platform(device_info):
    """当前平台 fixture"""
    return device_info.platform


@pytest.fixture(scope="session")
def poco(airtest_device, platform):
    """
    Poco 实例 fixture
    根据平台自动选择 Poco 引擎
    """
    try:
        if platform == "android":
            from poco.drivers.android.uiautomation import AndroidUiautomationPoco
            poco_instance = AndroidUiautomationPoco(
                device=airtest_device,
                use_airtest_input=True,
                screenshot_each_action=False,
            )
        else:
            from poco.drivers.ios import IOSPoco
            poco_instance = IOSPoco(device=airtest_device)

        log.info(f"Poco 初始化成功: {platform}")
        return poco_instance
    except Exception as e:
        log.warning(f"Poco 初始化失败: {e}，将仅使用图像识别模式")
        return None


@pytest.fixture(scope="session")
def app_launcher(platform):
    """APP 启停管理 fixture"""
    launcher = AppLauncher(platform=platform)
    return launcher


@pytest.fixture(scope="session", autouse=True)
def setup_app(app_launcher, device_info):
    """
    自动 APP 启停 fixture
    测试会话开始前启动 APP，结束后关闭
    """
    log.info(f"===== 测试会话开始 [{device_info.name}] =====")
    app_launcher.launch()
    yield
    app_launcher.close()
    log.info(f"===== 测试会话结束 [{device_info.name}] =====")


@pytest.fixture(autouse=True)
def step_allure(request):
    """每个测试用例自动记录为 Allure 步骤"""
    test_name = request.node.name
    with allure.step(f"执行测试: {test_name}"):
        yield


@pytest.fixture(scope="session")
def test_data():
    """
    测试数据加载 fixture

    用法:
        def test_something(test_data):
            data = test_data("test_data.yaml")
    """
    from utils.data_loader import load_yaml, parametrize_data

    def _load(filepath, key=None):
        if key:
            return parametrize_data(filepath, key)
        return load_yaml(filepath)

    return _load
