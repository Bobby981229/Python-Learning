"""
阿姆斯特朗数 - 水仙花数
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身
"""

for number in range(100, 1000):
    a = number % 10  # 个位
    b = number // 10 % 10  # 十位
    c = number // 100  # 百位
    if number == a ** 3 + b ** 3 + c ** 3:
        print(number)

