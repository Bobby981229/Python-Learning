"""
集合的运算
成员运算、交集运算、并集运算、差集运算、比较运算（相等性、子集、超集）等
"""

""" 成员运算 - 可以通过成员运算in和not in 检查元素是否在集合中 """
print('成员运算')
set1 = {11, 12, 13, 14, 15}
print('set1: ', set1)
print('10 in set1:', 10 in set1)        # False
print('15 in set1:', 15 in set1)        # True
print()

set2 = {'Python', 'Java', 'Go', 'Swift'}
print('set2:', set2)
print('Ruby in set2: ', 'Ruby' in set2)    # False
print('Java in set2: ', 'Java' in set2)    # True
print()

""" 交并差运算 - 可以进行交集、并集、差集等运算，而且可以通过运算符和方法调用两种方式来进行操作 """
print('交并差运算')
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}
print('set1:', set1)
print('set2:', set2)
print()

# 交集 —— 两个集合重合的部分
# 方法一: 使用 & 运算符
print('交集:', set1 & set2)                # {2, 4, 6}
# 方法二: 使用intersection方法
print('交集:', set1.intersection(set2))    # {2, 4, 6}
print()

# 并集 —— 两个集合合并
# 方法一: 使用 | 运算符
print('并集:', set1 | set2)         # {1, 2, 3, 4, 5, 6, 7, 8, 10} - 去重
# 方法二: 使用union方法
print('并集:', set1.union(set2))    # {1, 2, 3, 4, 5, 6, 7, 8, 10} - 去重
print()

# 差集 —— 求差值
# 方法一: 使用 - 运算符
print('差集:', set1 - set2)              # {1, 3, 5, 7}
# 方法二: 使用difference方法
print('差集:', set1.difference(set2))    # {1, 3, 5, 7}
print()

# 对称差
# 方法一: 使用 ^ 运算符
print('对称差:', set1 ^ set2)                        # {1, 3, 5, 7, 8, 10}
# 方法二: 使用symmetric_difference方法
print('对称差:', set1.symmetric_difference(set2))    # {1, 3, 5, 7, 8, 10}
# 方法三: 对称差相当于两个集合的并集减去交集
print('对称差:', (set1 | set2) - (set1 & set2))      # {1, 3, 5, 7, 8, 10}
print()

# 复合运算
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
# 将set1和set2求并集再赋值给set1
# 也可以通过set1.update(set2)来实现
set1 |= set2
print("并集:", set1)    # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
# 将set1和set3求交集再赋值给set1
# 也可以通过set1.intersection_update(set3)来实现
set1 &= set3
print("交集:", set1)    # {3, 6}
print()

""" 比较运算 """
# 两个集合可以用==和!=进行相等性判断，如果两个集合中的元素完全相同，那么==比较的结果就是True，否则就是False
# 子集： 如果集合A的任意一个元素都是集合B的元素，那么集合A称为集合B的子集，即对于∀a∈A，均有a∈B，则A⊆B。
# 真子集：如果A是B的子集,并且B中至少有一个元素不属于A,那么集合A叫做集合B的真子集.
# 超集： 如果一个集合S2中的每一个元素都在集合S1中，且集合S1中可能包含S2中没有的元素，
# 则集合S1就是S2的一个超集，反过来，S2是S1的子集。 S1是S2的超集，若S1中一定有S2中没有的元素，则S1是S2的真超集，反过来S2是S1的真子集。
print('比较运算')
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
print('set1:', set1)
print('set2:', set2)
set3 = set2
print('set3:', set3)

# < 运算符表示真子集，<= 运算符表示子集
print('真子集, 子集:', set1 < set2, set1 <= set2)    # True True
print('真子集, 子集:', set2 < set3, set2 <= set3)    # False True

# 通过issubset方法也能进行子集判断
print('子集:', set1.issubset(set2))      # True

# 反过来可以用issuperset或>运算符进行超集判断
print('超集:', set2.issuperset(set1))    # True
print('超集:', set2 > set1)              # True
