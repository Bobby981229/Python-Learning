list1 = [1, 3, 5, 7, 100, 200]

# 删除指定下标对应的元素  Del
print(list1)
del list1[5]
print('Del 5: ', list1)

# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素   Remove
if 3 in list1:
    list1.remove(3)  # 在list中删掉3

if 1234 in list1:
    list1.remove(1234)
print('Remove 3: ', list1)  # [1, 400, 5, 7, 100, 200, 1000, 2000]

# 从指定的位置删除元素  Pop
list1.pop(0)  # 删掉0号位的元素
list1.pop(len(list1) - 1)
print('Pop 0', list1)  # [400, 5, 7, 100, 200, 1000]


# 清空列表元素
list1.clear()
print('清空所有元素: ', list1)  # [], list为空
