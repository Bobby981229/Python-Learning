"""
创建和使用字典
字典的{}中的元素是以键值对的形式存在的，每个元素由:分隔的两个值构成，:前面是键，:后面是值
"""
# :前面是键，:后面是值
xinhua = {
    '麓': '山脚下', '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名', '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print('Xinhua:', xinhua)
person = {
    'name': '刘尚远', 'age': 21, 'weight': 68, 'office': '西影路46号',
    'home': '西影路46号', 'tel': '13121561120'
}
print('Info:', person)
print()

# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='刘尚远', age=21, weight=68, home='西影路46号')
print('Person-Dict函数:', person)    # {'name': '刘尚远', 'age': 21, 'weight': 68, 'home': '西影路46号'}
print()

# 可以通过Python内置zip函数压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print('item1:', items1)    # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print('item2:', items2)    # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
print()

# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}  # 1~5遍历, ** 乘方
print(items3)     # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
print()

# 键值对个数
person = {'name': '刘尚远', 'age': 21, 'weight': 68, 'home': '西影路46号'}
print('键值对个数:', len(person))    # 4
for key in person:
    print(key, person[key])
print()

