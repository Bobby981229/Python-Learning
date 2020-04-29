"""
列表 - list
列表（list），也是一种结构化的、非标量类型，它是值的有序序列;
每个值都可以通过索引进行标识，定义列表可以将列表的元素放在[]中;
多个元素用,进行分隔，可以使用for循环对列表元素进行遍历，也可以使用[]或[:]运算符取出列表中的一个或多个元素。
"""

list1 = [1, 3, 5, 7, 100]
print(list1)  # [1, 3, 5, 7, 100]
print()

# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2)  # ['hello', 'hello', 'hello']
print()

# 计算列表长度(元素个数)
print(len(list1))  # 5
# 下标(索引)运算
print(list1[0])  # 1
print(list1[4])  # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1])  # 100
print(list1[-3])  # 5
print()

list1[2] = 300  # 将list1中第三个元素替换为300
print(list1)  # [1, 3, 300, 7, 100]
print()

# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])  # 打印list1中当前元素
print()

# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
print()

# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)


