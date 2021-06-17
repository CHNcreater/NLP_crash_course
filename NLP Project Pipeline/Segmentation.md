# 自然语言处理项目流程（1） NLP Project Pipeline

[TOC]
自然语言处理项目的一般流程图如下图所示，

![](.\NLP Projects Pipeline.assets\2021-06-12_10-50-20.jpg)

还有一张脑图，也能够帮助大家理解NLP整个处理流程，参考下面的图片，

![](.\NLP Projects Pipeline.assets\IMG_0105.JPG)

下面内容，针对NLP处理流程中的Pipeline逐一介绍各个部分的功能，主要算法和主要工具。

## 1 分词

分词是NLP任务的基础环节，对文本的第一步操作，是非常重要的。

### 1.1 分词工具介绍

#### 1.1.1 中文分词工具

![img](https://pic2.zhimg.com/80/v2-ec0692a9ecbc85b4a21741def16b7121_1440w.jpg)

*注：图片来自知乎@灰灰*

这里可以根据自己的需要，去选择合适自己的分词工具，一般来讲，在实验中选择jieba分词较多。本讲也立足于jieba分词来做介绍。

**开源工具**

HanLP：

[https://github.com/hankcs/HanLP](https://link.zhihu.com/?target=https%3A//github.com/hankcs/HanLP)

结巴分词：

[https://github.com/fxsjy/jieba](https://link.zhihu.com/?target=https%3A//github.com/fxsjy/jieba)

盘古分词：

[http://pangusegment.codeplex.com/](https://link.zhihu.com/?target=http%3A//pangusegment.codeplex.com/)

庖丁解牛：

[https://code.google.com/p/paoding/](https://link.zhihu.com/?target=https%3A//code.google.com/p/paoding/)

SCWS中文分词：

[http://www.xunsearch.com/scws/docs.php](https://link.zhihu.com/?target=http%3A//www.xunsearch.com/scws/docs.php)

**高校工具**

FudanNLP：

[https://github.com/FudanNLP/fnlp](https://link.zhihu.com/?target=https%3A//github.com/FudanNLP/fnlp)

LTP：

[http://www.ltp-cloud.com/document](https://link.zhihu.com/?target=http%3A//www.ltp-cloud.com/document)

THULAC：

[http://thulac.thunlp.org/](https://link.zhihu.com/?target=http%3A//thulac.thunlp.org/)

NLPIR：

[http://ictclas.nlpir.org/docs](https://link.zhihu.com/?target=http%3A//ictclas.nlpir.org/docs)

**商业服务**

BosonNLP：

[http://bosonnlp.com/dev/center](https://link.zhihu.com/?target=http%3A//bosonnlp.com/dev/center)

百度NLP：

[https://cloud.baidu.com/doc/NLP/NLP-API.html](https://link.zhihu.com/?target=https%3A//cloud.baidu.com/doc/NLP/NLP-API.html)

搜狗分词：

[http://www.sogou.com/labs/webservice/](https://link.zhihu.com/?target=http%3A//www.sogou.com/labs/webservice/)

腾讯文智：

[https://cloud.tencent.com/document/product/271/2071](https://link.zhihu.com/?target=https%3A//cloud.tencent.com/document/product/271/2071)

腾讯价格单：

[https://cloud.tencent.com/document/product/271/1140](https://link.zhihu.com/?target=https%3A//cloud.tencent.com/document/product/271/1140)

阿里云NLP：

[https://data.aliyun.com/product/nlp](https://link.zhihu.com/?target=https%3A//data.aliyun.com/product/nlp)

新浪云：

[http://www.sinacloud.com/doc/sae/p](https://link.zhihu.com/?target=http%3A//www.sinacloud.com/doc/sae/python/segment.html)

#### 1.1.2 英文分词

NLTK

SpaCy

StanfordCoreNLP

### 1.2 分词算法

分词工具有两个非常经典的底层算法，一个是前向最大匹配算法，一个是后向最大匹配算法。

#### 1.2.1 前向最大匹配算法 Forward Maximum Matching

![](.\NLP Projects Pipeline.assets\2021-06-12_11-34-23.jpg)

```python
def FMM(vocab:list, sentence:str, max_length=5):
    """
    input:
    vocab[list]: the list of vacab
	sentence[str]: the sentence
    max-length[int]: the max_length
    
    return:
    result[list]: the result of segmentation
    """
    result = []
    length = len(sentence)-max_length
    i = 0
    while i<len(sentence):
        print(i)
        windows = sentence[i:i+max_length if i+max_length<len(sentence) else len(sentence)]
        print(windows)
        while True:
            if windows in vocab:
                result.append(windows)
                i += len(windows)
                break
            else:
                if len(windows)==1:
                    result.append('[UNK]')
                    i += 1
                    break
                windows = windows[:-1]
                print(windows)
    return result
```

#### 1.2.2 后向最大匹配算法 Backwards Maximum Matching

![](.\NLP Projects Pipeline.assets\2021-06-12_11-38-18.jpg)

```python
def BMM(vocab:list, sentence:str, max_length:int=5):
    """
    input:
    vocab[list]: the list of vacab
    sentence[str]: the sentence
    max-length[int]: the max_length

    return:
    result[list]: the result of segmentation
    """
    result = []
    i = len(sentence)
    while i > 0:
        print(i)
        windows = sentence[i-max_length+1 if i-max_length+1 > 0 else 0:i]
        print(windows)
        while True:
            if windows in vocab:
                result.append(windows)
                i -= len(windows)
                break
            else:
                if len(windows)==1:
                    result.append('[UNK]')
                    i -= 1
                    break
                windows = windows[1:]
                print(windows)
    return result[::-1]
```

上面这两种最大匹配算法的缺点：

* 词典的质量影响很大，如果词典不全，则新词无法切分；如果词典过大，分词效率太慢。
* 贪心策略，局部最优。
* 不能考虑语义，因此无法解决歧义问题。

#### 1.2.3 融合语义的分词方法

借助语言模型来融合语义信息，从而得到更有质量保证的分词结果。

具体做法，就是在分词阶段，生成所有可能的分词可能作为候选分词结果，然后输入语言模型中，为每种分词结果进行打分，取得分最高的候选分词结果为最终的分词结果。

![](.\NLP Projects Pipeline.assets\2021-06-12_13-54-22.jpg)

这种语言模型，可以是基于统计的语言模型，比如我们有一个海量的文本资源库，对其中的单词词频进行统计，然后得到每个单词的频率，通过下面的方式来计算。
$$
\begin{array}
PP("我们","经常","有意见","分歧")&=P("我们")P("经常")P("有意见")P("分歧")\\
&=\frac{\#\{我们\}}{\#N}\frac{\#\{经常\}}{\#N}\frac{\#\{有意见\}}{\#N}\frac{\#\{分歧\}}{\#N}
\end{array}
$$
上面的公式，存在一个问题，就是遇到某些出现次数较少的词语，其频率非常小，连乘会导致整体的概率非常小，导致出现下溢的现象。因此，为了解决这个问题，使用$logP(word)$来解决。

这种解决方法将分词和打分选择分为了两步来解决，其最大的缺点就是效率很低。

### 1.3 维特比算法

通过维特比算法，将1.2中割裂的两步，融合到一起，维特比算法利用了DP的思想。

![](.\NLP Projects Pipeline.assets\2021-06-12_15-07-46.jpg)

```python
def Viterbi(vocab, vocab_frequency, sentence):
    """
    input:
    vocab[list]: vocabulary list
    vocab_frequency[list]: probility list
    sentence: sentence

    return:
    result[list]: the segmentation result
    """
    result = []
    assert len(vocab)==len(vocab_frequency)
    incoming = [0]*len(sentence)
    shortest = [0]*len(sentence)
    dag = {i:[] for i in range(len(sentence))}
    for item in vocab:
        index = sentence.find(item)
        dag[index+len(item)-1].append(index)
    print(dag)
    for i in range(len(sentence)):
        if i == 0:
            incoming[i] = 0
            shortest[i] = vo_fq[vocab.index(sentence[0])]
        end = dag[i]
        path_length = 100000
        for j in end:
            value = vo_fq[vocab.index(sentence[j:i+1])]
            if j == 0:
                if value < path_length:
                    path_length = value
                    incoming[i] = j
                    shortest[i] = path_length
            else:
                if value+shortest[j-1] < path_length:
                    path_length = value+shortest[j-1]
                    incoming[i] = j-1
                    shortest[i] = path_length
    print(incoming,shortest)
    start = incoming[-1]
    end = len(sentence)
    while start:
        result.append(sentence[start+1:end])
        end = start+1
        start = incoming[start]
        if start == 0:
            result.append(sentence[start:end])
            break
    return result[::-1]

if __name__ == '__main__':
    vocab = ['我们','经常','我','经','常','有','有意见','意见','分歧','意','见','分','歧']
    vo_fq = [1.6,2.3,2.3,3,3,2.3,2.3,1.6,1.6,3,3,2.3,2.3]
    sentence = '我们经常有意见分歧'
    # print(FMM(vocab=vocab,sentence=sentence,max_length=5))
    # print(BMM(vocab=vocab,sentence=sentence,max_length=5))
    print(Viterbi(vocab,vo_fq,sentence))
```

### 1.4 分词算法总结

基于匹配规则的方法——最大匹配算法

基于概率统计方法——LM，HMM，CRF

分词被认为是已经解决的问题

## 2 拼写错误纠正

在业务场景中，经常出现用户输入错误的字符的情况，这时拼写错误纠正就是一个很必要的环节。

### 2.1 编辑距离 Edit distance

如果用户写错了，某个单词，可以使用编辑距离来选择最小的相似单词，如果有多个编辑距离相同的候选单词，则还需进一步选择最适合的单词。

![](.\NLP Projects Pipeline.assets\2021-06-12_15-29-42.jpg)

上面这种方法，需要让用户输入与词典中每个单词都进行匹配，时间复杂度为O(V)，为了降低时间复杂度，提高效率，可以使用一种生成策略，即根据用户输入，生成编辑距离为1，2的字符串（因为用户不可能一点都输入不对，基本会落在编辑距离为1-2的范围之内），然后通过一些过滤条件，最终得到拼写纠正后的单词。

![](.\NLP Projects Pipeline.assets\2021-06-12_15-55-57.jpg)

### 3 词过滤

过滤停用词，过滤频率很低的词汇。

stop-words

stemming

lemmatization

可以使用jieba，NLTK等工具包实现去除停用词，提取词干等操作。