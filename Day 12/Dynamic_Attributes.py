"""
动态属性
在运行时可以改变其结构的语言，例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化
对象的方法其实本质上也是对象的属性，如果给对象发送一个无法接收的消息，引发的异常仍然是AttributeError
"""


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('刘尚远', 20)
# 为Student对象动态添加sex属性
stu.sex = '男'
print(stu.name, stu.sex, stu.age)


"""
如果不希望在使用对象时动态的为对象添加属性，可以使用Python的__slots__魔法
对于Student类来说，可以在类中指定__slots__ = ('name', 'age')
这样Student类的对象只能有name和age属性，如果想动态添加其他属性将会引发异常
"""


class Student:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('刘尚远', 20)
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'
