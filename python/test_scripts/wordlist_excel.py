# 用于将一个txt文档单词表，按照每行十个单词导入到excel中
import openpyxl
import os

def fenge():
    with open('input.txt', 'r', encoding = 'utf-8') as f:
        lines = f.readlines()

    result = []
    for line in lines:
        word = line.split(' ')[0]
        result.append(word)

    with open('output.txt', 'w') as f:
        for word in result:
            f.write(word + '\n')

def daoruexcel():

    # 读取txt文件内容
    with open('output.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    # 将内容分割成单词列表
    words = content.split()

    # 创建一个新的Excel工作簿
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # 将单词列表按照每行10个单词的要求分组
    for i in range(0, len(words), 10):
        sheet.append(words[i:i+10])

    # 保存Excel文件
    workbook.save('output.xlsx')

daoruexcel()