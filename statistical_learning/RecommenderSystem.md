### 推荐系统

#### 1、背景

为了解决信息过载的问题

#### 2、简介

- 不同于搜索引擎，推荐系统更倾向于人们没有明确的目的，它通过用户的历史行为或兴趣偏好或人口统计学特征来对用户进行推荐。

#### 3、推荐系统的分类

- 推荐系统
  - 基于内容的推荐
  - 协同过滤推荐
    - 基于内存的协同过滤
      - 基于用户的协同过滤
      - 基于项目的协同过滤
    - 基于模型的协同过滤
      - 矩阵分解
        - SVD
        - FunkSVD
        - BiasSVD
        - SVD++
      - Bayes网络
      - 基于图的模型
      - 等等
  - 基于混合模型的推荐
    - 机器学习模型常用的三种模型混合方法：Bagging，Boosting，Stacking
    - Stacking：基分类器将决策结果当作特征送入更高一层的模型中进行训练，这种堆叠的方法类似神经网络的层

#### 4、评价标准

- 评分预测任务
  - RMSE
  - MAE

-Top-N列表推荐
  - 查准率/召回率/F1-score

#### 5、推荐系统在真实生产中的问题

- 如何解决冷启动

#### 参考

https://zhuanlan.zhihu.com/p/27502172