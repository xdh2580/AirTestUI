"""
通知模块
支持钉钉机器人 / 邮件 两种通知方式，用于测试结果推送
"""
import hmac
import hashlib
import base64
import urllib.parse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

import requests

from config.settings import settings
from utils.logger import get_logger

log = get_logger("Notification")


def send_notification(title: str, content: str):
    """
    发送通知（根据配置自动选择通知方式）

    Args:
        title: 通知标题
        content: 通知内容（支持 Markdown）
    """
    notification_config = settings.get("notification", None)
    if not notification_config:
        log.warning("通知未配置，跳过发送")
        return

    enabled = notification_config.get("enabled", False) if hasattr(notification_config, "enabled") else False
    if not enabled:
        log.debug("通知功能未启用，跳过发送")
        return

    notify_type = notification_config.get("type", "dingtalk") if hasattr(notification_config, "type") else "dingtalk"

    if notify_type == "dingtalk":
        _send_dingtalk(title, content)
    elif notify_type == "email":
        _send_email(title, content)
    else:
        log.warning(f"不支持的通知类型: {notify_type}")


def _send_dingtalk(title: str, content: str):
    """发送钉钉机器人通知"""
    dingtalk = settings.notification.dingtalk if hasattr(settings, "notification") else None
    if not dingtalk:
        log.error("钉钉配置缺失")
        return

    webhook = dingtalk.get("webhook", "") if hasattr(dingtalk, "webhook") else ""
    secret = dingtalk.get("secret", "") if hasattr(dingtalk, "secret") else ""

    if not webhook:
        log.error("钉钉 Webhook 未配置")
        return

    # 签名计算
    url = webhook
    if secret:
        timestamp = str(round(datetime.now().timestamp() * 1000))
        string_to_sign = f"{timestamp}\n{secret}"
        hmac_code = hmac.new(
            secret.encode("utf-8"),
            string_to_sign.encode("utf-8"),
            digestmod=hashlib.sha256,
        ).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = f"{webhook}&timestamp={timestamp}&sign={sign}"

    payload = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": content,
        },
    }

    try:
        resp = requests.post(url, json=payload, timeout=10)
        result = resp.json()
        if result.get("errcode") == 0:
            log.info("钉钉通知发送成功")
        else:
            log.error(f"钉钉通知发送失败: {result}")
    except Exception as e:
        log.error(f"钉钉通知发送异常: {e}")


def _send_email(title: str, content: str):
    """发送邮件通知"""
    email_cfg = settings.notification.email if hasattr(settings, "notification") else None
    if not email_cfg:
        log.error("邮件配置缺失")
        return

    smtp_host = email_cfg.get("smtp_host", "") if hasattr(email_cfg, "smtp_host") else ""
    smtp_port = email_cfg.get("smtp_port", 465) if hasattr(email_cfg, "smtp_port") else 465
    sender = email_cfg.get("sender", "") if hasattr(email_cfg, "sender") else ""
    password = email_cfg.get("password", "") if hasattr(email_cfg, "password") else ""
    receivers = email_cfg.get("receivers", []) if hasattr(email_cfg, "receivers") else []

    if not all([smtp_host, sender, password, receivers]):
        log.error("邮件配置不完整")
        return

    msg = MIMEMultipart("alternative")
    msg["Subject"] = title
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)
    msg.attach(MIMEText(content, "html", "utf-8"))

    try:
        with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
            server.login(sender, password)
            server.sendmail(sender, receivers, msg.as_string())
        log.info("邮件通知发送成功")
    except Exception as e:
        log.error(f"邮件通知发送异常: {e}")


def build_report_message(summary: dict) -> tuple:
    """
    构建测试报告通知内容

    Args:
        summary: 测试结果摘要 {
            "total": 10, "passed": 8, "failed": 1, "skipped": 1,
            "duration": "120s", "env": "staging"
        }

    Returns:
        (title, content) 元组
    """
    title = f"AirTestUI 自动化测试报告 - {summary.get('env', 'unknown')}"
    total = summary.get("total", 0)
    passed = summary.get("passed", 0)
    failed = summary.get("failed", 0)
    skipped = summary.get("skipped", 0)
    duration = summary.get("duration", "0s")
    env = summary.get("env", "unknown")
    pass_rate = f"{passed / total * 100:.1f}%" if total > 0 else "0%"

    content = f"""
### {title}

> 环境: **{env}** | 耗时: **{duration}**

| 指标 | 数值 |
|------|------|
| 总用例 | {total} |
| 通过 | {passed} |
| 失败 | {failed} |
| 跳过 | {skipped} |
| 通过率 | {pass_rate} |

---
*来自 AirTestUI 自动化测试框架*
"""
    return title, content
