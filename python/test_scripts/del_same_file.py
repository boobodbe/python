import os

def delete_files_with_suffix(folder_path, suffix):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file.endswith(suffix):
            os.remove(file_path)
            print("{} --> 已删除。".format(file_path))
        elif os.path.isdir(file_path):
            delete_files_with_suffix(file_path, suffix)

# 双引号里面填需要处理的文件夹路径，其他地方都不要动
folder_path = "D:/temp/课件和资料/b/"  
a = ["(1).pdf",  "(1).jpg", "(1).chm", "(1).docx", "(1).zip",  "(1).exe", "(1).doc", "(1).doc", "(1).xmind", "(1).txt", "(1).c", "(1).gz", "(1).xz", "(1).7z", "(1).rar", "(2).zip"]
for i in a:
    suffix = i
    delete_files_with_suffix(folder_path, suffix)
