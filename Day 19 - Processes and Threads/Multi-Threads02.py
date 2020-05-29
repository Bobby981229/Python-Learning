"""
多线程
通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程
"""

from random import randint
from threading import Thread
from time import time, sleep


# 创建自定义的线程类
class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("开始下载 %s ... " % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print("%s 下载完成，耗时%d秒" % (self._filename, time_to_download))
        print()


def main():
    start = time()

    # 创建线程对象
    t1 = DownloadTask("Python-进程和线程教学.pdf")
    t2 = DownloadTask("Peking Hot.avi")

    # 启动线程
    t1.start()
    t2.start()

    # 等待线程结束
    t1.join()
    t2.join()

    end = time()
    print("下载完成，总耗时%.3f秒" % (end - start))


if __name__ == "__main__":
    main()
