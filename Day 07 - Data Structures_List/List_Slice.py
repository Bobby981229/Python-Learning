"""
列表 - 切片操作
和字符串一样，列表也可以做切片操作，
通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表
"""

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']  # fruits = fruits + ['pitaya', 'pear', 'mango']
print('Fruits: ', fruits)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

# 列表切片
fruits2 = fruits[1:4]  # 1 2 3 号元素
print('Fruits2 ', fruits2)  # apple strawberry waxberry

fruits3 = fruits[:]  # 可以通过完整切片操作来复制列表
print('Fruits3: ', fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

fruits4 = fruits[-3:-1]  # 取-3, -2
print('Fruits4: ', fruits4)  # ['pitaya', 'pear']

fruits5 = fruits[::-1]  # 可以通过反向切片操作来获得倒转后的列表的拷贝
print('Fruits5: ', fruits5)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
