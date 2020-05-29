"""
通过生成式创建列表
"""

# 创建一个由1到9的数字构成的列表
items1 = [i for i in range(1, 10)]
print('items1: ', items1)
print()

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = [i for i in 'hello world' if i not in ' aeiou']  # 除了空格和O
print('items2: ', items2)
print()


# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = [x + y for x in 'ABC' for y in '12']  # 两个for循环嵌套
print('items3: ', items3)    # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
