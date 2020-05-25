"""
多线程

在Python早期的版本中就引入了thread模块（现在名为_thread）来实现多线程编程，然而该模块过于底层，而且很多功能都没有提供
因此目前的多线程开发我们推荐使用threading模块，该模块对多线程编程提供了更好的面向对象的封装
"""

from threading import Thread
from time import time, sleep
from random import randint


def download_task(filename):
    print("正在下载 %s ... " % filename)
    time_to_download = randint(5, 10)  # 随机设置下载所需要的时间
    sleep(time_to_download)  # 定时，线程休眠
    print()
    print("%s 下载完成，耗费时间为%d秒" % (filename, time_to_download))


def main():
    start = time()  # 开始计数

    # 调用函数，创建新的线程
    t1 = Thread(target=download_task, args=("Python-进程和线程教学.pdf",))
    t2 = Thread(target=download_task, args=("Peking Hot.avi",))

    # 启动线程
    t1.start()
    t2.start()

    # 等待线程执行结束
    t1.join()
    t2.join()

    end = time()  # 停止计时
    print("\n下载完成，总耗时%.3f秒" % (end - start))


if __name__ == "__main__":
    main()
