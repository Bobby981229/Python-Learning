"""
字典的运算
"""

person = {'name': '刘尚远', 'age': 21, 'weight': 68, 'home': '西影路46号'}
# 检查name和tel两个键在不在person字典中
print('name & tel in person:', 'name' in person, 'tel' in person)    # True False
print()

# 通过age修将person字典中对应的值修改为22
if 'age' in person:  # 如果age存在person中, 则修改age的值
    person['age'] = 22
    print('修改后的age:', person.get('age'))
    for key, value in person.items():
        print('修改后的person:', key, value)
print()

# 通过索引操作向person字典中存入新的键值对
person['tel'] = '13122334455'
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去赢取你的闺蜜'
print('name & tel', 'name' in person, 'tel' in person)    # True True
print()

# 检查person字典中键值对的数量print('键值对个数:', len(person))    # 6
# 对字典的键进行循环并通索引运算获取键对应的值
for key in person:
    print(f'{key}: {person[key]}')
