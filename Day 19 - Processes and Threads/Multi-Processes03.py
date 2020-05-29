"""
多进程 - subprocess模块中的类和函数来创建和启动子进程, 然后通过管道来和子进程通信
"""

# 如何实现两个进程间的通信

from multiprocessing import Process
from time import time, sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:  # 当counter小于10时，一直循环
        print(string, end="", flush=True)
        counter += 1
        sleep(0.01)


def main():
    Process(target=sub_task, args=("Ping ",)).start()  # 启动进程
    Process(target=sub_task, args=("Pong ",)).start()  # 启动进程


if __name__ == '__main__':
    main()