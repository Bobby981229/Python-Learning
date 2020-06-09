"""
heapq模块（堆排序）

从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""

import heapq

# 创造一个列表
grade = [24, 60, 88, 100, 54, 43, 76, 66, 92, 36, 45]

# 创造一个字典
price = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'Apple', 'shares': 50, 'price': 543.22},
    {'name': 'FBI', 'shares': 200, 'price': 21.09},
    {'name': 'Google', 'shares': 35, 'price': 31.75},
    {'name': 'Oracle', 'shares': 45, 'price': 16.35},
    {'name': 'ACN', 'shares': 75, 'price': 115.65}
]

print('成绩最高的三个:', sorted(heapq.nlargest(3, grade)))  # 成绩最高的三个 + 排序
print('成绩最低的三个:', sorted(heapq.nsmallest(3, grade)))  # 成绩最低的三个 + 排序
print()

print('价格最高的两个:', heapq.nlargest(2, price, key=lambda x: x['price']))
print('份额最低的两个:', heapq.nsmallest(2, price, key=lambda x: x['shares']))

