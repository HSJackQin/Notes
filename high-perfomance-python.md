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