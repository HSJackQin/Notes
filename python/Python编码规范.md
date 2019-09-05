## Python编码规范

### 1、书写规范

#### 行长度

- 尽量不要用分号将两条命令放在同一行

- 每行不超过80字符

- 不要使用反斜杠`\`连接行，可以使用`([{`进行隐式连接

   ```python
   if (width == 0 and height == 0 and
       color == 'red' and emphasis == 'strong'):
    # See details at
    # http://www.example.com/us/developer/documentation/api/content/v2.0/csv_file_name_extension_full_specification.html
    ```

#### 空行

- 顶级定义（函数或类定义）之间空两行，其余空一行

#### Shebang

- 只有在类Unix系统中，被直接执行的文件中才有必要加入`#!`，例如`#!/usr/bin/python3`

#### 注释



#### **参考**

[1] https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/

[2] Python最佳实践指南2018 https://learnku.com/docs/python-guide/2018/writing-style/3261

