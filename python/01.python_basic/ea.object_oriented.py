"""
面向对象（Object oriented programming, OOP）
面向对象包含了面向过程。宏观面向对象，微观面向过程。
类是图纸，是模板。对象是类的具体实例。对象就是这个模具造出的饼干。
属性是静态数据（变量）：例如: id age name
方法是动态行为（函数）：例如: 学习 踢球
类也称为类对象，类的实例也称为实例对象。
类名：首字母大写，多个单词用“驼峰原则”。
函数放在类里面就叫方法。
__init__构造方法和__new__方法
初始化对象，需要定义构造函数__init__()方法。构造方法用于执行“实例对象的初始化工作”，即对象创建后，初始化当前对象的相关属性，无返回值。
构造方法是负责初始化（装修），不是建对象（房子）。
__new__()方法：用于创建对象，一般无需重新定义该方法。
实例属性是从属于实例对象的属性，也称为“实例变量”。
其他操作：
dir(obj)可以获得对象的所有属性、方法。
obj.__dict__对象的属性字典
pass，空语句
isinstance(对象.类型)，判断对象是不是指定类型

类属性是从属于类对象的属性，也称为类变量。
类方法是从属于类对象的方法。类方法通过装饰器@classmethod来定义。格式如下：
@classmethod
def 类方法名(cls [,形参列表])：
    方法体
类方法中不能访问实例属性和实例方法。

静态方法通过装饰器@staticmethod来定义，格式如下：
@staticmethod
def 静态方法名([形参列表])：
    方法体
调用静态方法格式：类名.静态方法名(参数列表)
静态方法中不能访问实例属性和实例方法

__del__()被称为“析构方法”，用于实现对象被销毁时所需的操作。
python实现自动垃圾回收，当对象没有被引用时（引用计数为0），由垃圾回收器调用__del__().

call方法和可调用对象
python中，凡是可以将（）直接应用到自身并执行，都称为可调用对象。
定义了__call__()的对象，称为“可调用对象”，即该对象可以像函数一样被调用。

python中方法没有重载。
如果在类体中定义了多个重名的方法，只有最后一个方法有效。
python中不能出现重名的方法。
"""
class Student:
    def __init__(self,name,score):
        self.name = name  # 实例属性
        self.score = score
    
    def say_score(self):
        print("{}'s score is {}.".format(self.name, self.score))

s1 = Student("God", 99)
print(s1.name, s1.score)
s1.say_score()
s2 = Student("Mike", 77)
s2.age = 10  # 只有s2有这个属性
print(s2.name, s2.score, s2.age)
print(dir(s2))
print(s2.__dict__)
print(isinstance(s2, Student))
print('-'*30)

print(type(Student))
print(id(Student))
print(Student)
print('-'*30)

class c1():
    company = "BaiDu"
    
    def __init__(self, name):
        self.name = name
    
    @classmethod  # 类方法 
    def printCompany(cls):
        print(cls.company)
        
    @staticmethod
    def aa(a,b):
        print("{}+{}={}".format(a,b,a+b))
        
c1.printCompany()
c1.aa(1,2)
print('-'*30)

def f1():
    print("f1\n")
    
f1()
print(dir(f1))    

class Car:
    def __call__(self, age, money):
        print("call方法")
        print("车龄：{}，金额：{}。".format(age,money))
        
c = Car()
c(3,20000)
print('-'*30)

# 测试方法的动态性
class Person:
    def work(self):
        print("work hard.")
        
def play_game(s):
    print("play game.")

def work2(s):
    print("work hard, study hard.")
    
Person.play = play_game
Person.work = work2

p = Person()
p.play()
p.work()
print('-'*30)

# 测试私有属性，私有方法，方法的本质也是属性
class Employee:
    __company = 'BaiDu'
    
    def __work(self):
        print("work hard, earn manoy.")
    
print(dir(Employee))
print(Employee._Employee__company)
a = Employee()
a._Employee__work()

# 学完python的私有属性和私有方法，阿里视频看完第100节。
# 2024-05-26 15：49