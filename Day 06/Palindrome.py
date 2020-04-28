"""
回文数 —— 12321
"""


def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


num = int(input("Please input a integer number: "))
# 0 is false, 1 is true
print('The result of %d is: %d' % (num, is_palindrome(num)))
