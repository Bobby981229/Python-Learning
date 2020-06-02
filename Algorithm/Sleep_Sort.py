"""
Sleep_Sort --- 睡眠排序
"""
import time
import threading


# 睡眠的方法
def do_sleep(func):
    time.sleep(float(func))  # 使用幂函数就可以负数排序了 --> pow(1.1, float(func))
    print('---> ', func)


def main():
    # 需要排序的序列
    num = [5, 3, 9, 11, 10, 12, 0, 8, 16, 1, 9]

    start = time.perf_counter()  # 开始计时
    thread_list = []  # 将多个线程存在一个数组中

    # 创建线程
    for i in range(len(num)):
        temp = threading.Thread(target=do_sleep, args=(str(num[i]), ))
        thread_list.append(temp)

    for t in thread_list:
        t.start()  # 开启线程

    for t in thread_list:
        t.join()  # 关闭线程

    end = time.perf_counter()

    print('总耗时:', str(end - start))


if __name__ == "__main__":
    main()

