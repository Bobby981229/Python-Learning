"""
练习题 03 输入年份判断是不是闰年
"""
year = int(input("请输入年份: "))
is_leap = year % 4 == 0 and year % 100 != 0
print("是否为闰年:", is_leap)
