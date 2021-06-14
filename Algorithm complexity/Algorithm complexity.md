# Algorithm complexity

[TOC]

## 1 Mater Theorem 主定理方法

![image-20210611104748538](D:\yinbo.qiao\Study Folder\github\NLP_crash_course\Algorithm complexity\Algorithm complexity.assets\image-20210611104748538.png)

该定理用于推理递推关系式，只一个非常经典的计算时间复杂度的定理。

## 2 Fibonanci number 斐波那契数

问题描述：序列依次为1，1，2，3，5，8，13，21，......，怎么求出序列中第N个数？

```python
def fib(n):
	if n<3:
        return 1
    return f(n-1)+f(n-2)
```

**2.1 计算该算法的时间复杂度？**

通过递归树计算时间复杂度

![](D:\yinbo.qiao\Study Folder\github\NLP_crash_course\Algorithm complexity\Algorithm complexity.assets\2021-06-11_11-08-22.jpg)

第一层需要一个操作，第二层需要两次操作，第三层需要4次操作，往下依次8次，16次... ，很容易观察出，该递归算法满足$O(2^n)$时间复杂度。

**通过堆栈计算空间复杂度**，空间复杂度为$O(n)$。

**2.2 优化斐波那契数的计算**

动态规划，通过保存中间计算结果以化简算法的时间复杂度操作。

```python
# 通过维护一个数组来保存计算的中间结果
import numpy as np
def fib(n):
    tmp = np.zeros(n)
    tmp[0]=1
    tmp[1]=1
    for i in range(2,n):
        tmp[i] = tmp[i-2]+tmp[i-1]
    return tmp[n-1]
# O(N) O(2^N)
# 还可以进一步优化，只利用三个内存单元
def fib(n):
    c = 0
    a,b=1,1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    return c
```

**2.3 斐波那契数O(1)解决方案**

通过公式的方法来计算，那么如何计算得到斐波那契数的递推公式呢？

![](D:\yinbo.qiao\Study Folder\github\NLP_crash_course\Algorithm complexity\Algorithm complexity.assets\2021-06-11_11-49-51.jpg)

还可以通过其他多种手段得到想同的答案，在此不做赘述，可以参考网络资源。

## 3 P vs NP vs NP Hard vs NP Complete

详细的解释可以参考知乎文章[P问题、NP问题、NP-Complete和NP-Hard问题](https://zhuanlan.zhihu.com/p/73953567)。

**P问题**：可以在多项式时间内得到解决的问题，有多项式时间复杂度算法，可以快速求解。

**NP问题**：不确定是否存在多项式时间复杂度的算法解决该问题，但是可以在多项式时间复杂度内验证给出的答案是否是正确的。

所以现在学术界正在对NP？=P进行研究，也就是说是否存在能在多项式时间内验证正确的问题，一定存在多项式时间的算法呢？等待未来的突破吧。

**NP-Hard问题**：时间复杂度极高，指数时间复杂度，当数据量极大时，该问题使用当前的计算机无法解决。

**NP-Complete问题：**俗称NPC问题，这类问题是为了探索NP问题而提出的，为了寻找到NP问题的最大规约问题，从而去解决NP问题。比如，用二元一次方程组解一元一次方程。

![](D:\yinbo.qiao\Study Folder\github\NLP_crash_course\Algorithm complexity\Algorithm complexity.assets\2021-06-11_14-58-37.jpg)

![](D:\yinbo.qiao\Study Folder\github\NLP_crash_course\Algorithm complexity\Algorithm complexity.assets\2021-06-11_15-03-34.jpg)



## 4 算法文章

[算法设计与分析（1）——插入排序过程、时间复杂度分析](https://zhuanlan.zhihu.com/p/270615311)

[算法设计与分析（2）——冒泡排序算法过程、正确性证明及改进](https://zhuanlan.zhihu.com/p/270964384)

[算法设计与分析（3）——快速排序过程、时间复杂度分析及改进](https://zhuanlan.zhihu.com/p/271106295)

[算法设计与分析（4）——归并排序过程、时间复杂度分析及改进](https://zhuanlan.zhihu.com/p/271686548)

[算法设计与分析（5）——基于键值比较排序算法下边界](https://zhuanlan.zhihu.com/p/271738235)

[算法设计与分析（6）——堆排序过程、时间复杂度分析及改进](https://zhuanlan.zhihu.com/p/277387363)

[算法分析与设计（7）——基数排序、计数排序时间复杂度分析](https://zhuanlan.zhihu.com/p/296231019)

[算法设计与分析（8）——最大元选择问题](https://zhuanlan.zhihu.com/p/331714729)

[算法设计与分析（9）——次大元选择](https://zhuanlan.zhihu.com/p/333306647)

[算法设计与分析（10）——中间元选择](https://zhuanlan.zhihu.com/p/339371932)

[算法设计与分析（11）——动态集及红黑树](https://zhuanlan.zhihu.com/p/344759326)

[算法设计与分析（12）——等价类表示](https://zhuanlan.zhihu.com/p/352783144)