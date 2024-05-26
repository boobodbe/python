# import os

# for file in os.listdir():
#     if "Financial_Times" in file:
#         new_file = file.replace("Financial_Times", "103")
#         os.rename(file, new_file)
import os

file_list = [
    "Barron's -- 101",
    "Bloomberg_Businessweek -- 102",
    "Financial_Times -- 103",
    "Foreign_Affairs -- 104",
    "National_Geographic -- 105",
    "New_Scientist -- 106",
    "Photography_Week -- 107",
    "Readers_Digest -- 108",
    "Science -- 109",
    "The_Economist -- 110",
    "The_Guardian -- 111",
    "The_Times -- 112",
    "The_New_Yorker -- 113",
    "The_Wall_Street_Journal -- 114",
    "The_Washington_Post -- 115",
    "Time -- 116",
    "USA_TODAY -- 117"
]

def magazine2num():
    for file in os.listdir():
        for item in file_list:
            old_name, new_name = item.split(" -- ")
            if old_name in file:
                os.rename(file, file.replace(old_name, new_name))
                break

def num2magazine():
    for file in os.listdir():
        for item in file_list:
            new_name, old_name = item.split(" -- ")
            if old_name in file:
                os.rename(file, file.replace(old_name, new_name))
                break

print("杂志重命名脚本，输入你想干嘛\n")
print("英文名转为数字，请输入1\n")
print("数字转为英文名，请输入2\n")
num = int(input("等待您的输入："))
if(num == 1):
    magazine2num()
elif(num == 2):
    num2magazine()
else:
    print("傻逼，输错了\n")
