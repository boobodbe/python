#encoding = utf-8
"""
API(Application Programming Interface)应用程序编程接口，是用于描述模块中提供的函数和类的功能描述和使用方式描述。

"""
import salary

print(salary.__name__)
print(salary.__doc__)
print(salary.yearSalary.__doc__)
print("=="*30)

import math as m

print(id(m))
print(type(m))
print(m.sqrt(4))
print("=="*30)

from math import sqrt,sin
print(sqrt(81))
# 模块完成  2024-05-28  17：14