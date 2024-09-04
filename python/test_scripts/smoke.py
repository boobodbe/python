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
    b = []  # 设置一个空列表，保存伪造数据，每条烟成本加几块钱
    # 打印排序后的数据
    for row in sorted_data:
        if int(row[5]) == 0:
            continue
        smoke_num += int(row[5])
        money = money + float(row[5]) * float(row[2])
        a.append('{} -- {} ** {:.2f} -- {:.2f}'.format(row[0][:-1], int(row[5]), float(row[2]), float(row[3])))
        # b.append('{} -- {:.2f}'.format(row[0][:-1], float(row[3])))
        b.append('{} -- {} ** {:.2f} -- {:.2f}'.format(row[0][:-1], int(row[5]), float(row[2]) + 3.0, float(row[3])))
        # 上一行3.0代表成本每条加3.0，可修改

    with open('smoke.txt', 'w') as f:
        print("{}号 -- {}条 -- {:.2f}\n".format(file_name[6:8], smoke_num, money))
        f.write("{}号 -- {}条 -- {:.2f}\n".format(file_name[6:8], smoke_num, money))

    # 打印列表里面的数据
        for i in a:            
            f.write(i)
            f.write('\n')
        f.write("总 ---- {}条 ---- {:.2f}\n".format(smoke_num, money))
        f.write("\n未收到\n\n")
    
    
        for j in b:
            f.write(j)
            f.write('\n')
            
        os.remove(path)


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