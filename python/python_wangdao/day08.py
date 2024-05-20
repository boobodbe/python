# python, day08
def aa():
	# 引用计数
	str1 = "hello"
	str2 = "hello"
	print(id(str1), id(str2))
# day08 -- p22 -- over -- 2024-05-12-23：45


def ab(name, gender=True):
	# 缺省参数
	gender_text = "boy"
	if not gender:
		gender_text = "girl"
	print("{} is a {}.\n".format(name, gender_text))

def ac(num, *args, **kwargs):
	# 可变参数 也叫 多值参数
	# 在元组前面加*就是解包，效果就是（1，2，3，4）编程1，2，3，4
	# 在字典前面加**，解包unpack
	print(num)
	print(args)
	print(kwargs)

def ad(n):
	if n == 1 or n ==2:
		return n
	return ad(n-1)+ad(n-2)
# day08 -- p23 -- over -- 2024-05-13-23：06


if __name__ == "__main__":
	print("{} kinds of step.".format(ad(5)))
