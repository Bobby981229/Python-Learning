"""
字符串运算符

判断是否为小写字母: 'a' <= char <= 'z'
判断是否为大写字母: 'A' <= char <= 'Z'
判断是否为字母: 'a' <= char <= 'z' or 'A' <= char <= 'Z'
判断是否为中文: '\u4e00' <= char <= '\u9fa5'
判断是否为数字: '0' <= char <= '9'
"""

# 统计字符串中小写字母的个数

str1 = "Hello, World !"
count = 0

# 遍历循环查找字符串中的小写字母
for char in str1:
    if 'a' <= char <= 'z':
        count += 1

print('字符串中小写字母的格式为: ', count)




