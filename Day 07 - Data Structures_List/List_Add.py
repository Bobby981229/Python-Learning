"""
向列表中添加元素以及如何从列表中移除元素。
"""

list1 = [1, 3, 5, 7, 100]
print('Origin: ', list1)  # [1, 3, 5, 7, 100]

# 添加元素
list1.append(200)  # 将新元素添加到list最后面
print('Add 01: ', list1)

list1.insert(1, 400)  # 在第1位添加新元素
print('Add 02: ', list1, '\n')

# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]  # list1 = list1 + [1000, 2000]
print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print('当前总长度: ', len(list1))  # 9, 显示当前List的长度

