## Shell编程

### Shell脚本的运行

1. `source filename`：这个命令是在当前shell中执行脚本，并且改动直接在当前环境生效；不需要文件的可执行权限；

1. `./filename`：打开一个子shell来读取并执行脚本命令，在执行前必须赋给文件可执行权限；

1. `bash filename` / `sh filename`：这两个命令和上一个一样，都是新建当前shell的子shell执行脚本命令，（其实全称是`/bin/bash filename` or `/bin/sh filename`），且不需要文件具有可执行权限；

&emsp;只有第一个命令会在当前shell环境中生效，因此一般常用于修改初始化文件后执行。

@import "pics/1.png"

### Shell变量

#### 1、变量的合法命名
  - `var=hahaha`：定义变量时名字前不加`$`，且**等号前后不能有空格**
  - 命名只能使用英文，数字和下划线，不能以数字开头
  - 不能有空格，标点，bash关键字（`help`查看保留关键字）

#### 2、使用变量
  - 变量名前加`$`，最好给变量添加`{}`来声明边界，如`echo ${var}`

#### 3、只读变量
  - 变量完成定义后可以声明为只读变量，`readonly var`，只读变量不能被修改

#### 4、删除变量
  - `unset var`命令可以删除变量，但不能删除只读变量

#### 5、变量类型
  - 局部变量：尽在当前shell实例中有效
  - 环境变量：所有程序均可访问
  - shell变量：shell程序设置的特殊变量

#### 6、字符串
  - 单引号
    - 单引号里的任何字符都会原样输出，单引号字符中的变量是无效的
    - 单引号中转义字符也是无效的，但可以用成对单引号来拼接字串
  - 双引号
    - 双引号里可以有变量
    - 转义字符有效
  - 无引号
  - 拼接字符串
@import "pics/2.png"

  - 获取长度、提取字串、查找子串等操作
@import "pics/3.png"

#### 7、数组

  - 定义：
  ```bash
  array_name=(v1 v2 v3 v4)
  array_name=(
  v1
  v2
  v3
  v4
  )
  array_name[0]=v1
  array_name[3]=v4
  ```

  - 读取

  ```bash
  value=${array_name[n]} #按照下标索引元素
  echo ${array_name[@]} #获取数组所有元素
  length=${#array_name[@]} #获取数组元素个数
  length=${#array_name[n]} #获取单个元素长度
  ```

#### 8、注释

  - 单行
  - 多行注释
  ```bash
  :<<EOF
  注释内容
  EOF
  # 或者
  :<<!
  注释内容
  !
  ```

