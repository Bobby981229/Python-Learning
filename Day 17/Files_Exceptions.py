"""
文件和异常
实际开发中常常会遇到对数据进行持久化操作的场景，而实现数据持久化最直接简单的方式就是将数据保存到文件中
"""
import time

"""
读取文本文件时，需要在使用open函数时指定好带路径的文件名（相对路径或绝对路径）并将文件模式设置为'r'
然后通过encoding参数指定编码，如果不能保证保存文件时使用的编码方式与encoding参数指定的编码方式是一致的
那么就可能因无法解码字符而导致读取失败
"""


# 当文件不存在时，捕获异常
def main():
    f = None
    try:
        f = open('F://Python//Github - Python 100 Days//Day 17//Info.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()
    print()




