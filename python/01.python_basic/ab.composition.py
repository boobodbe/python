"""
对象：
一切皆对象：
标识identity
类型type
值value

对象的本质：一个内存块，拥有特定的值，支持特定类型的相关操作

引用：
在python中，变量也称为：对象的引用（reference）。变量存储的就是对象的地址。

变量位于：栈内存
对象位于：堆内存

python是动态类型的语言
不需要声明类型

python标识符命名规则：
模块和包名：全小写字母
函数名：全小写字母，多个单词之间用下划线隔开
类名：首字母大写，采用驼峰原则
常量名：全大写字母，多个单词使用下划线隔开

python中最基本的4中数据类型：
整形
浮点型
bool型
字符串
"""

a = "abcdefghijklmn\
opqrstuvwxyz"
print(a)

a= 3
print(a)
print(id(a))
print(type(a))

b = "我爱你"
print(b)
print(id(b))
print(type(b))

MAX_AGE = 120
print(MAX_AGE)
MAX_AGE = 200
print(MAX_AGE)

x = y = 100
print(x, y)

# 系列解包赋值
a, b = 1, 2
a, b = b, a 
print(a,b)

a= 10/5
print(a)
b = 9%4
print(b)

# 使用divmod()可以同时拿到商和余数，返回元组
print(divmod(13, 4))