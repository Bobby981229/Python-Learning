"""
可见性和属性装饰器
对象的属性通常会被设置为私有（private）或受保护（protected）的成员，简单的说就是不允许直接访问这些属性
对象的方法通常都是公开的（public），因为公开的方法是对象能够接受的消息，也是对象暴露给外界的调用接口，这就是所谓的访问可见性
可以通过给对象属性名添加前缀下划线的方式来说明属性的访问可见性， 可以用__name表示一个私有属性，_name表示一个受保护属性
"""


# __name表示一个私有属性，_name表示一个受保护属性
class Student:
    # 初始化
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('Bobby', 20)
stu.study('Python程序设计')
# print(stu.__name)
print(stu._Student__name, stu._Student__age)
