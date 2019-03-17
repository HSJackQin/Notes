## Python高性能编程

### Chapter 1 理解高性能Python

- 基本计算机系统
  - 计算单元
    - cpu多核心并行
    - python全局解释器(GIL)
  - 储存单元
    - SSD、RAM、L1/L2缓存
  - 通信层
    - 总线
    - 不同总线和各种连接的速度不同
- 理想计算模型
- python虚拟机
  - 利用numpy实现矢量操作的优化
  - python非编译和动态性
  - GIL的影响可以通过multiprocessing（多进程而不是多线程）等避免

### Chapter 2

- 测试时间和内存的方法

### Chapter 3 列表和元组

- 列表是动态数组
  - 列表在进行增大时的操作：
     - 先创建一个拥有更多额外空间的新列表
     - 将旧列表复制进新列表
     - 删除旧列表
  - 因此列表需要超额分配空间来保证append的复杂度

- 元组是静态数组
  - 元组不支持改变大小，但可以将两个元组合并成一个新的元组而不引入额外空间
  - 与列表的append相比，针对元组的操作复杂度为O(n)，因为任意两个元组相加始终返回一个新分配的元组
  - 元组占用的空间相对较小，因此对于静态数据是一个轻量级且更好的选择
  - 元组静态特性的另一个好处体现在资源缓存上，1-20长度的元组不被使用后不会立即被系统回收空间，可以为未来的新元组预留空间
  - 初始化元组比初始化列表快很多！

### Chapter 4 字典和集合

- 字典和元组对无序数的查询都是O(1)，但其性能取决于散列函数的性能
- 元组特性是键值唯一，因此在遍历寻找不同元素的时候避免了列表实现的对比检查，性能优越
- 散列函数的选择
  - 散列函数和熵
- python对命名空间的管理
  - 可以通过对变量本地化避免python每次全局查询带来的时间消耗

**总结：** 字典和集合适用于能够被键索引的数据。散列函数对键的使用方式极大的影响数据结构的最终性能；字典也是Python的内部功能之一。

### Chapter 5 迭代器和生成器

**基础知识：** 生成器和迭代器
  - 凡是可以作用于for循环的都是可迭代对象Iterable;
  - 凡是可作为next()函数对象的都是迭代器Iterator;它们表示一个惰性计算的序列；
  - 集合数据类型可以通过iter()函数获得一个Iterator对象

- Python中for循环的解析：实际上是先生成一个迭代器，然后每一步进行迭代直到出界。
  - 因此python中for可以迭代任何可迭代对象，而不仅仅是list等
  - 通过collections的iterable判断是否可迭代
  - 内置的enumerate函数可以将list变为索引和元素同时进行迭代
- range和xrange
- 列表表达式&生成器表达式
  - 生成器的yield关键字
- 无穷数列的迭代器
- 生成器的延迟估值
- 使用迭代器的性能好于列表，因为我们避免了昂贵的append操作
- 使用迭代器有助于代码适用于多CPU等场景

### Chapter 6 矩阵和矢量计算
