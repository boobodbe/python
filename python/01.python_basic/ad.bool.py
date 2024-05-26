"""
整数缓存：
命令行模式下，只存比较小的整数，范围为[-5,256]。底层用数组实现
文件模式下，所有数字都会被缓存，范围是无穷。[-5,256]用数组实现，其他数字用链表实现
"""

a = 10<20 and 50<100
print(a)

b = 200
c = 20 < b < 500
d = 20<b and b<500
print(c)
print(d)

e = 0b1101
f = 0b1001
c = e&f 
print(bin(c))
print(3<<2)
print(20>>2)

g = 3
h = 4
print(g+h)
print(str(g)+str(h))
print("I love you!  "*1000)

i = 257
j = 257
print(id(i))
print(id(j))
print(i is j)
