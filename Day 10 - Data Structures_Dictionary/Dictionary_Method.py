"""
字典的方法
字典类型的方法基本上都跟字典的键值对操作相关

"""

# 字典中的值又是一个字典(嵌套的字典)
students = {
    1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
    1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
}

# 使用get方法通过键获取对应的值，如果取不到不会引发KeyError异常而是返回None或设定的默认值
print('1001:', students.get(1001))
print('1002:', students.get(1002))  # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print('1005:', students.get(1005))  # None
print('1006:', students.get(1005, {'name': '无名氏'}))  # {'name': '无名氏'}
print()

# 获取字典内所有的键
print('Keys:', students.keys())
# 获取字典内所有的值
print('Values:', students.values())
print()

# 对字典中所有的键值对进行循环遍历
for key, value in students.items():
    print(key, '--->', value)
print()

# 使用pop方法通过键删除对应的键值对并返回该值
stu1 = students.pop(1002)
print('students-pop:', stu1)  # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print('length:', len(students))  # 2
# stu2 = students.pop(1005)    # KeyError: 1005
stu2 = students.pop(1005, {})
print(stu2)
print()

# 使用popitem方法删除字典中最后一组键值对并返回对应的二元组
# 如果字典中没有元素，调用该方法将引发KeyError异常
key, value = students.popitem()  # 删掉最后一个
print(key, value)  # 1003 {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
print()

# setdefault可以更新字典中的键对应的值或向字典中存入新的键值对
# setdefault方法的第一个参数是键，第二个参数是键对应的值
# 如果这个键在字典中存在，更新这个键之后会返回原来与这个键对应的值
# 如果这个键在字典中不存在，方法将返回第二个参数的值，默认为None
result = students.setdefault(1005, {'name': '方启鹤', 'sex': True})
print('result:', result)  # {'name': '方启鹤', 'sex': True}
print('students:', students)  # {1001: {...}, 1005: {...}}
print()

# 使用update更新字典元素，相同的键会用新值覆盖掉旧值，不同的键会添加到字典中
others = {
    1005: {'name': '乔峰', 'sex': True, 'age': 32, 'place': '北京大兴'},
    1008: {'name': '钟灵', 'sex': False},
    1010: {'name': '王语嫣', 'sex': False, 'age': 19}
}
students.update(others)
for key, value in students.items():
    print(key, '--->', value)  # {1001: {...}, 1005: {...}, 1010: {...}, 1008: {...}}
print()

# 删除元素
person = {'name': '王大锤', 'age': 25, 'sex': True}
print('person:', person)    # {'name': '王大锤', 'age': 25, 'sex': True}
del person['age']
print('person-del:', person)    # {'name': '王大锤', 'sex': True}
