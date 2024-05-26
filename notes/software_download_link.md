- Windows配置小鹤双拼方案

  - cmd

  - ```shell
      HKCU\Software\Microsoft\InputMethod\Settings\CHS /v UserDefinedDoublePinyinScheme0 /t REG_SZ /d "小鹤双拼*2*^*iuvdjhcwfg^xmlnpbksqszxkrltvyovt"
      ```

  - powershell

  - ```shell
      Set-ItemProperty -LiteralPath 'HKCU:\Software\Microsoft\InputMethod\Settings\CHS' -Name 'UserDefinedDoublePinyinScheme0' -Type String -Value '小鹤双拼*2*^*iuvdjhcwfg^xmlnpbksqszxkrltvyovt'
      ```

- windwos暂停更新，管理员方式打开cmd窗口，输入下面命令，注意其中的3000代表暂停更新的天数，可修改

    -   ```she
        reg add “HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings” /v FlightSettingsMaxPauseDays /t reg_dword /d 3000 /f
        ```

- 自用软件列表：https://docs.qq.com/sheet/DR2lSS1djZ3BUS0JB?tab=BB08J2

- 浏览器
  
  - 百分浏览器（推荐）----  添加时间：2023-12-13
  
    - 官方网站：https://www.centbrowser.cn/
  
- 压缩/解压缩软件

  - 7-zip
    - 官方网站：https://7-zip.org/download.html
  - bandizip
    - 官方网站：https://www.bandisoft.com/bandizip/
  
- windows系统优化设置
  - 卸载软件--geek
  - 官方网站：https://geekuninstaller.com/download
  - Dism++  关闭自动更新，优化配置等
  
      - 蓝奏云（10.1.1002）：https://wwsx.lanzouu.com/i2naB1jufnpe
  - Windows 轻松设置
  
      -   蓝奏云：https://wwsx.lanzouu.com/iD4zb1kd8bdc
  - Windows 实用设置工具
  
      -   蓝奏云：https://wwsx.lanzouu.com/iQTzi1lslmwb
  - FixWin 故障修复
  
      -   蓝奏云：https://wwsx.lanzouu.com/irVn81lslmuj    密码:0000
  - BleachBit  电脑垃圾一键清理
  
      -   蓝奏云：https://wwsx.lanzouu.com/ixhAR1lslmsh
  - EmptyFolderNuker – 电脑空文件夹清理
  
      -   蓝奏云：https://wwsx.lanzouu.com/i6iu91jufnuj  密码:0000
  - 飘云阁dll修复
      - 蓝奏云：https://www.lanzouw.com/iRCns1scrc3e
  
- 音视频播放器

  - mpv -- 极简音视频播放
    - 官网：https://mpv.io/installation/

  - vlc -- 音视频播放
    - 官网：https://www.videolan.org/vlc/

  - potplayer -- 全能超强播放器
    - 下载：http://potplayer.tv/?lang=zh_CN
    - 国内网址：http://www.potplayercn.com/download
    - 官网：https://potplayer.daum.net/ 
  
- 截图/OCR软件

  - PixPin -- 支持长截图和OCR

    - 官网：https://pixpinapp.com/

  - Snipaste -- 不支持长图
      - 官网：https://zh.snipaste.com/
  - Umi-OCR -- 支持离线OCR识别

    - 官网：https://github.com/hiroi-sora/Umi-OCR/releases/tag/release/2.0.1

    - 蓝奏云：https://hiroi-sora.lanzoul.com/s/umi-ocr
  
- 文本编辑器

  - Typora -- markdown文档编辑器

      - 官方网址：https://typoraio.cn/releases/all
      - 蓝奏云（1.4.8和1.2.4激活版）：https://wwsx.lanzouu.com/i287p1jpou1g
      - 蓝奏云（v0.9.6免费版）：https://www.lanzouw.com/ifHya1scsxdg
  - MarkText -- markdown文本编辑器，可替代Typora

      - 官方网址：https://www.marktext.cc/

      - github网址：https://github.com/marktext/marktext/releases
  - Sublime Text -- 代码编辑器

      - 官网：https://www.sublimetext.com/
      - 蓝奏云：https://wwsx.lanzouu.com/itdEE0ihcs0b  密码:0000
  - Notepad3 -- 可替代电脑自带记事本

      - 官网：https://github.com/rizonesoft/Notepad3/releases
  - eDiary日记
      - 官网：http://www.haoxg.net/
  - windows日记本
      - 蓝奏云：https://www.lanzouw.com/iY78C1scr47a
  - xournalpp-1.2.1-windows-写字板
      - 蓝奏云：https://www.lanzouw.com/iTzOx1scr87e
  - 几何画板5.06.exe
      - 蓝奏云：https://www.lanzouw.com/iPEFw1scrayd
  
