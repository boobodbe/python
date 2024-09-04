#import tkinter
#from tkinter import filedialog
import csv
import os
 

def smoke_sort(path):
    # 用来对csv文件按照某一列升序排序
    # 这个函数是用来输出详细数据
    # 打开CSV文件
    file_name = path.split('\\')[-1]
    # with open('D:\\temp\\{}'.format(path), 'r', encoding='gbk') as file:
    with open(path, 'r', encoding='gbk') as file:
        # 创建CSV读取器对象
        reader = csv.reader(file)
        # 跳过表头行，提示header未使用，换成reader试试看
        header = next(reader)
        # reader = next(reader)
        # 将数据存储到列表中
        data = list(reader)
        # 按照指定列进行排序，例如按照第二列（索引为1）进行升序排序，提示row在外部使用过，换成lie试试
        sorted_data = sorted(data, key=lambda row: float(row[3]))
        # sorted_data = sorted(data, key=lambda lie: float(lie[3]))

    smoke_num = 0  # 统计订购量
    money = 0  # 统计总金额
    a = []  # 设置一个空列表，保存每条数据
    b = []  # 设置一个空列表，保存简单数据
    # 打印排序后的数据
    for row in sorted_data:
        # print(row)  # 列表格式
        # 跳过订购量为0的烟
        if int(row[5]) == 0:
            continue
        # 统计订购总量
        smoke_num += int(row[5])
        # 统计订购总金额
        money = money + float(row[5]) * float(row[2])
        # print('{} -- {} ** {:.2f} -- {:.2f}'.format(row[0][:-1], int(row[5]), float(row[2]), float(row[3])))
        a.append('{} -- {} ** {:.2f} -- {:.2f}'.format(row[0][:-1], int(row[5]), float(row[2]), float(row[3])))
    # print(path, type(path))  # 打印文件名
        b.append('{} -- {:.2f}'.format(row[0][:-1], float(row[3])))
    # print(path, type(path))
    with open('smoke.txt', 'w') as f:
    # print('\n----------复制下面的数据----------\n')
    # print(path[6:8], '号 --', smoke_num, '条', money)
    # print("{}号 -- {}条 -- {:.2f}".format(path[6:8], smoke_num, money))
    # print("{}号 -- {}条 -- {:.2f}".format(path[6:8], smoke_num, money))
    # print("{}号 -- {}条 -- {:.2f}".format(file_name[6:8], smoke_num, money))
        print("{}号 -- {}条 -- {:.2f}\n".format(file_name[6:8], smoke_num, money))
        f.write("{}号 -- {}条 -- {:.2f}\n".format(file_name[6:8], smoke_num, money))

    # 打印列表里面的数据
        for i in a:
            # print(i)
            f.write(i)
            f.write('\n')
        # print("总 ---- {}条 ---- {:.2f}".format(smoke_num, money))
        f.write("总 ---- {}条 ---- {:.2f}\n".format(smoke_num, money))
    # print("\n未收到")
        f.write("\n未收到")
    # print('\n\n')
    # print("下面是简化版本。\n")
    # print("{}号 -- {}条 -- {:.2f}".format(path[6:8], smoke_num, money))
    # for j in b:
    #     print(j)
    # print('\n----------复制上面的数据----------\n')

    # del_file = "D:\\temp\\" + path #当代码和要删除的文件不在同一个文件夹时，必须使用绝对路径
    # os.remove(del_file)#删除文件
    os.remove(path)
    # print("已经删除原文件：",path)


# 2024年8月18号修改，删除选择文件的图形化界面
"""
root = tkinter.Tk()

root.title('路径选择')
max_w, max_h = root.maxsize()
root.geometry(f'500x300+{int((max_w - 500) / 2)}+{int((max_h - 300) / 2)}')  # 居中显示
root.resizable(width=False, height=False)
 
# 标签组件
label = tkinter.Label(root, text='选择目录：', font=('华文彩云', 15))
label.place(x=50, y=100)
 
# 输入框控件
entry_text = tkinter.StringVar()
entry = tkinter.Entry(root, textvariable=entry_text, font=('FangSong', 10), width=30, state='readonly')
entry.place(x=150, y=105)

# 按钮控件
def get_path():
    # 注意以下列出的方法都是返回字符串而不是数据流
    # 返回一个字符串，且只能获取文件夹路径，不能获取文件的路径。
    # path = filedialog.askdirectory(title='请选择一个目录')
 
    # 返回一个字符串，可以获取到任意文件的路径。
    path = filedialog.askopenfilename(title='请选择文件')
 
    # 生成保存文件的对话框， 选择的是一个文件而不是一个文件夹，返回一个字符串。
    # path = filedialog.asksaveasfilename(title='请输入保存的路径')
 
    entry_text.set(path)
    # print("选好的路径：", path)  # 输出选好的路径
    # print("格式化路径：", path.replace('/', '\\\\'))
    csv_file = path.replace('/', '\\\\')  # 拿到文件路径
    # print(csv_file, type(csv_file), csv_file.split('\\\\')[-1])  # D:\\temp\\20240313113955.csv <class 'str'> 20240313113955.csv
    smoke_sort(csv_file)


button = tkinter.Button(root, text='选择路径', command=get_path)
button.place(x=400, y=95)

root.mainloop()
"""

# os.system('pause')
# input('Press <Enter>')

def get_csv_files(path):
    csv_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(root, file))
    return csv_files

d_drive_temp_folder = "D:\\temp"
csv_files_paths = get_csv_files(d_drive_temp_folder)
for i in csv_files_paths:
    smoke_sort(i)
    break

os.system(f'start {"smoke.txt"}')
os.system('pause')
os.remove("smoke.txt")
os.system("exit")