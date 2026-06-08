"""
重试装饰器模块
提供灵活的重试机制，支持条件重试和指数退避
"""
import time
import functools

from utils.logger import get_logger

log = get_logger("Retry")


def retry(
    max_attempts: int = 2,
    wait_between: float = 3.0,
    retry_on: tuple = (Exception,),
    on_retry=None,
):
    """
    通用重试装饰器

    Args:
        max_attempts: 最大重试次数（含首次执行）
        wait_between: 重试间隔（秒）
        retry_on: 触发重试的异常类型元组
        on_retry: 重试前的回调函数，签名为 on_retry(attempt, exception)

    用法:
        @retry(max_attempts=3, wait_between=2)
        def click_login():
            ...

        @retry(retry_on=(TimeoutError, AssertionError))
        def wait_for_element():
            ...
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    if attempt > 1:
                        log.info(f"{func.__qualname__} 第 {attempt} 次尝试成功")
                    return result
                except retry_on as e:
                    last_exception = e
                    if attempt < max_attempts:
                        log.warning(
                            f"{func.__qualname__} 第 {attempt} 次执行失败: {e}，"
                            f"{wait_between}s 后重试..."
                        )
                        if on_retry:
                            on_retry(attempt, e)
                        time.sleep(wait_between)
                    else:
                        log.error(
                            f"{func.__qualname__} 已达最大重试次数 {max_attempts}，"
                            f"最终异常: {e}"
                        )
            raise last_exception
        return wrapper
    return decorator


def retry_until_true(
    func=None,
    max_attempts: int = 10,
    interval: float = 1.0,
):
    """
    持续重试直到函数返回 True

    Args:
        func: 被装饰的函数，应返回 bool
        max_attempts: 最大检查次数
        interval: 检查间隔（秒）

    用法:
        @retry_until_true(max_attempts=20, interval=2)
        def is_page_loaded():
            return exists(Template("loaded.png"))
    """
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                result = fn(*args, **kwargs)
                if result:
                    log.debug(f"{fn.__qualname__} 条件满足 (第 {attempt} 次检查)")
                    return True
                if attempt < max_attempts:
                    time.sleep(interval)
            log.warning(f"{fn.__qualname__} 条件始终未满足 (共 {max_attempts} 次检查)")
            return False
        return wrapper

    if func is not None:
        return decorator(func)
    return decorator
