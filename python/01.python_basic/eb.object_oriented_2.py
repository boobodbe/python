"""
@property装饰器 -- 有点难理解，不懂
可以将一个方法的调用方式变成“属性调用”。
主要用于处理属性的读操作、写操作。

面向对象的三大特征：封装（隐藏）、继承、多态

super()可以获得父类的定义。

多态：同一个方法的调用，不同对象行为完全不同。
多态是方法的多态，属性没有多态。
多态的存在有两个必要条件：继承、方法重写。

特殊方法和运算符重载：
a+b    实际是    a.__add__(b)
"""
import copy

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    @property
    def salary(self):
        print("salary is ", self.__salary)
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        if 0<salary<1000000:
            self.__salary = salary
        else:
            print("too large")
        
emp1 = Employee("God", 3000)
emp1.salary = 50000
print(emp1.salary)
print('-'*30)

class Person:
    def __init__(self, name, age):
        print("create Person.\n")
        self.name = name
        self.age = age
        
    def say_age(self):
        print("{}'s age is {}.\n".format(self.name,self.age))
        
    def __str__(self):
        print("重写__str__方法。")
        return "name:{},age:{}".format(self.name, self.age)
        
        
class Student(Person):
    def __init__(self,name, age, score):
        # 调用父类构造方法，可以使用一下两种方法
        #Person.__init__(self,name,age)
        super(Student,self).__init__(name,age)
        print("create Student.")
        self.score = score
    
    def say_score(self):
        print("my score is ", self.score)

s1 = Student("God", 18, 90)
s1.say_age()
s1.say_score()
print(dir(s1))
print('-'*30)

obj = object()
print(dir(obj))

# 重写__str__方法
p = Person("god", 18)
print(p)
s = str(p)
print('-'*30)

# 多重继承
class A:
    def aa(self):
        print("aa")
        
class B:
    def bb(self):
        print("bb")
        
class C(A,B):
    def cc(self):
        print("cc")
        
c = C()
c.cc()
c.aa()
c.bb()
print('-'*30)

# 多态
class Animal:
    def shout(self):
        print("动物叫了一声。")

class Dog(Animal):
    def shout(self):
        print("小狗，汪汪汪。")

class Cat(Animal):
    def shout(self):
        print("小猫，喵喵喵。")
        
def animalShout(a):
    a.shout()  # 会产生多态，传入的对象不同，调用的方法不一样

animalShout(Dog())
animalShout(Cat())
print('-'*30)

#特殊方法和运算符重载
class Per:
    def __init__(self,name):
        self.name = name
       
    def __add__(self,other):
        if isinstance(other, Per):
            return "{}---{}".format(self.name, other.name)
        else:
            return "不是同类对象，不能相加"
            
    def __mul__(self, other):
        if isinstance(other,int):
            return self.name*other
        else:
            return "不是同类对象，不能相乘"

p1 = Per("God")
p2 = Per("Godd")

x = p1+p2
print(x)
print(p1*3)
print('-'*30)

#浅拷贝、深拷贝
class MobilePhone:
    def __init__(self,cpu):
        self.cpu = cpu
        
class CPU:
    def calculate(self):
        print("正在计算，算个12345！")
    
c = CPU()
m = MobilePhone(c)

print("浅拷贝....")
m2 = copy.copy(m)
print("m:", id(m))
print("m2:", id(m2))
print("m-->cpu:", id(m.cpu))
print("m2-->cpu:", id(m2.cpu))
print("\n深拷贝....")
m3 = copy.deepcopy(m)
print("m:", id(m))
print("m3:", id(m3))
print("m-->cpu:", id(m.cpu))
print("m3-->cpu:", id(m3.cpu))
print('-'*30)

#继承和组合
class Screen:
    def show(self):
        print("show a nice pic.")
        
class Phone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen

c = CPU()
s = Screen()
m = Phone(c,s)
m.cpu.calculate()
m.screen.show()
print('-'*30)

#设计模式，工厂模式
class Benz:pass
class BMW:pass
class BYD:pass

class CarFactory:
    __obj = None
    __init_flag = True
    
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj
        
    def __init__(self,name):
        if CarFactory.__init_flag:
            print("初始化第一个对象。")
            CarFactory.__init_flag = False
    
    def createCar(self, brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"

factory = CarFactory()
c1 = factory.createCar("奔驰")
c2 = factory.createCar("宝马")
print(c1)
print(c2)
print('-'*30)

# 设计模式：工厂和单例模式结合起来
factory2 = CarFactory()
print(factory)
print(factory2)

# 设计模式，单例模式
class MySingleton:
    __obj = None
    __init_flag = True
    
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj
        
    def __init__(self,name):
        if MySingleton.__init_flag:
            print("初始化第一个对象。")
            self.name = name
            MySingleton.__init_flag = False
            
a = MySingleton("aa")
print(a)
b = MySingleton("bb")
print(b)
print('-'*30)
# python入门课程学完，最后这些面向对象有点难，之后再回顾回顾。今天是2024-05-26  23：56