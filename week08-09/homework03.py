"""
作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""
import time
from functools import wraps


def timer(func):
    print("timer...")

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("{} ran in {}s".format(func.__name__, round(end - start, 5)))
        return result

    return wrapper


@timer
def runtest():
    for i in range(100):
        print(f"start run {i}")


if __name__ == "__main__":
    runtest()
