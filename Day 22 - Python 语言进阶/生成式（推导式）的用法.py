"""
生成式（推导式）的用法
"""

# 创造一个股票字典
price = {
    'Apple': 191.88,
    'Google': 1186.96,
    'IBM': 149.24,
    'Oracle': 48.44,
    'ACN': 166.89,
    'FBI': 208.09
}

print('price: ', price)
print()

# 用股票价格大于100元的股票构造一个新的字典
price2 = {key: value for key, value in price.items() if value > 100}
print('price2: ', price2)

# 生成式（推导式）可以用来生成列表、集合和字典
