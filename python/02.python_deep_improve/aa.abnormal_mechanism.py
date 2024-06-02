"""
异常机制的本质：
当程序出现异常，程序安全的退出，处理完后继续执行的机制。
层次：
BaseException：（所有异常的父类）
    KeyBoardinterrupt
    Exception
        NameError
        ValueError
        AttributeError
        ...
    SystemExit
    GeneratorExit
try...except...else...结构
try...except...finally...结构：
finally块无论是否发生异常都会执行，通常用来释放try块中申请的资源。

python中常见异常：
python中的异常都派生自BaseException类。
SyntaxError: 语法错误
NameError: 尝试访问一个没有申明的变量
ZeroDivisionError: 除数为0错误
ValueError: 数值错误
TypeError: 类型错误
AttributeError: 访问对象的不存在的属性
IndexError: 索引越界异常
KeyError: 字典的关键字不存在

win上下文管理资源：
无论有无异常，总能释放资源
"""

try:
    print("step1")
    a = 3/1
    print("step2")
except BaseException as e:
    print("step3")
    print(e)
print("step4")
print('-'*30)

while True:
    try:
        x = int(input("input a num:"))
        print("num: ", x)
        if x==0:
            print("over!")
            break
    except BaseException as e:
        print("异常，输入的不是数字！")
        print(e)
print('-'*30)

try:
    a = input("input a num:")
    b = input("input a num:")
    c = float(a)/float(b)
    print(c)
except ZeroDivisionError:
    print("异常：不能是0")
except TypeError:
    print("必须是数字")
except BaseException as e:
    print(e)
    print(type(e))
finally:
    print("我是finally语句。")
print('-'*30)

try:
    f = open("d:/test.cpp", "r")
    content = f.readline()
    print(content)
except BaseException as e:
    print(e)
finally:
    f.close()
print("over")
print('='*30)

with open("d:/test.cpp") as f:
    for line in f:
        print(line, end='')
print('-'*30)

# tranceback模块
import traceback 
try:
    print("\nStep1!")
    num = 1/0
except:
    # traceback.print_exc()
    with open("d:/a.log", 'a') as f:
        traceback.print_exc(file=f)

# 自定义异常类
class AgeError(Exception):
    def __init__(self, errorInfo):
        self.errorInfo = errorInfo
        
    def __str__(self):
        return str(self.errorInfo)+"。年龄错误！，应该在1-150之间"

age = int(input("please input a age: "))
if age<1 or age>150:
    raise AgeError(age)
else:
    print("年龄正确：", age)
# 异常部分结束，2024-05-27  09：25