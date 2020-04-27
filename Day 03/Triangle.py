"""
输入三条边长，如果能构成三角形就计算周长和面积
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print('三角形周长: ', a + b + c)
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5  # 海伦公式 **0.5 开根号
    print('三角形面积: %.2f' % s)
else:
    print('该三角形不存在 ！')
