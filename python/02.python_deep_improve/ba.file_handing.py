with open(r"D:\a.txt", 'w', encoding = 'utf-8') as f:
    s = "hello\n"
    f.write(s)
print('-'*30)

try:
    f = open(r"D:\a.txt", 'a')
    s = "God\n"
    f.write(s)
except BaseException as e:
    print(e)
finally:
    f.close()
# 看完13节 2024-05-27

with open(r"D:\a.txt", 'r', encoding='utf-8') as f:
    # s = f.read(1)
    # s2 = f.read()
    # print(s)
    # print("第二次读的：")
    # print(s2)
    #for line in f:
    #    print(line, end = '')
    lines = f.readlines()
    print(lines)
    lines2 = [line.rstrip()+"\t#"+str(index)+'\n' for index,line in zip(range(1,len(lines)+1),lines)]
    print(lines2)
    
with open(r"D:\a.txt", 'w', encoding = 'utf-8') as f:
    f.writelines(lines2)

# 用with打开两个资源  
with open(r"D:\aaa.jpg", 'rb') as src,open(r"D:\bbb.jpg", 'wb') as mu:
    for line in src:
        mu.write(line)

# 序列化和反序列化，用pickle模块
import pickle
with open(r"D:\b.dat", 'wb') as f:
    name = "God"
    age = 34
    score = [1,2,3]
    resume = {'name':name, 'age':age,'score':score}
    pickle.dump(resume,f)  # 序列化

with open(r"D:\b.dat", 'rb') as f:
    resume2 = pickle.load(f)  # 反序列化
    print(resume2)
print("=="*30)

# os 模块
import os
# os.system("ping baidu.com")
print(os.name)  # windows-->nt  linux-->posix
print(os.sep)  # windows-->\  linux-->/
print(repr(os.linesep))  # windows-->\r\n linux-->\n
a = '3'
print(a)
print(repr(a))  # repr可以显示数据的原始信息
# 获取文件和文件夹相关的信息
print(os.stat("ba.file_handing.py"))  # 返回当前文件的状态信息
# 关于工作目录的操作
print(os.getcwd())  # 获取当前的工作目录
os.chdir("d:")
# os.mkdir("bbbb")
# os.makedirs("moive/bood/aaa")
# os.rename("bbbb", 'dddd')
test = os.listdir("D:\image")
print(test)
print("=="*30)
# os.path模块，很重要
import os.path
path = os.getcwd()
file_list = os.listdir(path)
print(file_list)
for file_name in file_list:
    pos = file_name.rfind('.')
    if file_name[pos+1:] == 'py':
        print(file_name)
print("=="*30)
file_list2 = [file_name for file_name in os.listdir(path) if file_name.endswith(".py")]
print(file_list2)
print("=="*30)

# walk
path = os.getcwd()
list_files = os.walk(path, topdown = False)
for root,dirs,files in list_files:
    for name in files:
        print(os.path.join(root,name))
    for name in dirs:
        print(os.path.join(root,name))
print("=="*30)

# shutil模块，文件和目录的拷贝等
import shutil
shutil.copyfile("a.txt", "a_copy.txt")
# shutil.copytree("D:\image","D:\ceshi", ignore = shutil.ignore_patterns("*.jpg","*.mp4"))
print("over")
print("=="*30)
# 压缩, 还有zipfile模块
# shutil.make_archive("D:/aazip", "zip", "D:/aa")

# 递归遍历目录树结构
def my_print_file(path, level):
    child_files = os.listdir(path)
    for file in child_files:
        file_path = os.path.join(path, file)
        print("\t"*level + file_path[file_path.rfind(os.sep)+1:])
        if os.path.isdir(file_path):
            my_print_file(file_path, level+1)
my_print_file("D:/document", 0)
# 文件操作结束，2024-05-28 15：47