"""
实例 03.1
1~100000000求和的计算密集型任务
"""

from time import time


def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]  # 将1~10000000加入数列表中
    start = time()  # 开始计数

    # 将列表中的数字进行遍历相加
    for number in number_list:
        total += number

    print(total)
    end = time()  # 结束计时
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()



