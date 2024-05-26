"""
字符串的本质是：字符序列
python不支持单字符，单字符也作为字符串
字符串不可变

使用内置函数ord()可以把字符转换为unicode码
使用内置函数chr()可以把十进制数转换成对应的字符

三个单引号括起来的内容可以保留原格式打印

replace()，不改变原值，二十创建一个新的值

字符串切片操作：slice
格式：[起始偏移量start：终止偏移量end：步长step]

split()分割和join()合并
split()可以按指定分隔符将字符串分割成多个子字符串，默认按空格分割
join()用于将一系列子字符串连接起来

字符串驻留机制：常量字符串只保留一份。

去除首尾信息：
strip()：去除首尾指定信息。lstrip()可以去除字符串左边指定信息，rstrip()可以去除字符串右边指定信息

格式排版：
center()，ljust()，rjust()

特征判断方法：
isalnum()  判断是否为字母或数字
isalpha()  判断是否只由字母构成
isdigit()  判断是否只由数字构成
isspace()  判断是否为空白字符
isupper()  判断是否为大写字母
islower()  判断是否为小写字母

格式化：.format()

可变字符串：
python中字符串属于不可变对象，不支持原地修改。
如果确实需要原地修改字符串，可以使用io.StringIO对象或array模块
"""

print(ord("a"))
print(chr(66))

a = '''
I
	Love
		python
				！
'''
print(a)

b = '我在学python'
print(b)
print(len(b))

c = 'i\n love\n you'
print(c)

d = "ni\thao\tma"
print(d)

name = input("please input your name:")
print("your name:", name)

e = 'hello god you are a good girl'
print(e)
e = e.replace("good", "nice")
print(e)
print(e[4])
print(e[::2])

b = e.split()
print(b)

c = '*'.join(b)
print(c)

d = "我相信芙菲是我的狗，当然这并不是真的。芙菲是只狗。我是个小孩。我们在一起玩得很开心。只是恰巧她住在我们家而已。这段经历影响了日后我对于感情的看法：你并不拥有你所爱的人。"
print(len(d))
print(d.startswith("我"))
print(d.endswith("。"))
print(d.find("狗"))
print(d.rfind("狗"))
print(d.count("我"))
print(d.isalnum())  # 判断是否全是字母和数字

e = 'god'
print(e.center(10, ' '))

import io 
f = "youareagoodgirl"
fio = io.StringIO(f)
print(fio)
print(fio.getvalue())
fio.seek(3)
fio.write("***")
print(fio.getvalue())

# 01、python入门 章节二.基本概念 完成 2024 - 05 - 24 - 16：32