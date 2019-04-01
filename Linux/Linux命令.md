# Linux常用命令总结

参考：[Vamei's Blog](http://www.cnblogs.com/vamei/archive/2012/10/10/2718229.html)

### 启动

- 控制台

`Ctrl + Alt + F2`:进入控制台；Linux默认有7个控制台，F7一般对应图形界面；


### （1）Shell

- Shell用户和Unix系统之间的交互，Shell命令分如下三种
  - Shell内建函数(built-in function)
  - 可执行文件(executable file)
  - 别名(alias)



- 命令查询
  - `whatis`：一句话介绍命令
  - `man`：返回命令的帮助文档
  - `info`：返回更加详细的文档
  - `which`：查找命令位置
  - `type`：了解命令类型

- `alias`：重命名，例如`alias gita = "git add"`
- `Ctrl + C`：中止运行中的命令
- `Ctrl + Z`：暂停运行中的命令

- 文件操作
  - `ls`
  

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

- find

`find path -name filename`:在指定目录下查找名字符合的文件
`find path -name filename -exec command {} \`:对匹配的文件执行该参数所给出的shell命令

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

- sort

sort命令常用参数：

`-f`:忽略大小写
`-r`:反向排序
`-t`:指定分隔符，默认是Tab
`-k`:指定以哪列进行排序

`sort -k 1 filename`:以第一列为标准进行排序
`sort -t ":" -k 2 -r filename`:以':'为分隔符，按照第二列的反序进行排序

- uniq

`uniq`命令用于去除排序过的文件中的重复行，要求重复行必须相邻，因此常和`sort`一起使用

常用参数：

`-i`:忽略大小写
`-c`:计数
`-u`:只显示唯一的行

- nano

Linux默认的文本编辑器（另外一个是vi）

