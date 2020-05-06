"""
定义和使用元组

元组是不可变类型，这就意味着元组类型的变量一旦定义，
其中的元素不能再添加或删除，而且元素的值也不能进行修改
"""

# 定义一个三元组
t1 = (30, 10, 55)

# 定义一个四元组
t2 = ('刘尚远', 21, True, '陕西西安')

# 查看变量的类型
print('t1的类型: ', type(t1))
print('t2的类型: ', type(t2))
print()

# 查看元组中元素的数量
print('t1中元素的数量: ', len(t1))
print('t1中元素的数量: ', len(t2))
print()

# 通过索引运算获取元组中的元素
print(t1[0], t1[1])
print(t2[0], t2[1], t2[3])
print()

# 循环遍历元组中的元素
for element in t2:
    print(element)
print()

# 成员运算 - 判断元组中的元素是否存在
print('t1中包含50: ', 50 in t1)
print('t2中包含刘尚远: ', '刘尚远' in t2)
print()

# 拼接
t3 = t1 + t2  # 两个元组相加
print('t1 + t2 = ', t3)
print()

# 切片
print('切片: ', t3[::3])  # 每隔3个元素取一位
print()

# 比较运算
print('t1 = t2 : ', t1 == t2)
print('t1 >= t3 : ', t1 >= t3)
print('t1 < (30, 11, 55) : ', t1 < (30, 11, 55))