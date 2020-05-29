"""
关键字参数
"""


# 判断传入的三条边长能否构成三角形的函数


def is_triangle(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and a + c > b and b + c > a


# 调用函数传入参数不指定参数名按位置对号入座
print(is_triangle(3, 4, 5))
print()
print(is_triangle(a=1, b=2, c=3))
print()
print(is_triangle(c=13, b=12, a=5))
print()
print('Please input 3 integer:')
print('The result is:', is_triangle(input(), input(), input()))
print()


# 关键字传参
# 参数列表中的*是一个分隔符，*前面的参数都是位置参数，而*后面的参数就是命名关键字参数
def can_form_triangle(*, a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c, a + c > b, b + c > a


# TypeError: can_form_triangle() takes 0 positional arguments but 3 were given
# print(is_valid_for_triangle(3, 4, 5))
# 传参时必须使用“参数名=参数值”的方式，位置不重要
print(can_form_triangle(a=3, b=4, c=5))
print(can_form_triangle(c=5, b=4, a=3))
print()


# 使用可变参数*args来接收任意数量的参数
# 使用可变参数和关键字参数。关键字参数会将传入的带参数名的参数组装成一个字典
# 参数名就是字典中键值对的键，而参数值就是字典中键值对的值
def calc(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for value in kwargs.values():
        result += value
    return result


print(calc())                  # 0
print(calc(1, 2, 3))           # 6
print(calc(a=1, b=2, c=3))     # 6
print(calc(1, 2, c=3, d=4))    # 10
