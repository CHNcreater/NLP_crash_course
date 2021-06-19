# Expert system and Probabilistic 专家系统与基于概率统计学习

## 前言

专家系统又称为符号主义，维基百科对专家系统的定义如下所示，

> **专家系统**是早期[人工智能](https://zh.wikipedia.org/wiki/人工智能)的一个重要分支，它可以看作是一类具有专门知识和经验的计算机智能程序系统，一般采用人工智能中的[知识表示](https://zh.wikipedia.org/wiki/知识表示)和[知识推理](https://zh.wikipedia.org/w/index.php?title=知识推理&action=edit&redlink=1)技术来模拟通常由领域专家才能解决的复杂问题。
>
> 一般来说，专家系统=[知识库](https://zh.wikipedia.org/wiki/知识库)+[推理机](https://zh.wikipedia.org/wiki/推理机)，因此专家系统也被称为基于知识的系统。一个专家系统必须具备三要素：
>
> 1. 领域专家级知识
> 2. 模拟专家思维
> 3. 达到专家级的水平

基于概率统计的方法，对于数据量的要求很大，根据数据来推测关系。

专家系统适合于没有数据或数据很少的情况，而基于概率统计学习则适合大量数据情况，给定数据，通过模型找到用户输入到结果的映射关系。

## 1 专家系统

专家系统=知识库+推理机，通过知识和推理来解决一个问题。

**专家系统的工作流**

![专家系统那么牛逼，为什么还是不靠谱_费根鲍姆](http://5b0988e595225.cdn.sohucs.com/images/20190215/771801d1adec4655b75c38bdb1aa2dea.jpeg)

**专家系统的属性：**

* 处理不确定性
* 知识的表示：比如使用图数据库来存储知识图谱等
* 可解释性：能够解释为什么得到当前的答案
* 可以做知识推理

## 2 逻辑推理

使用离散数学来解决专家系统的逻辑推理问题，构建推理引擎。

**Forward Chaining Algorithm**

![Algoritma Forward Chaining dan Backward Chaining - Skripsi Teknik  Informatika](https://2.bp.blogspot.com/-xTAMWea4hDk/Vzwr4CflHSI/AAAAAAAAAQg/zkHk_pOJ17UXFpOEY6LIQ6XIM6NcC49jACLcB/s1600/algoritma-forward-chaining-ilmu-skripsi.png)

**专家系统的缺点：**

* 需要设计大量的规则
* 需要领域专家
* 可移植性差
* 学习能力差
* 人能考虑的范围是有限的

## 3 解决难题的思路

**step1：** 找出一个类似的经典问题

**step2：** 查找一些文献，有关于该相似问题

## 总结

专家系统，现在可能被掩盖在深度学习的光环之下，这里做了非常简短的介绍，了解上面这些知识即可。