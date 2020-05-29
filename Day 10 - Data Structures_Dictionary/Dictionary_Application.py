"""
字典的应用
"""

# 输入一段话，统计每个英文字母出现的次数
sentence = input('请输入一段话: ')
counter = {}
for i in sentence:
    if 'A' <= i <= 'Z' or 'a' <= i <= 'z':  # 判断a~z的大小写字母
        counter[i] = counter.get(i, 0) + 1  # 将出现的字母添加到字典中
for key, value in counter.items():
    print(f'字母{key}出现了{value}次.')
print()


# 在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典
""" 创建股票字典 公司:价格 """
stocks = {
    'Apple': 191.88,
    'GOOGLE': 1186.96,
    'IBM': 149.24,
    'ORACLE': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'TCL': 21.29
}

stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)
print()

# 创建一个新的字典, 将价格大于100的元素存入
stocks3 = {key for key, value in stocks.items() if value > 100}
print('价格大于100的公司:', stocks3)

