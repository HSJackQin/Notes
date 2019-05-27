# Linux常用命令总结

## Linux安装及初始化流程（以Ubuntu 18.04为例）

### 1、镜像下载及安装

### 2、磁盘分区

1. /boot 分区256mb， 这部分是分给Linux启动内核等所需的单独空间

1. 交换分区swap，这个在虚拟机安装Linux时会用到，即指定Windows的虚拟内存大小，一般设置成当初分配给虚拟机的内存大小即可

1. 最后将剩余空间全分给 / 即可

### 3、初始化设置

1. 语言建议默认的英文环境，不需要改为中文

1. 在`setting -> display`中可以调整分辨率及缩放，打开terminal调整窗口及字体大小

1. 设置root密码：`sudo passwd`设置初始密码，之后`su root`登陆即可

1. 如果是虚拟机安装，还会提示安装VMware Tools，根据提示安装即可，`tar`将压缩文件解压后直接`sudo`执行即可，随后可以设置共享文件夹

1. apt换国内源：
  - `cd /etc/apt`
  - `sudo mv ./sources.list ./sources.list.bak`
  - `vi sources.list`
  - 将以下内容复制进去即可（注意先`lsb_release -c`获取系统版本号检查一下）

```bash
deb http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse
```

  - `sudo apt update`更新软件列表，会覆盖原来的缓存
  - `sudo apt upgrade`将本机软件更新为最新

6. 安装vim、ssh等常用工具

  - `sudo apt install vim`
  - `sudo apt install openssh-server`
    - `ssh-keygen -t rsa`：生成公私钥
  - `sudo apt install git`

7. 卸载不需要的软件

  - `sudo apt remove libreoffice-common`

8. 安装

  - 搜狗输入法:
    - 先安装fcitx：`sudo apt install fcitx`
    - `Language&support`里面添加中文
    - 官网下载linux sougou文件
    - 安装：
    ```bash
    sudo apt -f install
    sudo dpkg -i sogoupinyin_2.2.0.0108_amd64
    ```
    - 之后需要注销重启，然后在右上角keyboard图标里面设置输入法切换

  - chromium:
  
    - `sudo apt install chromium-browser`  

9. 安装anaconda及配置vscode

  - 安装Anaconda
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
    - 安装时自动添加环境变量，完成后`source .bashrc`
  
  - VS code
    - 官方安装即可
    - 遇到没有写权限问题，暂时不知道怎么解决，暴力删除`.config/Code/`文件夹即可


10. 主题及终端美化

---

