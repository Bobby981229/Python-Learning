""" 集合的方法 """
# Python中的集合是可变类型，我们可以通过集合类型的方法为集合添加或删除元素。

# 创建一个空集合
set1 = set()
# 通过add方法添加元素
set1.add(33)
set1.add(55)
set1.update({1, 10, 100, 1000})  # 添加
print('set1:', set1)  # {33, 1, 100, 55, 1000, 10}
print()

# 通过discard方法删除指定元素
set1.discard(100)
set1.discard(99)
print('set1-discard:', set1)  # {1, 10, 33, 55, 1000}

# 通过remove方法删除指定元素，建议先做成员运算再删除
# 否则元素如果不在集合中就会引发KeyError异常
if 10 in set1:
    set1.remove(10)
print('set1-remove:', set1)  # {33, 1, 55, 1000}

# pop方法可以从集合中随机删除一个元素并返回该元素
print('set1-pop:', set1.pop())

# clear方法可以清空整个集合
set1.clear()
print('set1-clear:', set1)  # set()
print()

""" 两个集合相同的元素 """
set1 = {'Java', 'Python', 'Go', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Objective-C', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print('相同的元素:', set1.intersection(set2))
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True
print()

""" 不可变集合 """
set1 = frozenset({1, 3, 5, 7})
set2 = frozenset(range(1, 6))  # frozenset(1, 2, 3, 4, 5)
print('交集:', set1 & set2)    # frozenset({1, 3, 5})
print('并集:', set1 | set2)    # frozenset({1, 2, 3, 4, 5, 7})
print('差值:', set1 - set2)    # frozenset({7})
print('真子集:', set1 < set2)    # False
