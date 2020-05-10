"""
面向对象编程 - 类
面向对象编程：把一组数据和处理数据的方法组成对象，把行为相同的对象归纳为类，通过封装隐藏对象的内部细节，
通过继承实现类的特化和泛化，通过多态实现基于对象类型的动态分派。
类是对象的蓝图和模板，对象是类的实例
"""


# 定义类 - 使用class关键字加上类名来定义类
class Student:

    def study(self, course_name):
        print(f'学生正在学习{course_name}.')

    def play(self):
        print(f'学生正在玩游戏.')


# 创建和使用对象 - 使用构造器语法来创建对象
stu1 = Student()
stu2 = Student()
print(stu1)  # <__main__.Student object at 0x10ad5ac50>
print(stu2)  # <__main__.Student object at 0x10ad5acd0>
print(hex(id(stu1)), hex(id(stu2)))  # 0x10ad5ac50 0x10ad5acd0
print()


# 调用对象的方法
# 通过“类.方法”调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法，点前面的对象就是接收消息的对象，只需要传入第二个参数
stu1.study('Python程序设计')             # 学生正在学习Python程序设计.
print()

Student.play(stu2)    # 学生正在玩游戏.
stu2.play()           # 学生正在玩游戏.
