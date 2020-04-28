"""
Python中每个文件就代表了一个模块（module），
我们在不同的模块中可以有同名的函数，
在使用函数的时候我们通过import关键字导入指定的模块就可以区分到底要使用的是哪个模块中的foo函数
"""

from module1 import foo

# 输出hello, world!
foo()

from module2 import foo

# 输出goodbye, world!
foo()

print('****************************************')

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()


# def foo():
#     print('hello, world!')


# def foo():
#     print('goodbye, world!')





