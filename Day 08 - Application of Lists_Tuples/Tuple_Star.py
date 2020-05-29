"""
星号表达式 - 相当于列表
让一个变量接收多个值
在解包语法中，星号表达式只能出现一次
"""

a = 1, 10, 100, 1000

i, j, *k = a
print('*在后面时: ', i, j, k)          # 1 10 [100, 1000]
print()

i, *j, k = a
print('*在中间时: ', i, j, k)          # 1 [10, 100] 1000
print()

*i, j, k = a
print('*在前面时: ', i, j, k)          # [1, 10] 100 1000
print()

*i, j = a
print(i, j)             # [1, 10, 100] 1000
print()

i, *j = a
print(i, j)             # 1 [10, 100, 1000]
print()

i, j, k, *l = a
print(i, j, k, l)       # 1 10 100 [1000]
print()

i, j, k, l, *m = a
print(i, j, k, l, m)    # 1 10 100 1000 []
print()

# range函数
a, b, *c = range(1, 10)
print(a, b, c)
print()

a, b, c = [1, 10, 100]
print(a, b, c)
print()

a, *b, c = 'hello'
print(a, b, c)
