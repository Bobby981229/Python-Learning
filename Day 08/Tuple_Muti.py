"""
空元组 - 一元组 - 多元组

一个元组中如果有两个元素，我们就称之为二元组；
一个元组中如果五个元素，我们就称之为五元组。
需要提醒大家注意的是，()表示空元组，
但是如果元组中只有一个元素，需要加上一个逗号，否则()就不是代表元组的字面量语法
"""

# 空元组
a = ()
print(type(a))    # <class 'tuple'>
print()

# 不是元组
b = ('hello')
print(type(b))    # <class 'str'>
c = (100)
print(type(c))    # <class 'int'>
print()

# 一元组
d = ('hello', )
print(type(d))    # <class 'tuple'>
e = (100, )
print(type(e))    # <class 'tuple'>
