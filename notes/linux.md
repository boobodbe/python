### Linux用户配置命令

刚开始给系统配置root的密码：`sudo passwd root`

切换到root：`su`

 添加新用户：`sudo useradd -m username -s /bin/bash`

-   -m 是创建一个用户目录，-s 是指定解析器

配置新用户的密码：`sudo passwd username`

查看新增的用户：`cat /etc/passwd`

删除用户：`sudo userdel -r username`

光标跳转：`ctrl + A`回到开头，`ctrl + E`回到结尾。

每次切换用户是进行了压栈操作，用完要`exit` 

导出历史操作命令：`history | tail -30 > filename.txt`

-   可以指定输出后30行

导出历史操作命令：`history > filename.txt`

-   全部导出