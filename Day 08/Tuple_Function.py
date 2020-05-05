"""
函数的可变参数
将多个参数打包成了一个元组
"""

def add(*args):
    print(type(args), args)
    total = 0
    for val in args:
        total += val
    print('Total: ', total)
    return total


add(1, 10, 20)        # <class 'tuple'> (1, 10, 20)
add(1, 2, 3, 4, 5)    # <class 'tuple'> (1, 2, 3, 4, 5)
