"""
工资结算系统
某公司有三种类型的员工，分别是部门经理、程序员和销售员。需要设计一个工资结算系统
根据提供的员工信息来计算员工的月薪。其中，部门经理的月薪是固定15000元
程序员按工作时间（以小时为单位）支付月薪，每小时200元
销售员的月薪由1800元底薪加上销售额5%的提成两部分构成
"""

# 通过对上述需求的分析，可以看出部门经理、程序员、销售员都是员工，有相同的属性和行为
# 那么我们可以先设计一个名为Employee的父类，再通过继承的方式从这个父类派生出部门经理、程序员和销售员三个子类
# 后续的代码不会创建Employee 类的对象，因为我们需要的是具体的员工对象，所以这个类可以设计成专门用于继承的抽象类
# Python中没有定义抽象类的关键字，但是可以通过abc模块中名为ABCMeta 的元类来定义抽象类
# 关于元类的知识，后面的课程中会有专门的讲解，这里不用太纠结这个概念，记住用法即可


from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05


emps = [
    Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'),
    Programmer('荀彧'), Salesman('吕布'), Programmer('张辽'),
]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')