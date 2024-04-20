# 自动同步文件到gitee，参考https://zhuanlan.zhihu.com/p/405819680?utm_id=0

from time import ctime, time
from os import system


def get_time():
	"""获取当前时间"""
	return ctime()

def create_git_order(time):
	"""生成git指令并执行"""
	order_arr = ["git add *", "git commit -m" + '"'+time+'"', "git push"]  # gitee提交出错
	# order_arr = ["git add *", "git commit -m" + '"'+time+'"', "git push origin master"]
	for order in order_arr:
		system(order)

def put_file(time):
	"""在桌面放置文件"""
	file = open(r"D:\temp\git_push_time.txt", "a")
	file.write(time + "完成提交\n")

if __name__ == "__main__":
	data = get_time()
	create_git_order(data)
	put_file(data)