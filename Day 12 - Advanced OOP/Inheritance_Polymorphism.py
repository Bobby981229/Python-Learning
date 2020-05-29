"""
继承和多态
面向对象的编程语言支持在已有类的基础上创建新类，从而减少重复代码的编写
提供继承信息的类叫做父类（超类、基类），得到继承信息的类叫做子类（派生类、衍生类）
"""

# 我们定义一个学生类和一个老师类，我们会发现他们有大量的重复代码
# 而这些重复代码都是老师和学生作为人的公共属性和行为
# 我们应该先定义人类，再通过继承，从人类派生出老师类和学生类

"""
继承的语法是在定义类的时候，在类名后的圆括号中指定当前类的父类
如果定义一个类的时候没有指定它的父类是谁，那么默认的父类是object类
object类是Python中的顶级类，这也就意味着所有的类都是它的子类，要么直接继承它，要么间接继承它

在子类的初始化方法中，我们可以通过super().__init__()来调用父类初始化方法
super函数是Python内置函数中专门为获取当前对象的父类对象而设计的
"""


class Person:
    """人类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭')

    def sleep(self):
        print(f'{self.name}正在睡觉')

    def detail(self):
        print(f'{self.name}今年{self.age}岁了')


# 继承的语法是在定义类的时候，在类名后的圆括号中指定当前类的父类
class Student(Person):
    """学生类"""

    def __init__(self, name, age):
        # super(Student, self).__init__(name, age)
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')


class Teacher(Person):
    """老师类"""

    def __init__(self, name, age, title):
        # super(Teacher, self).__init__(name, age)
        super().__init__(name, age)
        self. title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}')


stu1 = Student('刘尚远', 20)
stu2 = Student('Jack', 21)
teacher = Teacher('Bobby', 45, '教授')

stu1.eat()
stu2.detail()
teacher.sleep()
print()

stu1.study('Python程序设计')
teacher.teach('Python程序设计')
