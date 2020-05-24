"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

import re


def main():
    user_name = input("请输入用户名: ")
    qq_number = input("请输入QQ号码: ")

    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[a-zA-Z0-9_]{6,20}$', user_name)
    m2 = re.match(r'^[1-9]\d{4,11}', qq_number)

    if not m1:
        print("请输入有效的用户名 !")

    if not m2:
        print("请输入有效的QQ号码 !")

    if m1 and m2:
        print("用户名和QQ号码输入正确 ！")


if __name__ == '__main__':
    main()
