# AirTestUI

基于 **pytest + Airtest/Poco** 的企业级 APP UI 自动化回归测试框架，支持 Android / iOS 双平台、多设备并发执行。

---

## 特性一览

| 特性 | 说明 |
|------|------|
| 双平台支持 | Android (ADB) + iOS (iOS-USB)，通过配置文件切换 |
| 多设备并发 | pytest-xdist 驱动，每个 worker 绑定独立设备 |
| POM 模式 | BasePage 封装，同时支持图像识别 (Template) 与 UI 树定位 (Poco) |
| 双报告体系 | Allure（截图 + 步骤 + 趋势）+ pytest-html（轻量备选） |
| 数据驱动 | YAML / Excel / JSON，一键对接 `@pytest.mark.parametrize` |
| 失败自动截图 | conftest.py hook 自动捕获，附加到 Allure 报告 |
| 重试机制 | `@retry` 装饰器 + pytest-rerunfailures，双重保障 |
| 通知推送 | 钉钉机器人 / 邮件，测试结束自动推送结果摘要 |
| 配置覆盖 | `local_config.yaml` + `AIRTESTUI_*` 环境变量，三级覆盖 |

---

## 目录结构

```
AirTestUI/
├── config/                     # 配置管理
│   ├── config.yaml             # 设备 / 环境 / APP 配置
│   └── settings.py             # 配置加载器
├── base/                       # 基础层
│   ├── driver_manager.py       # 设备驱动管理器（单例 / 设备池 / 并发分配）
│   ├── app_launcher.py         # APP 启停管理
│   └── base_page.py            # POM 基类（图像识别 + Poco 双模式）
├── pages/                      # 页面对象层
│   ├── android/                # Android 页面对象
│   └── ios/                    # iOS 页面对象
├── testcases/                  # 测试用例层
│   ├── android/                # Android 用例
│   └── ios/                    # iOS 用例
├── utils/                      # 工具层
│   ├── logger.py               # 日志（loguru / 控制台 + 文件 + 错误分离）
│   ├── screenshot.py           # 截图 + Allure 附件
│   ├── retry.py                # 重试装饰器
│   ├── data_loader.py          # 数据驱动加载器
│   └── notification.py         # 通知（钉钉 / 邮件）
├── data/                       # 测试数据（YAML / Excel / JSON）
├── resources/                  # 图像识别素材（截图模板）
├── logs/                       # 运行日志输出
├── reports/                    # 测试报告输出
├── conftest.py                 # 全局 fixture & hook
├── pytest.ini                  # pytest 运行配置
└── requirements.txt            # Python 依赖
```

---

## 快速开始

### 1. 环境准备

```bash
# Python >= 3.9
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 设备与 APP 配置

编辑 `config/config.yaml`，填写你的设备信息和 APP 包名：

```yaml
android:
  devices:
    - serial: "your_device_serial"    # adb devices 获取
      name: "pixel-6"
  app:
    package: "com.your.app"
    activity: ".MainActivity"

ios:
  devices:
    - uuid: "auto"                    # 自动检测连接的 iOS 设备
      name: "iPhone-14"
  app:
    bundle_id: "com.your.app"
```

### 3. 准备图像素材

将截图模板放到 `resources/android/` 或 `resources/ios/` 目录，供 `Template()` 引用。

### 4. 运行测试

```bash
# 运行全部测试
pytest

# 仅运行 Android 用例
pytest -m android

# 仅运行 iOS 用例
pytest -m ios

# 仅运行冒烟测试
pytest -m smoke

# 仅运行回归测试
pytest -m regression

# 按优先级筛选
pytest -m p0

# 单设备顺序执行（关闭并发）
pytest -n 0

# 指定并发数
pytest -n 2

# 不自动重试
pytest --reruns 0
```

### 5. 查看报告

```bash
# Allure 报告
allure serve allure-results

# pytest-html 报告
# 自动生成到 reports/report.html，浏览器直接打开即可
```

---

## 编写测试用例

### 页面对象

在 `pages/` 下创建页面对象，继承 `BasePage`：

```python
from base.base_page import BasePage
from airtest.core.api import Template

class ProfilePage(BasePage):
    def __init__(self, poco=None):
        super().__init__(poco=poco)
        self._img_avatar = Template(self.resource_path("android/img_avatar.png"))

    def is_profile_displayed(self) -> bool:
        if self._poco:
            return self.poco()("profile_view").exists()
        return self.is_exists(self._img_avatar)

    def get_nickname(self) -> str:
        return self.poco_get_text("nickname_label")
```

### 测试用例

在 `testcases/` 下编写测试类，使用框架提供的 fixture：

```python
import allure
import pytest
from pages.android.profile_page import ProfilePage

