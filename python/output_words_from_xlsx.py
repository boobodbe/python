import pandas as pd

def get_words():
    # 读取Excel文件中名为"打开记录"的工作表
    df = pd.read_excel('plan.xlsx', sheet_name='Words')
    # 筛选出第一列等于1的行
    filtered_rows = df[df.iloc[:, 5] == 1]
    # 获取第二列的值
    second_column_values = filtered_rows.iloc[:, 1].tolist()
    # 将结果保存到txt文档
    with open('output.txt', 'w') as f:
        for value in second_column_values:
            f.write(str(value) + '\n')

def get_riji():
    # 读取Excel文件中名为"april"的工作表
    df = pd.read_excel('plan.xlsx', sheet_name='april')
    with open('riji.txt', 'w') as f:
        for index, row in df.iterrows():
            date = row['日期'].strftime('%Y-%m-%d')
            # print(date, type(date))
            week = row['星期']
            info = str(row['kk']).replace("<<", "\t").replace(">>", "\n")
            # print(info, type(info))
            # break
            f.write(f"{date} ---- {week}\n{info}\n")

while True:
    do_what = input("输入你要干嘛\n输出不会的单词，请按1\n输出日记，请按2\n退出请按0\n等待您的输入：")
    if do_what == '1':
        get_words()
    elif do_what == '2':
        get_riji()
    elif do_what == '0':
        break
    else:
        print("出错，重输！！！\n")
