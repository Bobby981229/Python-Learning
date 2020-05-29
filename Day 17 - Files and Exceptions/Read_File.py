"""
读取文件的方法
"""

import time


# with关键字指定文件对象
def main():
    try:
        with open("/Day 17 - Files and Exceptions//Info.txt", 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


if __name__ == '__main__':
    main()

print("\n*********************************\n")


# 使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器
def main():
    # 一次性读取整个文件内容
    with open('/Day 17 - Files and Exceptions//Info.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('/Day 17 - Files and Exceptions//Info.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('/Day 17 - Files and Exceptions//Info.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
