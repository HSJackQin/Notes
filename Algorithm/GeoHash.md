# GeoHash编码

## GeoHash存在的问题

- 1. 采用Peano编码（N字形编码）会产生编码相似，但距离突变的情况。**解决方案**：在根据编码匹配距离之后，再进行实际距离的计算

- 2. 规则分块带来的一个问题是相邻的点可能分属不同的区块（这重问题发生在边界处）。**解决方案**：匹配时不只匹配当前块，还匹配相邻的8块

- 3. GeoHash适合对点数据进行索引，而对于线，面数据的索引采用R树更有优势

## 参考文献

[1] https://www.cnblogs.com/LBSer/p/3310455.html
