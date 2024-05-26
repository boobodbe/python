def caesar_cipher(plaintext, shift):
	ciphertext = ""
	for char in plaintext:
		if char.isalpha():
			char_num = ord(char.lower()) - ord('a')
			shifted_num = (char_num + shift) % 26
			shifted_char = chr(shifted_num + ord('a'))
			if char.isupper():
				shifted_char = shifted_char.upper()
			ciphertext += shifted_char
		else:
			ciphertext += char
	return ciphertext

def caesar_cipher_decrypt(ciphertext, max_shift):
	for shift in range(max_shift + 1):
		plaintext = ""
		for char in ciphertext:
			if char.isalpha():
				char_num = ord(char.lower()) - ord('a')
				shifted_num = (char_num - shift) % 26
				shifted_char = chr(shifted_num + ord('a'))
				if char.isupper():
					shifted_char = shifted_char.upper()
				plaintext += shifted_char
			else:
				plaintext += char
		print(f"Shift = {shift}: {plaintext}")

while True:
	print('\n'+"**"*20)
	do_what = input("请输入您想要进行什么操作，\n进行凯撒加密，请输入1\n进行凯撒解密，请输入2\n退出程序，请输入0\n等待您的输入：")
	if do_what == "1":
		# 获取用户输入的明文和偏移量
		print("**"*20)
		plaintext = input("请输入明文：")
		shift = int(input("请输入偏移量："))
		# 调用函数进行加密
		ciphertext = caesar_cipher(plaintext, shift)
		# 输出加密后的密文
		print("加密后的密文为：", ciphertext)
		print("**"*20+'\n')
	elif do_what == "2":
		print("**"*20)
		ciphertext = input("请输入密文：")
		max_shift = 25
		caesar_cipher_decrypt(ciphertext, max_shift)
		print("**"*20)
	elif do_what == "0":
		print("程序结束！！！")
		print("**"*20)
		break
	else:
		print("输入出错，请重新输入！！！")
		print("**"*20)
