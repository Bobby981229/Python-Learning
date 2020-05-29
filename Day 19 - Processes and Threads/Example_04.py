"""
实例 03.2
1~100000000求和的计算密集型任务 -- 多进程
"""

from time import time
from threading import Thread
from random import randint
from multiprocessing import Process, Queue


def task_handle(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0

    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handle, args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()

        # 开始记录所有进程执行完成花费的时间
        start = time()
        for p in processes:
            p.join()
        # 合并执行结果
        total = 0
        while not result_queue.empty():
            total += result_queue.get()
        print(total)
        end = time()
        print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()
