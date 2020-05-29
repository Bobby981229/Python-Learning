"""
素数
"""

from math import sqrt  # 开根号


def prime(num):
    result = int(sqrt(num))  # 对输入的数字进行开根号计算
    for x in range(2, result + 1):
        if num % x == 0:  # 判断数字的模
            return False
    return True if num != 1 else False


num = int(input('Please input a integer number: '))
# 0 is false, 1 is true
print('%d result: %d' % (num, prime(num)))
