"""
递归调用

Python中允许函数嵌套定义，也允许函数之间相互调用
而且一个函数还可以直接或间接的调用自身，函数自己调用自己称为递归调用
"""


# 非负整数N的阶乘
def fac(num):
    if num in (0, 1):  # 递归的收敛条件
        return 1  # 结束函数的递归调用
    return num * fac(num - 1)  # 调用自身函数


# 递归调用函数入栈
# 5 * fac(4)
# 5 * (4 * fac(3))
# 5 * (4 * (3 * fac(2)))
# 5 * (4 * (3 * (2 * fac(1))))
# 停止递归函数出栈
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120
result = fac(5)  # 计算5的阶乘
print('Result of fac 5: ', result)  # 120
print()

"""
函数调用会通过内存中称为“栈”（stack）的数据结构来保存当前代码的执行现场，函数调用结束后会通过这个栈结构恢复之前的执行现场
栈是一种先进后出的数据结构，这也就意味着最早入栈的函数最后才会返回，而最后入栈的函数会最先返回
调用一个名为a的函数，函数a的执行体中又调用了函数b，函数b的执行体中又调用了函数c，那么最先入栈的函数是a，最先出栈的函数是c
内存中的栈空间很小，因此递归调用的次数如果太多，会导致栈溢出（stack overflow）
"""


# 斐波那契数列
# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# 打印前20个斐波那契数
for i in range(1, 21):
    print(fib(i))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
