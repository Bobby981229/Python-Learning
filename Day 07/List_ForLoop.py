"""
列表的生成式
通过for循环为空列表添加元素
"""

# 创建一个由1到9的数字构成的列表
items1 = []
for x in range(1, 10):  # 1 ~ 9
    items1.append(x)
print(items1)
print()

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = []
for x in 'hello world':
    if x not in ' aeiou':  # 去掉o和空格
        items2.append(x)
print(items2)
print()


# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = []
for x in 'ABC':
    for y in '12':
        items3.append(x + y)  # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
print(items3)



