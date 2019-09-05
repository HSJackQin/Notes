## Linux文本处理

---

主要介绍不一定最常用，但却是最强大的Linux文本处理工具（三驾马车）—— `sed`, `grep`, `awk`

#### 1、`awk`

##### 基本知识

- 分隔符

- 命令写法

##### 实际应用

用Leetcode上面的一道题举例子：

> 192.统计词频
> 假设word.txt内容如下：
> the day is sunny the the
> the sunny is is
> 你的脚本应当输出：
> the 4
> is 3
> sunny 2
> day 1

利用`awk`可以方便的用一行`bash`命令完成任务：

首先，通过`cat`和`|`管道操作符将txt文件传递给`awk`，然后通过`awk`实现`for`循环将每个单词作为键，以字典`count`的形式对单词进行计数，然后再利用`for`循环将字典的键值对输出，最后利用`sort`进行排序。

```bash
 cat word.txt | awk '{for(i=1;i<=NF;i++){count[$i]++}} END {for(k in count){print k" "count[k]}}' | sort -rnk 2
 ```

 当然，也可以不用字典，利用`Linux`自带的`uniq`命令完成对词的计数：

 ```bash
 cat word.txt | awk '{for(i=1;i<=NF;i++)print $i}' | sort | uniq -c | sort -rn | awk '{print $2,$1}'
 ```

for more information, please use `man` and `google`.


#### `grep`

##### 基本知识

基本用法：根据规则搜索并打印出匹配到的行

##### 实际应用

#### `sed`

##### 基本知识

基本用法：利用脚本来处理（按行）文本文件

##### 实际应用

（1）说一个文本处理中简单的例子：

现在我有个待处理文本(制表符分隔)：

 ```vim
 1^I2^I3^I4$
 asdf^Ighjk^Iqwer^Ityui$
 qwer^Ityui^Iuiop^Iqwer$
 ```

我需要取出除第1行之外的每行第二个字段，并存入文件。需要的命令是：

 ```bash
cat file.txt | sed '1d' | awk -F \t '{print $2}' > res.txt
 ```


（2）这里以一个解析kml文件为例，展示这三个命令配合使用的效果。

假设我们有一个kml格式的文件，大致长这个样子：

 ```html
 <?xml version="1.0" encoding="utf-8"?>
<kml>
<Document>
    <name>XXX</name>
    <Style id="ytrhshdhjwwr">
        <Pair>
            <style>#hflhl</style>
        </Pair>
    </Style>
    <Folder>
        <name></name>
        <open>1</open>
        <Placemark>
            <name>石家庄市</name>
            <Cost>
                <longitude>100</longitude>
                <latitude>20</latitude>
                <direct>45</derect>
                <title>省会</title>
                <range>4567</range>
            </Cost>
        </Placemark>
        <Placemark>
            <name>北京市</name>
            <Cost>
                <longitude>110</longitude>
                <latitude>23</latitude>
                <direct>45</derect>
                <title>直辖市</title>
                <range>4589</range>
            </Cost>
        </Placemark>
        <Placemark>
            <name>秦皇岛市</name>
            <Cost>
                <longitude>120</longitude>
                <latitude>25</latitude>
                <direct>45</derect>
                <title>地级市</title>
                <range>3568</range>
            </Cost>
        </Placemark>
    </Folder>
</Document>
</kml>
 ```

现在我们想提取标签< Placemark> </ Placemark>之间的内容，包括城市名，经纬度，等级等信息，该如何去做呢？

首先，由于html的标签是成对出现的，而`grep`命令的默认匹配单位是行，所以我们考虑先把这些文本转换为一行，也就是去掉每一行尾的换行符`\r\n`，

 ```bash
 cat position.kml | tr "\r\n" " "
 ```

 然后拿出我们想要的信息：

 ```bash
 .. | grep -e "<Placemark[^>]*>.*<\Placemark>"
 ```

 然后我们想要对每个< Placemark> </ Placemark>对分别做处理，这时可以重新在合适的位置（每个 < Placemark> </ Placemark>后）添加换行符，使每一行再次独立出来，

 ```bash
 .. | sed -e 's/\(<Placemark[^>]*>\)/\1\n/g' -e 's/\(<Placemark[^>]*>\)/\1\n/g'
 ```

 如果对中间环节有疑问可以重定向到文件中查看一下。独立之后我们只需要拿出我们需要的行（这里用`grep`来匹配< title>，因为< name>会带来我们不需要的行），然后再次利用`sed`去除所有的标签格式，剩下的就是我们关心的几个变量了，直接利用`awk`输出就好。

 ```bash
 .. | grep "<title" | sed -e 's/<[^>]*>//g' | awk '{print $1,$2,$3,$4,$5,$6}'
 ```

 最后得到：

 ```bash
 石家庄市 100 20 45 省会 4567
 北京市 110 23 45 直辖市 4589
 秦皇岛市 120 25 45 地级市 3568
 ```


#### `sort`

##### 基本知识

##### 实际应用

#### `xarg`

##### 基本知识

##### 实际应用

#### `find`

##### 基本知识

##### 实际应用

