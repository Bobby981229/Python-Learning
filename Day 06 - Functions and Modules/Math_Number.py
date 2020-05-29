"""
实现计算求最大公约数和最小公倍数的函数
"""


def gcd(x, y):  # 计算最大公约数
    # if x > y:
    #     (x, y) = (y, x)
    # else:
    #     (x, y)

    (x, y) = (y, x) if x > y else (x, y)
    for i in range(x, 0, -1):  # 从两个数中较大的数开始做递减的循环
        if x % i == 0 and y % i == 0:
            return i


def lcm(x, y):  # 计算最小公倍数
    return x * y // gcd(x, y)  # 两数乘积 / 最大公约数


x = int(input("x = "))
y = int(input("y = "))
print('%d和%d的最大公约数是: %d' % (x, y, gcd(x, y)))  # 调用函数，计算并显示最大公约数
print('%d和%d的最小公倍数是: %d' % (x, y, lcm(x, y)))  # 调用函数，计算并显示最小公倍数
