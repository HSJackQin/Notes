# -*- coding: utf-8 -*-

# Python日常使用的一些操作笔记

# （1）Python列表统计词频
list1 = ['a', 'b', 'c', 'a', 'c', 'c']
from collections import Counter
Counter(list1)

# 当然，你也可以利用list自带的list.count写出循环来实现，或者
# 利用字典来实现
'''
for ...:
    list1.count('c')
'''

# (2) Python与各种格式的文件的交互
### <1> Python读取xlsx
import xlrd
from openpyxl import load_workbook

work_book = load_workbook(str(PATH) + file_name)
sheets = work_book.get_sheet_names()
book = work_book.get_sheet_by_name(sheets[0])
rows = book.rows
lines = []
for row in rows:
    lines.append([col.value for col in row])

'''
列表/字典生成式等等，进一步的提取操作
'''

### <2> Python读取txt等文本文件
with open('file_path', 'r') as f:
    data = f.readlines()
    for line in data: #逐行读取
        tmp = line.strip().split()
        '''
        '''
"""如果需要一次性读取，可以使用f.read()，然后借助eval，如下"""
with open('file path') as f:
    data = eval(f.read())

"""推荐使用 with open 而不是 f = open, ..., f.close()"""

### <3> Python写入文件
with open('new file path', 'w') as f:
    f.write(str('something'))

"""python写入excel文件"""
# 用到再查，或者pandas作为中间步骤比较方便

"""python读写json文件"""
import json
#字符串操作
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data) #python->json
data = json.loads(json_str) #json->python
#文件操作
# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)


### <4> Python标准输入输出



# (3) Python引入模块以及sys添加path


# （4）Python各种标准写法

# （5）Python工程项目书写规范

# （6）Python常用第三方库

# 1. Numpy
# 2. Pandas
# 3. Scipy
# 4. scikit-learn