参考：[Vamei's Blog](http://www.cnblogs.com/vamei/archive/2012/10/10/2718229.html)

### 启动

- 控制台

`Ctrl + Alt + F2`:进入控制台；Linux默认有7个控制台，F7一般对应图形界面；


### （1）Shell

- Shell用户和Unix系统之间的交互，Shell命令分如下三种
  - Shell内建函数(built-in function)
  - 可执行文件(executable file)
  - 别名(alias)

- 执行命令
  - `source`：在当前bash环境下读取并执行参数代表的脚本中的命令，该命令常用`.`来代替
  - `sh`：重新建立一个子shell，并执行脚本的命令
  - 区别：`sh`启动子shell，继承父shell中的环境变量，但其新建的，改变的变量不会影响父shell；但`source`是将脚本中的命令
  依次读取并在当前shell中执行，因此脚本中所有新建，改变变量的语句都会保存在当前shell中，在很多时候善用`source`命令可以
  省去重新启动bash的麻烦

- 命令查询
  - `whatis`：一句话介绍命令
  - `man`：返回命令的帮助文档
  - `info`：返回更加详细的文档
  - `which`：查找命令位置
  - `type`：了解命令类型

- `alias`：重命名，例如`alias gita="git add"`，注意等号两边不要有空格！
- `Ctrl + C`：中止运行中的命令
- `Ctrl + Z`：暂停运行中的命令

### （2）目录及文件管理

- 处理目录的常用命令
  - `mkdir [-mp]`：`-m`用于在创建目录时配置目录权限，`-p`用于递归的创建目录
  - `rmdir [-p]`：只能（递归的）删除空目录，如果目录下有文件，应该用`rm`命令删除
  - `rm [-i -rf]`：`-i`即互动模式，在删除前系统会询问是否确定，`-rf`中`-r`是递归删除，常用在目录的删除，`-f`就是force，忽略不存在的文件，直接删除不报告。**`rm -rf`一定要慎用！**
  - `cp [-i]`：`-i`是互动模式

- 文件操作
  - `ls`
  - `cat`
  - `head`
  - `tail`
  - `more/less`
  
- 下载和传输
  - scp
  - rsync
  - wget：`wget https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data`




- 进程管理

  - `ps`：查看当前正在运行的进程
  - `grep`：搜索关键字
  - `kill`：终止进程
  ```bash
  ps -aux | grep java # 查看所有进程里java相关的进程信息 
  #-aux显示所有状态
  kill -9 [PID] #强迫指定进程号的进程立刻终止
  ```

- 管道操作
```bash
cat /etc/passwd | /bin/bash | wc -l
```
这个命令找出系统有多少用户使用bash

- RE正则匹配

- grep

grep是对文件中的内容的搜索

- find

`find path -name filename`:在指定目录下查找名字符合的文件
`find path -name filename -exec command {} \`:对匹配的文件执行该参数所给出的shell命令

  - 还可以按照文件的各种属性（比如：修改时间，大小，权限，是否为空等）进行查找

- sed

sed是一种在线编辑器，它一次处理一行内容，并逐行输出到屏幕，但默认情况下文档内容并不改变。

`sed '1,$d filename'`:删除文本的第一行到最后一行

sed常用参数：

`-n`:使用安静模式，只将sed作用的行打印到屏幕上
`-i`:直接修改读取的文档内容，而不是由屏幕输出

sed常用命令：

`a`:新增，a后面可以接字串，会出现在下一行
`d`:删除，命令后面不接任何内容
`i`:插入，后面可以接字串，新内容会出现在该行的上一行
`p`:列印，通常与参数`sed -n`一起出现
`s`:取代

命令不同于参数，是在参数之后的具体命令，比如

`sed -n '1p' filename`:使用sed进行搜索
`sed '1a xxxx' filename`:在第一行后新增一行，内容是'xxxx'

- awk

awk是一种优良的文本处理的编程语言工具，功能极其强大。
它有些类似shell编程，可以提供文本处理的一系列操作。

基本的工作流程是扫描文件的每一行，查找与命令行中所给内容匹配的
模式，如果匹配，就进行下一步编程操作，没找到就继续处理下一行。

awk不仅可以通过命令行调用，还可以以shell脚本的方式运行。

`awk [-F field-separator] 'command' input-file(s)`:awk命令的一般格式；command是真正的awk命令；-F后面可以指定域分隔符

`awk 'NR==2,NR==4 {print}' filename`:显示文本的2~4行

`awk '{if(NR>=20 && NR<=30) print $1}' filename`：只查看文件的第20-30行，并打印每行的第一个字段（默认用分隔符分割，当然也可以用`-F '\t'`参数指定特定的分隔符）

- sort

sort命令常用参数：

`-f`:忽略大小写
`-r`:反向排序
`-t`:指定分隔符，默认是Tab
`-n`:按照数值的大小进行排序
`-k`:指定以哪列进行排序

`sort -k 1 filename`:以第一列为标准进行排序
`sort -t ":" -k 2 -r filename`:以':'为分隔符，按照第二列的反序进行排序
`sort -t " " -k 1.2,1.2, -nrk 3,3 facebook.txt`:来一个复杂的~ `-k 1.2, 1.2`表示只按照第一个域的第二个字符进行排序，逗号前后表示开始和结束的字符，`-nrk 3,3`表示按照第3个域的数值反序进行排序，不同参数可以连起来写

- uniq

`uniq`命令用于去除排序过的文件中的重复行，要求重复行必须相邻，因此常和`sort`一起使用

常用参数：

`-i`:忽略大小写
`-c`:计数
`-u`:只显示唯一的行

- nano

  Linux默认的文本编辑器（另外一个是vi）

- iconv

  Linux转编码命令

- nohup

  常用于将输出信息重定向

- crontab

  常用，用来定期执行程序的命令
