class Cat:
    """定义"猫"类"""

    def __init__(self, new_name):
        print("这是一个初始化方法")

    # 定义"吃"方法
    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s要喝水" % self.name)


# 创建“猫“对象
tom = Cat("Bobby")
tom.name = "Tom"

tom.eat()
tom.drink()
print()

# 在创建一个猫对象
laze_cat = Cat("Fiamma")
laze_cat.name = "Fiamma"

laze_cat.eat()
laze_cat.drink()
