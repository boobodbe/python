### 用户管理

修改ubuntu的root密码：sudo passwd root

给ubuntu添加一个新用户：sudo useradd -m username -s /bin/bash

ctrl a 光标回到行首，ctrl e 光标回到尾部

删除已经存在的用户：sudo userdel -r username

如果是进程正在使用：用exit退出进程，再删除

查看系统中存在的用户：cat /etc/passwd

### 目录切换

ls -l 可以列出所有目录和文件

rwx分别是读、写、执行，分为三组，第一组是当前用户，第二组是当前用户组，第三组是其他用户

windows 将文件从 ubuntu 拷贝到 本机

scp tutu@192.168.56.101:~/day2/day2_kk.file .