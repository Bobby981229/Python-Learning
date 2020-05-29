"""
使用变量保存数据并进行加减乘除运算
"""
a = 321
b = 123
print(a + b)  # 加
print(a - b)  # 减
print(a * b)  # 乘
print(a / b)  # 除
print(a // b)  # 整除
print(a % b)  # 模 - 整数除法求余数
print(a ** b)  # 指数
print("\n***********************************************************************************\n")

"""
赋值运算符和复合赋值运算符
"""
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print("The value of a = %d" % a)      # 算一下这里会输出什么
print("\n***********************************************************************************\n")

"""
比较运算符和逻辑运算符的使用
"""
flag0 = 1 == 1  # True
flag1 = 3 > 2  # True
flag2 = 2 < 1  # False
flag3 = flag1 and flag2  # False
flag4 = flag1 or flag2  # True
flag5 = not (1 != 2)  # False
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False


