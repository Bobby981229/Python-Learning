"""
计算最大公约数和最小公倍数。
"""
x = int(input('请输入第一个数值: '))
y = int(input('请输入第二个数值: '))

if x > y:
    x, y = y, x  # 交换数值

# 从两个数中较大的数开始做递减的循环
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print('%d和%d的最大公约数是: %d' % (x, y, i))
        print('%d和%d的最小公倍数是: %d' % (x, y, x * y // i))
        break