@allure.feature("个人中心")
@allure.story("Android")
@pytest.mark.android
@pytest.mark.regression
class TestProfile:

    @pytest.fixture(autouse=True)
    def setup(self, poco):
        self.profile = ProfilePage(poco=poco)

    @allure.title("查看个人资料")
    @pytest.mark.p0
    def test_view_profile(self):
        assert self.profile.is_profile_displayed()
        nickname = self.profile.get_nickname()
        assert nickname is not None
```

### 数据驱动

在 `data/` 下创建 YAML 数据文件，用 `parametrize_data` 加载：

```python
from utils.data_loader import parametrize_data

@pytest.mark.parametrize("case", parametrize_data("login_data.yaml", "login_cases"))
def test_login_ddt(case, poco):
    login_page = LoginPage(poco=poco)
    login_page.login(case["username"], case["password"])
    if case["expected_result"] == "success":
        assert HomePage(poco=poco).is_home_page_displayed()
    else:
        assert login_page.is_login_page_displayed()
```

---

## 可用 Fixture

框架通过 `conftest.py` 自动注入以下 fixture：

| Fixture | 作用域 | 说明 |
|---------|--------|------|
| `worker_id` | session | 当前 xdist worker 编号 |
| `device_info` | session | 分配给当前 worker 的设备信息 |
| `airtest_device` | session | Airtest 设备实例 |
| `platform` | session | 当前平台 (`android` / `ios`) |
| `poco` | session | Poco 实例（自动选择 Android / iOS 引擎） |
| `app_launcher` | session | APP 启停管理器 |
| `setup_app` | session | 自动启停 APP（autouse） |
| `test_data` | session | 测试数据加载函数 |

---

## 自定义标记

| 标记 | 说明 |
|------|------|
| `@pytest.mark.android` | Android 平台用例 |
| `@pytest.mark.ios` | iOS 平台用例 |
| `@pytest.mark.smoke` | 冒烟测试 |
| `@pytest.mark.regression` | 回归测试 |
| `@pytest.mark.p0` | 优先级 P0（阻塞级） |
| `@pytest.mark.p1` | 优先级 P1（关键级） |
| `@pytest.mark.p2` | 优先级 P2（一般级） |
| `@pytest.mark.skip_ci` | 跳过 CI 环境 |

---

## 配置覆盖机制

框架支持三级配置覆盖，优先级从高到低：

1. **环境变量**：`AIRTESTUI_<大写键名>`，如 `AIRTESTUI_ENV=production`
2. **本地配置**：`config/local_config.yaml`（已 gitignore，不纳入版本控制）
3. **主配置**：`config/config.yaml`

---

## 通知配置

在 `config/config.yaml` 中启用通知并填写相关凭据：

```yaml
notification:
  enabled: true
  type: dingtalk           # dingtalk / email
  dingtalk:
    webhook: "https://oapi.dingtalk.com/robot/send?access_token=xxx"
    secret: "SEC..."
  email:
    smtp_host: "smtp.example.com"
    smtp_port: 465
    sender: "test@example.com"
    password: "password"
    receivers:
      - "dev-team@example.com"
```

测试结束后将自动推送结果摘要（包含通过率、失败数等）。

---

## CI/CD 集成

以 GitHub Actions 为例：

```yaml
name: Regression Test
on:
  schedule:
    - cron: '0 2 * * *'    # 每天凌晨 2 点执行

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest -m regression --alluredir=allure-results
      - name: Generate Allure Report
        uses: simple-elf/allure-report-action@master
        if: always()
```

---

## 常见问题

**Q: 如何只连接一台设备执行？**

修改 `config/config.yaml` 只保留一台设备，运行时使用 `pytest -n 0` 关闭并发。

**Q: 图像识别和 Poco 如何选择？**

- 推荐优先使用 Poco UI 树定位（稳定、不依赖分辨率）
- 图像识别适合无法获取 UI 树的场景（如游戏、WebView 内嵌内容）
- 两者可以在同一个页面对象中混合使用

**Q: 如何调试单个用例？**

```bash
pytest testcases/android/test_login.py::TestAndroidLogin::test_login_success -v -s -n 0
```

**Q: 如何添加新的页面对象？**

1. 在 `pages/android/` 或 `pages/ios/` 下新建 `.py` 文件
2. 继承 `BasePage`，在 `__init__` 中定义元素
3. 封装页面操作和验证方法，使用 `@allure.step` 标注

---

## 技术栈

| 组件 | 版本要求 | 用途 |
|------|---------|------|
| Python | >= 3.9 | 运行环境 |
| pytest | >= 7.4 | 测试框架 |
| airtest | >= 1.3 | UI 自动化引擎 |
| pocoui | >= 1.0 | UI 树定位引擎 |
| pytest-xdist | >= 3.3 | 多设备并发 |
| allure-pytest | >= 2.13 | Allure 报告 |
| pytest-html | >= 4.0 | HTML 报告 |
| loguru | >= 0.7 | 日志 |
| PyYAML | >= 6.0 | 配置与数据 |
