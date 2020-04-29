"""
对列表的排序操作
"""

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)  # 对list1进行排序
# sorted函数返回列表排序后的拷贝不会修改传入的列表
list3 = sorted(list1, reverse=True)  # 在默认的字母排序进行降序排列
list4 = sorted(list1, key=len)  # 通过key关键字参数指定, 根据字符串长度进行排序

print('原始排序: ', list1)
print('默认排序: ', list2)
print('降序排序: ', list3)
print('长度排序: ', list4)

# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print('默认降序排序:', list1)
