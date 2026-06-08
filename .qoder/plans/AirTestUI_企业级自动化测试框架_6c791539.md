# AirTestUI 企业级自动化测试框架

## 框架目录结构

```
AirTestUI/
├── config/                     # 配置管理
│   ├── __init__.py
│   ├── settings.py             # 全局配置加载
│   ├── config.yaml             # YAML 配置文件（设备/环境/APP信息）
│   └── conftest_generator.py   # 动态生成多设备 pytest fixture
├── base/                       # 基础层
│   ├── __init__.py
│   ├── base_page.py            # Page Object 基类（封装 airtest 核心操作）
│   ├── driver_manager.py       # 设备驱动管理器（连接/断开/设备池）
│   └── app_launcher.py         # APP 启动/重启/关闭管理
├── pages/                      # 页面对象层（POM模式）
│   ├── __init__.py
│   ├── android/                # Android 页面对象
│   │   └── __init__.py
│   └── ios/                    # iOS 页面对象
│       └── __init__.py
├── testcases/                  # 测试用例层
│   ├── __init__.py
│   ├── android/                # Android 测试用例
│   └── ios/                    # iOS 测试用例
├── utils/                      # 工具层
│   ├── __init__.py
│   ├── logger.py               # 日志模块
│   ├── screenshot.py           # 截图工具
│   ├── retry.py                # 重试装饰器
│   ├── data_loader.py          # 数据驱动加载器
│   └── notification.py         # 通知模块（钉钉/邮件）
├── data/                       # 测试数据
│   └── test_data.yaml
├── conftest.py                 # pytest 全局 fixture & hook
├── pytest.ini                  # pytest 配置
├── requirements.txt            # 依赖管理
├── .gitignore
├── logs/                       # 日志输出
└── reports/                    # 报告输出
```

## 核心设计

### 1. 配置管理 (config/)
- **config.yaml**: 集中管理设备列表、APP包名/路径、环境URL等
- **settings.py**: 读取yaml并暴露为全局配置对象，支持环境变量覆盖

### 2. 设备驱动管理 (base/driver_manager.py)
- 维护设备连接池，支持 Android(ADB) 和 iOS(iOS-USB) 两种连接方式
- 提供 `get_device()` / `release_device()` 接口
- 集成 pytest-xdist 实现多设备并发，每个 worker 绑定一台设备

### 3. Page Object 基类 (base/base_page.py)
- 封装 airtest 的 touch/swipe/wait/exists/assert_exists 等核心操作
- 内置智能等待、自动截图、操作日志记录
- 支持图像识别 + UI树定位双模式

### 4. 并发执行机制
- conftest.py 中根据 config.yaml 的设备列表动态生成 fixture
- pytest-xdist 的 `--dist=loadfile` 按文件分发用例
- 每个 worker 通过 workerid 确定绑定的设备

### 5. 报告体系
- Allure: 失败自动截图、步骤记录、环境信息
- pytest-html: 轻量备选
- conftest.py hook 实现自动附件

### 6. 数据驱动
- YAML/Excel 数据文件 + pytest.mark.parametrize
- data_loader 统一加载接口

## 实施任务清单

1. 创建项目目录结构和 .gitignore
2. 编写 requirements.txt
3. 编写 config/config.yaml 和 config/settings.py
4. 编写 base/driver_manager.py（设备驱动管理）
5. 编写 base/app_launcher.py（APP启停管理）
6. 编写 base/base_page.py（POM基类）
7. 编写 utils/logger.py（日志模块）
8. 编写 utils/screenshot.py（截图工具）
9. 编写 utils/retry.py（重试装饰器）
10. 编写 utils/data_loader.py（数据驱动加载）
11. 编写 utils/notification.py（通知模块）
12. 编写 conftest.py（全局fixture和hook）
13. 编写 pytest.ini
14. 编写示例页面对象 pages/android/ 和 pages/ios/
15. 编写示例测试用例 testcases/android/ 和 testcases/ios/
16. 编写示例测试数据 data/test_data.yaml