"""
__del__ 方法
"""


# 定义类
class Cat:

    def __init__(self, new_name):  # 设置形参new_name
        self.name = new_name
        print("%s 来了" % self.name)  # 输出

    def __del__(self):  # 销毁对象 - 自动调用
        print("%s 我去了" % self.name)


# tom 是个全局变量
tom = Cat("Bobby")  # 创建对象，指定new_name对应的实参
print(tom.name)

print("-" * 50)

