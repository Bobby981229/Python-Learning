"""
静态方法和类方法
静态方法和类方法就是发送给类对象的消息
"""


# 举一个例子，定义一个三角形类，通过传入三条边的长度来构造三角形，并提供计算周长和面积的方法
# 计算周长和面积肯定是三角形对象的方法，这一点毫无疑问。但是在创建三角形对象时
# 传入的三条边长未必能构造出三角形，为此我们可以先写一个方法来验证给定的三条边长是否可以构成三角形
# 这种方法很显然就不是对象方法，因为在调用这个方法时三角形对象还没有创建出来
# 我们可以把这类方法设计为静态方法或类方法，也就是说这类方法不是发送给三角形对象的消息，而是发送给三角形类的消息，代码如下所示


class Triangle(object):
    """三角形类"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    # 静态方法
    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and c + a > b

    # 类方法
    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def __str__(self):
        return f'({self.a}, {self.b}, {self.c})'


t1 = Triangle(3, 4, 5)
print(t1)
print('周长:', t1.perimeter())
print('面积:', t1.area())
