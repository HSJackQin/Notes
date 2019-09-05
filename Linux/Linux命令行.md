## Linux Command Line

---

这是《The Linux Command Line》的阅读笔记，结合自己日常应用的水平，摘录出对自己较有价值的一些命令行指令，随时补充更新。

### Shell文件操作

### 输入输出重定向

### 



### Linux的环境配置

`cp`命令会默默覆盖掉已经存在的同名文件。

- `nano`

  `Ctrl x`: 退出
  `Ctrl o`: 保存

- 修改`~/.bashrc`配置
  
  `cp ~/.bashrc ~/.bashrc.bak`
  `vim ~/.bashrc`
  `source ~/.bashrc`

- 添加环境变量

  `PATH=$PATH:$HOME/yourpath`
  `export PATH`: 让此shell的子进程可以使用PATH变量的内容

### VIM

坑回头再填。

- 连接行

- 查找和替换

  - 全局查找和替换

- 文件间操作

- 推荐学习资料：

  [learn-vim](https://github.com/dofy/learn-vim)

### 包管理

### 存储

### 网络



### 基本工具

包括正则表达式，grep等命令，管道啥的




### Shell脚本

