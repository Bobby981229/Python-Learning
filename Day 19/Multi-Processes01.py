"""
进程和线程

进程就是操作系统中执行的一个程序，操作系统以进程为单位分配存储空间，每个进程都有自己的地址空间
数据栈以及其他用于跟踪进程执行的辅助数据，操作系统管理所有进程的执行，为它们合理的分配资源。
进程可以通过fork或spawn的方式来创建新的进程来执行其他的任务，不过新的进程也有自己独立的内存空间
因此必须通过进程间通信机制（IPC，Inter-Process Communication）来实现数据共享，具体的方式包括管道、信号、套接字、共享内存区等

一个进程还可以拥有多个并发的执行线索，简单的说就是拥有多个可以获得CPU调度的执行单元，这就是所谓的线程
由于线程在同一个进程下，它们可以共享相同的上下文，因此相对于进程而言，线程间的信息共享和通信更加容易
"""

# 多进程

from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s ......' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 共耗时%d秒!' % (filename, time_to_download))
    print()


def main():
    start = time()
    download_task('Python-进程和线程教学.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗时%2.f秒 ！' % (end - start))


if __name__ == '__main__':
    main()


