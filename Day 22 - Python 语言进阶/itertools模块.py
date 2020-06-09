"""
itertools模块
迭代工具模块
"""

import itertools

# 产生ABCD的全排列
sort1 = itertools.permutations('ABCD')
print(sort1)
print()

# 产生ABCDE的五选三组合
itertools.combinations('ABCDE', 3)
# 产生ABCD和123的笛卡尔积
itertools.product('ABCD', '123')
# 产生ABC的无限循环序列
itertools.cycle(('A', 'B', 'C'))
