"""
多进程 - Process类创建了进程对象
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print("开始下载%s ..." % filename)
    time_to_download = randint(5, 10)  # 随机生成下载所需要的时间 5~10秒
    sleep(time_to_download)  # 推迟调用线程的运行
    print()
    print("%s下载完成，共耗时%d秒" % (filename, time_to_download))


def main():
    start = time()  # 开始计时

    """
    通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码
    后面的args是一个元组，它代表了传递给函数的参数
    """
    p1 = Process(target=download_task, args=("Python-进程和线程教学.pdf",))  # 调用函数，创建新的进程
    p2 = Process(target=download_task, args=("Peking Hot.avi",))  # 调用函数，创建新的进程

    p1.start()  # 启动进程
    p2.start()  # 启动进程

    # 等待进程执行结束
    p1.join()
    p2.join()

    end = time()  # 停止计时
    print("总耗时%.2f秒" % (end - start))  # 计算运行main函数所需要的总时间


if __name__ == '__main__':
    main()
