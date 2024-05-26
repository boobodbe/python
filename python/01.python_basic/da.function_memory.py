"""
函数是可重用的程序代码块。
函数是代码复用的通用机制。
函数也是对象。
print(locals()): 可以输出所有的局部变量
print(globals()): 可以输出所有的全局变量
局部变量的查询和访问速度比全局变量快，优先考虑使用

深拷贝和浅拷贝 shallow copy  deep copy 
浅拷贝：拷贝对象，但不拷贝子对象的内容，只是拷贝子对象的引用。浅拷贝相当于修改原对象。
深拷贝：拷贝对象，并且会连子对象的内存也全部（递归）拷贝，对子对象的修改不会影响原对象。深拷贝不修改原对象。

参数类型：
位置参数：需要个数和形参匹配
默认值参数：为某些参数设置默认值，这些参数在传递时可选，默认值参数放到位置参数后面
命名参数：按照形参的名称传递参数，称为命名参数，也称关键字参数
可变参数：指的是“可变数量的参数”，分两种情况
    1.*param（一个星号），将多个参数收集到一个元组对象中
    2.**param（两个星号），将多个参数收集到一个字典对象中
强制命名参数：在可变参数的函数中，如果*param在前面，后面的参数在调用的时候要强制命名

lambda表达式可以用来声明匿名函数，实在同一行中定义函数的方法
"""
import time

def add(a,b,c):
    '''实现三个数的和'''
    sum = a + b + c
    print("{} + {} + {} = {}".format(a, b, c, sum))
    return sum

def print_star(n):
    print('*'*n)
    
def avg(a,b):
    return (a+b)/2
    
def print_shape(n):
    s1 = '#'*n
    s2 = '*'*n
    return [s1,s2]
    
add(1,2,3)
print_star(5)
a = avg(10,20)
print(a)
b = print_shape(3)
print(b)
print(type(b))
print('-'*30)

b = 100
print(b)
def change():
    global b
    b = 200
    print(b)
change()   
print(b)
print('-'*30)

a = 1000
def test1():
    start = time.time()
    global a
    for i in range(100000000):
        a+=1
    end = time.time()
    print("global spend {}".format(end-start))
    
def test2():
    start = time.time()
    c = 1000
    for i in range(100000000):
        c+=1
    end = time.time()
    print("local spend {}".format(end-start))
    
c = [1,2,3]
def aa(a):
    print(a)
    a.append(4)
    print(a)

aa(c)
print(c)
print('-'*30)

def ab(a,b,*c):
    print(a,b,c)
    
ab(1,2,3,4,5,6)

def ac(a,b,**c):
    print(a,b,c)
    
ac(1,2,name='god', age = 18)
print('-'*30)

f = lambda a,b,c:a+b+c
print(f(1,2,3))
print(f)
print(id(f))
print(type(f))
g = [lambda a:a*2, lambda b:b*3, lambda c:c*4]
print(g[0](3),g[1](3),g[2](3))
# 函数完成，2024-05-26 13：03