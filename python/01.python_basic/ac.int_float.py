"""
整数：int
二进制：0b
八进制：0o
十二进制：0x

浮点数：float
round(value)，可以返回四舍五入的值。不改变原值，而是产生一个新的值

时间的表示：
time.time()返回当前的时间，浮点数
"""
import time

a = 0b10
print(a)
b = 0o10
print(b)
c = 0x10
print(c)
d = int(1.2)
print(d)
e = "123"
print(int(e))
f = 10**100
print(f)
g = 3.14
print(round(g))

# 增强型赋值运算，等号后面是一个整体
h = i = 3
h *= i+2  # h = h * (i+2)
print(h)

j = int(time.time())
print(j)
totalMinutes = j//60
print(totalMinutes)
totalHours = totalMinutes//60
print(totalHours)
totalDays = totalHours//24
print(totalDays)

# 学完20个视频，明天继续进行章节2的第21个视频