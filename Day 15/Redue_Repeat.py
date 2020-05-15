# 把记录函数执行时间的功能封装到一个装饰器中，在有需要的地方直接使用这个装饰器就可以了

import time
import random


def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')

# 定义装饰器函数，它的参数是被装饰的函数或类
# 定义一个带装饰功能（记录被装饰函数的执行时间）的函数
# 因为不知道被装饰的函数有怎样的参数所以使用*args和**kwargs接收所有参数
# 在Python中函数可以嵌套的定义（函数中可以再定义函数）


def record_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()  # 在执行被装饰的函数之前记录开始时间
        result = func(*args, **kwargs)  # 执行被装饰的函数并获取返回值
        end = time.time()  # 在执行被装饰的函数之后记录结束时间
        print(f'{func.__name__}执行时间: {end - start:.3f}秒\n')  # 计算和显示被装饰函数的执行时间
        return result  # 返回被装饰函数的返回值（装饰器通常不会改变被装饰函数的执行结果）

    # 返回带装饰功能的wrapper函数
    return wrapper


download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
print()
