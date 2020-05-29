from random import randint


def roll_dice(n=2):  # 默认两个骰子
    """摇色子"""
    total = 0
    for _ in range(n):  # 循环两次
        total += randint(1, 6)  # 从1~6中随机选取一位，相加计算得出total
    return total  # 返回total


def add(a=0, b=0, c=0):  # 定义a, b, c三个参数
    # 三个数相加
    return a + b + c


print('默认两颗骰子: %d' % roll_dice())  # 如果没有指定参数那么使用默认值摇两颗色子
print()

print('定义三颗骰子: %d' % roll_dice(3))  # 摇三颗色子
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
print('\n***************************************************************************\n')

"""
在参数名前面的*表示args是一个可变参数
"""


def add(*args):  # 定义循环次数
    total = 0
    for val in args:
        total += val  # 累加， total = total + val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))