"""
定义类
"""


# 定义"猫"类
class Cat:

    # 定义"吃"方法
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建“猫“对象
tom = Cat()

tom.eat()
tom.drink()

print(tom)

address = id(tom)  # 十六进制转换为十进制
print("%d" % address)
