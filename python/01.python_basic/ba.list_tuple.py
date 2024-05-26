"""
序列是一块连续的存储空间
列表推导式

列表元素的添加：
append()  extend()  insert()  --> 不生成新列表
+尾部添加  乘法扩展  --> 生成新列表

列表删除元素的底层是：元素的拷贝
del删除：del a[2]  删除列表指定位置的元素
pop(): 删除并返回指定位置的元素，如果未指定位置则默认返回列表最后一个元素，a.pop()  a.pop(1)
remove(): 删除首次出现的指定元素，若不存在则抛出异常，a.remove(10)

列表排序：
a.sort(): 默认是升序排列，不产生新列表
a.sort(reverse = True): 降序排列
random.shuffle(a): 随机打乱
b=sorted(a): 建立新列表列表 升序
c = sorted(a, reverse = True) 降序

其他函数：
max(a): 返回最大值
min(a): 返回最小值
sun(a): 求和

元组属于不可变序列

zip(list1, list2, list3...)： 将多个列表对应位置的元素组合为元组，并返回这个zip对象

"""
import random

a= list(range(10))
b = list(range(3,15,2))
c = list(range(3,-5,-1))
d = [x*2 for x in range(5)]
e = [x for x in range(100) if x % 9 == 0]
print(e)
print(type(a))
print("--"*20)

f = [20, 40]
print(id(f))
f = f + [50]
print(id(f))
print(f)
print("--"*20)

g = [20, 30]
print(id(g))
h = [40, 50]
print(id(h))
g.extend(h)
print(id(g))
print(g)
g = g + h 
print(id(g))
print("--"*20)

i = [10, 20, 30]
i.insert(2, 100)
print(i)
print("--"*20)

j = [1, 3 ,5 ,6 ,7]
del j[2]
k = j.pop(1)
j.remove(6)
print(j, k)
print(len(j))
print("--"*20)

l = [20, 10, 30, 40]
l.sort()
print(l)
l.sort(reverse = True)
print(l)
random.shuffle(l)
print(l)
print("--"*20)

m = [2,1,4,6,5, 9]
n = sorted(m)
print(n)
o = sorted(m, reverse = True)
print(o)
print(m)
print(sum(m))
print("--"*20)

p = (1,2,3)
q = 4, 5, 6
r = (7,)
s = tuple()
t = tuple("abc")
u = tuple([8,9,0])
print(p, q, r, s, t, u)
print(p[2], p[0:2])
v = zip(p, q, u)
print(v)
print(list(v))
