# 把csv文件按固定格式输出为txt文本

import csv
import os

'''
def read_csv(path):
    # 读取csv文件中的内容，但是需要传入文件名，必须是当前文件目录内,
    # 没用到这个函数，优化后的在下面，smoke_sort
    with open(path, mode='r', encoding='gbk') as csvfile:
        reader = csv.reader(csvfile)
        # header = next(reader)  # 跳过表头
        for row in reader:
            print('{} -- {} ** {:.2f} -- {:.2f}'.format(row[0], int(row[5]), float(row[2]), float(row[3])))  
            # str类型，需要转化成需要的int和float类型
        with open('output.txt', 'w', encoding='utf-8') as out:
            for row in reader:
                out.write('{} -- {} ** {:.2f} -- {:.2f}'.format(row[0], int(row[5]), float(row[2]), float(row[3])))
'''


def smoke_sort(path):
    # 用来对csv文件按照某一列升序排序
    # 这个函数是用来输出详细数据
    # 打开CSV文件
    with open('D:\\temp\\{}'.format(path), 'r', encoding='gbk') as file:
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
    print('\n----------复制下面的数据----------\n')
    # print(path[6:8], '号 --', smoke_num, '条', money)
    print("{}号 -- {}条 -- {:.2f}".format(path[6:8], smoke_num, money))

    # 打印列表里面的数据
    for i in a:
        print(i)
    print("总 ---- {}条 ---- {:.2f}".format(smoke_num, money))
    print("\n未收到")
    # print('\n\n')
    # print("下面是简化版本。\n")
    # print("{}号 -- {}条 -- {:.2f}".format(path[6:8], smoke_num, money))
    # for j in b:
    #     print(j)
    print('\n----------复制上面的数据----------\n')

    del_file = "D:\\temp\\" + path #当代码和要删除的文件不在同一个文件夹时，必须使用绝对路径
    os.remove(del_file)#删除文件
    print("已经删除：",del_file)


if __name__ == '__main__':
    files = os.listdir("D:\\temp\\")
    # print(files)
    csv_file = [file for file in files if file.endswith('.csv')]  # 返回的是列表对象
    for file_path in csv_file:  # 循环一次即可
        smoke_sort(file_path)
        # file_path = str(item)
        break
    # read_csv(file_path)
    # smoke_sort(file_path)
