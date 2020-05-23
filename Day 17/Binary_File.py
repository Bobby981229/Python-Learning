"""
读写二进制文件
"""


def main():
    try:
        with open('F://Python//Github - Python 100 Days//Day 17//吉鲁.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('F://Python//Github - Python 100 Days//Day 17//吉鲁.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()
