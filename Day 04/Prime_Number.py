"""
素数
"""

from math import sqrt  # 开根号

number = int(input("请输入一个正整数: "))
result = int(sqrt(number))  # 对输入的数字进行开根号计算
is_Prime = True

for x in range(2, result + 1):
    if number % x == 0:  # 判断数字的模
        is_Prime = False
        break

if is_Prime and number != 1:
    print('%d是素数' % number)
else:
    print('%d不是素数' % number)
