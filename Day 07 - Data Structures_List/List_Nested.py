"""
嵌套的循环
如果列表中的元素又是列表，那么我们可以称之为嵌套的列表。
嵌套的列表可以用来表示表格或数学上的矩阵
"""

# 嵌套的列表需要多次索引操作才能获取元素
scores = [[0] * 3 for _ in range(5)]
scores[0][0] = 95
print(scores)    # [[95, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]