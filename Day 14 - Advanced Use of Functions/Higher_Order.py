"""
高阶函数的用法
"""


# init_value代表运算的初始值，op代表二元运算函数
def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


# 将函数作为参数和调用函数是有显著的区别的，调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可
print(calc(init_value=0, op=add, x=4, y=5))  # 9
print(calc(init_value=1, op=mul, x=3, y=4, z=5))  # 60
print()


# filter和map函数都是高阶函数
# 前者可以实现对序列中元素的过滤，后者可以实现对序列中元素的映射
# 例如我们要去掉一个整数列表中的奇数，并对所有的偶数求平方得到一个新的列表

# 得到偶数
def is_even(num):
    return num % 2 == 0


# 进行平方处理
def square(num):
    return num ** 2


numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(square, filter(is_even, numbers1)))  # 在numbers1中使用filter过滤掉奇数, 并把剩余的偶数进行平方处理保存在numbers2中
print(numbers2)    # [144, 64, 3600, 2704]
print()

# 使用列表生成式
numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = [num ** 2 for num in numbers1 if num % 2 == 0]
print(numbers2)    # [144, 64, 3600, 2704]
