"""
控制语句 

列表推导式，很重要

如果目标不变，总有完成的一天。
如果目标总变，永远没有完成的一天。
"""
import turtle
print("Hello World\n")
num = 8
if num<10:
    print("小于10的整数：", num)
if 3:
    print("ok\n")
a = [1,2]
if a:
    print(a)
#b = int(input("please input a num:"))
b = 3
if b<0:
    print("This is a num<0")
elif b==0:
    print("This is 0.\n")
else:
    print("This is a num>0\n")
print(b if b < 0 else "this is a num>0")
# if while 都很熟悉了，视频跳过
num = 0
while num<=10:
    print(num)
    num += 1
print("end\n")
a = 1
sum = 0
while a<=100:
    sum += a
    a += 1
print("1+...+100= ", sum)
for x in (1,2,3):
    print(x*10)
for x in "hello":
    print(x)
sum = 0
for i in range(1,101):
    sum += i
print("1+...+100 = ", sum)
sum = 0
for i in range(1, 101, 2):
    sum += i
print("1+3+5+...+99 = ", sum)
sum = 0
for i in range(2, 101, 2):
    sum += i
print("2+4+6+...+100 = ", sum)    
for i in range(5):
    for j in range(5):
        print(i, end = '\t')
    print()
for i in range(1,10):
    for j in range(1,i+1):
        print("{} * {} = {}".format(j, i, i*j), end = '\t')
    print()
a = 1
while True:
    print(a,end='\t')
    a += 1
    if a==10:
        break
print('\n')
name = ('aa', 'bb', 'cc', 'dd')
age = (12, 23 ,45, 4)
jobs = ('asdf', 'afasdf', 'adfcv', 'asdfasd', 'a')
for name,age,job in zip(name, age, jobs):
    print("{}--{}--{}\n".format(name,age,job))
a = [x for x in range(1,5)]
print(a)
b = [x for x in range(1,20) if x % 5 == 0]    
print(b)
my_text = "  i love you you are a good girl. you are the best girl."
char_count = {c:my_text.count(c) for c in my_text}
print(char_count)
p = turtle.Pen()
p.width(4)
p.speed(10)
mycolor = ('red', 'green', 'orange', 'blue')
for i in range(1, 5):
    p.color(mycolor[i%4])
    p.circle(i*10)
    p.penup()
    p.goto(0, -i*10)
    p.pendown()

turtle.done()

# 控制语句结束，2024-05-26  00：04