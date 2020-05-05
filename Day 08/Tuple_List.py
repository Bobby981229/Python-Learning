"""
元组和列表的比较
"""
# 元组是不可变类型，不可变类型更适合多线程环境，因为它降低了并发访问变量的同步化开销
# 元组是不可变类型，通常不可变类型在创建时间和占用空间上面都优于对应的可变类型。
# 我们可以使用sys模块的getsizeof()函数来检查保存相同元素的元组和列表各自占用了多少内存空间。
# 我们也可以使用timeit模块的timeit函数来查看创建保存相同元素的元组和列表各自花费的时间

import sys
import timeit

# 0 ~ 99999
a = list(range(100000))
b = tuple(range(100000))

print('list a 所占用的内存: ', sys.getsizeof(a))   # 内存: 900120
print('tuple b 所占用的内存: ', sys.getsizeof(b))  # 内存: 800056
print()

print('list a 所花费的时间: ', timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
print()

print('tuple b 所花费的时间: ', timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))
print()

# 与列表相比, 创建元组所占用的内存和花费的时间都要低于


# 将元组转换成列表
info = ('刘尚远', 173, True, '陕西西安')
print(list(info))       # ['刘尚远', 173, True, '陕西西安']
print()

# 将列表转换成元组
fruits = ['apple', 'banana', 'orange']
print(tuple(fruits))    # ('apple', 'banana', 'orange')
