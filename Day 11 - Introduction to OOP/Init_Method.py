"""
初始化方法
"""


class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')


# 由于初始化方法除了self之外还有两个参数
# 所以调用Student类的构造器创建对象时要传入这两个参数
stu1 = Student('刘尚远', 20)
stu2 = Student('Bobby', 21)
stu1.study('Python程序设计')  # 骆昊正在学习Python程序设计
stu2.play()  # 王大锤正在玩游戏
