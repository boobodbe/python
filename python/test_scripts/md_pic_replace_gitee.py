# with open("test.md", "a+") as file:
#     content = file.readlines()
#     # print(content)

# with open("test.md", 'w') as
# # print(type(content))
# num = 0
# for i in content:
#     print(i)
#     # print(type(i))
#     if './assets' in i:
#         i.replace('./assets', 'https://gitee.com/boobodbe/code/blob/master/assets')
#         num += 1
#         print("{}张图片地址修改成功！\n".format)

import re

file = input("请输入要修改文件的文件名：")
# 读取文件内容
with open(file, 'r') as f:
    content = f.read()

# 使用正则表达式替换assets为hello
# 这是上传到gitee的code仓库的图片，可以这样修改
new_content = re.sub(r'./assets', 'https://gitee.com/boobodbe/code/raw/master/assets', content)
# new_content = re.sub(r'blob', 'raw', content)

# 将新内容写入文件
with open(file, 'w') as f:
    f.write(new_content)
