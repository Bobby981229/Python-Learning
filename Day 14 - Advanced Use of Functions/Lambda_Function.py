"""
Lambda函数 - 匿名函数
"""

# 匿名函数只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值
# 定义Lambda函数的关键字是lambda，后面跟函数的参数，如果有多个参数用逗号进行分隔
# 冒号后面的部分就是函数的执行体，通常是一个表达式，表达式的运算结果就是Lambda函数的返回值，不需要写return 关键字
numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers1)))
print(numbers2)  # [144, 64, 3600, 2704]
print()


def calc(*args, init_value=0, op=lambda x, y: x + y, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result


# 调用calc函数，使用init_value和op的默认值
print(calc(1, 2, 3, x=4, y=5))  # 15
# 调用calc函数，通过lambda函数给op参数赋值
print(calc(1, 2, 3, x=4, y=5, init_value=1, op=lambda x, y: x * y))  # 120
print()

import operator, functools

# 一行代码定义求阶乘的函数
fac = lambda num: functools.reduce(operator.mul, range(1, num + 1), 1)
# 一行代码定义判断素数的函数
is_prime = lambda x: x > 1 and all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(10))  # 3628800
print(is_prime(9))  # False

"""
上面使用的reduce函数是Python标准库functools模块中的函数，它可以实现对数据的归约操作
通常情况下，过滤（filter）、映射（map）和归约（reduce）是处理数据中非常关键的三个步骤
而Python的标准库也提供了对这三个操作的支持.

上面使用的all函数是Python内置函数，如果传入的序列中所有布尔值都是True，all函数就返回True，否则all函数就返回False
"""