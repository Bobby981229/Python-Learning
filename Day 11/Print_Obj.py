"""
打印对象
在类中放置__repr__魔术方法
该方法返回的字符串就是用print函数打印对象的时候会显示的内容
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

    def __repr__(self):
        return f'{self.name}: {self.age}'


stu1 = Student('刘尚远', 21)
print(stu1)  # 刘尚远: 21
students = [stu1, Student('Bobby', 20), Student('Jack', 19)]  # 将参数存进列表中
print(students)  # [刘尚远: 21, Bobby: 20, Jack: 19]
