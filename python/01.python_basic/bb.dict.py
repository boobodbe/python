"""
字典是无序可变序列
键是任意的不可变数据，值可以是任意数据

字典元素的访问：
a['name']：可以获得值，若键不存在，则抛出异常
a.get('name')：指定键不存在返回None，也可以设定键不存在返回的对象，a.get('gender', '一个男人')
a.items()：列出所有键值对
a.keys(): 列出所有的键
a.values(): 列出所有的值
a.update(b): 将字典b中的所有键值对添加到a上
del(a['name']): 删除指定的键值对
a.clear(): 清空字典
a.pop(): 删除指定的键值对，并返回对应的值
a.popitem(): 随机删除和返回键值对

序列解包：
可以用于元组、字典、列表
a,b,c = s  s是一个字典的话，返回的是键
a,b,c = s.values()  字典返回值
a,b,c = s.items()  返回键值对

集合是无序可变，元素不能重复。底层是用字典实现，保留了字典中的键对象，因此是不能重复且唯一的。
并集：a|b  or  a.union(b)
交集：a&b  or  a.intersection(b)
差集：a-b  or  a.difference(b)

python的序列部分结束，2024-5-25-16：28
"""
a = {"name":'god', "age":18, "job":'waiter'}
b = ['name', 'age', 'job']
c = ['god', 18, 'teacher']
d = dict(zip(b,c))
print(a)
print(d)
e = a.get('name')
f = a.get('gender', 'a people')
g = a['name']
print(e, f, g)
h = a.items()
i = a.keys()
j = a.values()
print(h)
print(i)
print(j)
print(len(a))
print("name" in a)
print("--"*20)

a["address"] = "beijing"
a["age"] = 30
print(a)
k = {'name':'good', 'money':1000, 'gender':'male'}
a.update(k)
# a.clear()
del(a['name'])
print(a)
nianling = a.pop('age')
print(nianling, a)
print(a.popitem())
print(a)
print("--"*20)

l = {"name":'god', "age":18, "job":'waiter'}
name, age, job = l.items()
print(name, age, job)
print("--"*20)

m = {'name':'aa', 'age':18, 'salary':3000, 'city':'citya'}
n = {'name':'bb', 'age':16, 'salary':2000, 'city':'cityc'}
o = {'name':'cc', 'age':15, 'salary':7000, 'city':'cityg'}
p = [m,n,o]
print(p)
print(p[1])
print("--"*20)

a = {1,2,4}
a.add(3)
print(a)
b = [1,3,5,6]
print(set(b))
a.remove(1)
print("a: ", a)
b = set(b)
print("b: ", b)
print("a|b: ", a|b)
print("a&b: ", a&b)
print("a-b: ", a-b)