- 文档阅读、图片查看
  - 稻壳阅读器 DocBox 绿色版 支持多种格式的文档阅读
      - 蓝奏云：https://wwsx.lanzouu.com/ixoZ61gq3d1g  密码:0000
  - PDF阅读器 超级轻量 单文件 SumatraPDF
      - 官方网站：https://www.sumatrapdfreader.org/download-free-pdf-viewer
  - 看图软件  2345看图王--纯净无广告版本
    - 蓝奏云：https://wwsx.lanzouu.com/iYb1b15iyuyd
  - Universal Viewer
      - 官网：http://www.uvviewsoft.com/uviewer/
  
- 下载器 -- 加速下载

  - IDM -- 超强下载器

    - 蓝奏云（6.41.3版本）：https://wwsx.lanzouu.com/iDSuM1gtcoyh  密码:0000

    - 俄罗斯大神版-持续更新：https://why666.lanzoub.com/b01o6beah  密码：6666
  - 迅雷 -- 极简破解版
    - 蓝奏云：https://wwsx.lanzouu.com/iDaq015iyxmj
  - qBittorrent_4.6.3.10_64bit_Portable.7z
      - 蓝奏云：https://www.lanzouw.com/iNBYI1scgnub
  - B站视频下载工具  DownKyi-1.5.9
    - 百度云盘：https://pan.baidu.com/s/1HEeLwwL6-v93Uye2s_VNIg?pwd=0000   提取码: 0000 
  
- 编译器、解释器
  - MinGW -- c/c++编译器
      - 官方网址：https://www.mingw-w64.org/downloads/

      - 其他下载网址：https://www.fosshub.com/MinGW.html
  - python 解释器
      - 官网：https://www.python.org/downloads/

      - 华为镜像：https://mirrors.huaweicloud.com/python/
  - JetBrains系列软件激活脚本
      - 蓝奏云（推荐）：https://wwsx.lanzouu.com/iFFhB1jpb8ch
      - 激活码网站：https://3.jetbra.in/
  - Git  -- 版本控制软件

      - 官方网站：https://git-scm.com/downloads

      - 清华大学镜像站：https://mirrors.tuna.tsinghua.edu.cn/
  
- 虚拟机

  - VMware 
  	- 果核下载：https://www.ghxi.com/?s=VMware

  - Virtual Box -- 免费
    - 官网：https://www.virtualbox.org/wiki/Downloads
  
- office办公软件

  - WPS破解版
    - 果核下载：https://www.ghxi.com/?s=wps

  - Office Tool Plus -- 可以快速部署微软office并激活

    - 官网：https://otp.landian.vip/zh-cn/

    - 蓝奏云（8.2.8.0版）：https://wwsx.lanzouu.com/iWBOU0wpgx5c

  - Heu_Kms 激活Windows和office
      - 蓝奏云：https://wwsx.lanzouu.com/iVNKQ1lss0gf
  
- Listary -- 文件搜索、应用启动快捷工具

  - 官方网站：https://www.listary.com/download
  
- 电脑剪切板增强工具 -- Ditto
    - 官方网站：https://ditto-cp.sourceforge.io/
    
- FileGee -- 多端文件同步工具 -- 支持同步到百度网盘 -- 免费版就够用

    - 官方网站：https://cn.filegee.com/download.html
    
- ToDesk -- 远程桌面控制
  - 官网：https://www.todesk.com/download.html
  
- 电子书格式转化 -- pdg、uvz等格式转为pdf  –图书需要的工具
  - 蓝奏云：https://wwsx.lanzouu.com/igJOB1da2rla
  
- BitWarden -- 密码管理器
  - 官网：https://bitwarden.com/pricing/
  
- Pointofix – 屏幕标记工具
  - 官网：https://www.pointofix.de/download.php
  
- 批量修改文件名
    - 蓝奏云：https://wwsx.lanzouu.com/ikKdp1lssiob
    
- BaiduPCS-Go-百度网盘命令行
    - gitee：https://gitee.com/morphyhu/BaiduPCS-Go
    - 蓝奏云：https://www.lanzouw.com/i1RrX1scgk2f
    
- Bandicam v5.3.3.1895 x64 中文pj便携版-录屏
    - 蓝奏云：https://www.lanzouw.com/iz8us1scglfe
    
- validrive-u盘检测工具.exe
    - 蓝奏云：https://www.lanzouw.com/i3j0V1scgo4b
    
- WizTree – 文件结构
    - 官网：https://diskanalyzer.com/download

-   auto_push_to_gitee.exe - 自动上传文件到gitee
    -   蓝奏云：https://www.lanzouw.com/iKIvT1ttuo7g
