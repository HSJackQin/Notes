## Hadoop

### Hadoop的三大核心组件

- HDFS
- MapReduce
- Yarn

- Hadoop与其他关系型数据库管理系统的区别：

  - 计算机硬盘的发展趋势是寻址时间的提升远远赶不上传输速率的提升，因此如果数据访问模式包含大量的磁盘寻址，
  会比流数据读取模式（流数据模式主要取决于传输速度）消耗更长的时间。
  - Hadoop适合于一次写入，多次读取的数据应用场景，关系型数据库更适合持续更新的数据集。

  - 两者的另一个区别是数据集对象的结构化程度：关系型数据库主要操作结构化数据，而Hadoop对半结构化数据和非结构化数据非常有效。

- Hadoop尽量在计算节点上存储数据，以实现数据的本地快速访问。数据本地化(data locality)特性是Hadoop数据处理的核心。

### HDFS

- HDFS(Hadoop Distributed Filesystem)，以流式数据访问模式来存储超大文件。

- 特点

  - 超大文件
  - 流式数据访问
  - 商用硬件
  - 低时间延迟的数据访问：HDFS是位高数据吞吐优化的，一定程度会提高时间延迟，
  对于低延迟的访问，HBase是更好的选择
  - 大量的小文件：namenode将文件系统的元数据储存在内存，因此文件数量受限于内存容量
  - 单用户写入，且不支持任意修改文件

- 数据块

  - HDFS数据块默认大小为128MB，设置的这么大是为了最小化寻址开销

- HDFS的容错机制

- 文件系统

  - 命令行接口
  - 尽管MapReduce可以访问任何文件系统，但是处理大数据集时，还是建议选择有数据本地优化的
  分布式文件系统，如HDFS

### map/reduce

- MapReduce是一种可用于数据处理的编程模型，优势在于处理大规模数据集。

- map/reduce处理天气数据，查询每年的最高气温

  - （图）

- 数据流

  - 分片：默认128MB，与HDFS一个块大小相同

- map

  - “数据本地优化”
  - map的输出写入磁盘，而不是HDFS系统，而reduce任务输出写入HDFS保存

- reduce

  - 如果有多个reduce任务，map的输出会根据哈希函数通过键值进行分区，喂给不同的reduce

- combiner函数

  - 尽可能避免map和reduce之间的数据传输是有利的
  - map输出之后可以设置combiner，combiner的输出作为reduce的输入
  - combiner属于优化方案
  - 但combiner的具体设计要根据具体任务来定

- Hadoop Streaming
  
  - Hadoop提供了MapReduce的API，Hadoop Streaming使用Unix的标准流作为Hadoop和程序
  之间的接口，所以我们可以使用任何编程语言通过标准输入输出来写MapReduce程序。

- shuffle机制（第七章）

MapReduce确保每个reducer的输入都是按键排序的。系统执行排序、将map输出作为输入传递给reducer
的过程称为shuffle，
shuffle理解为从map产生输出到reduce笑话输入的整个过程。

shuffle是MapReduce的“心脏”，是奇迹发生的地方。

底层发生的事情以及理解后的针对性调优

### yarn

第四章

