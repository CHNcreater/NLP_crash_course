# NLP_crash_course

<div align="center">
	<img src="./Images/NLP.png" alt="Natural Language Processing">
</div>



NLP速成课，NLP从入门到实践，旨在对于从事NLP相关研究和工作的同学们，分享NLP相关学习路径，学习资料以及所学所得、感想领悟。

## 算法
[算法复杂度](https://github.com/CHNcreater/NLP_crash_course/blob/main/Algorithm%20complexity/Algorithm%20complexity.md)

## 自然语言处理一般流程 NLP pipeline
### 分词
[什么是分词及几大基础算法](https://github.com/CHNcreater/NLP_crash_course/blob/main/NLP%20Project%20Pipeline/Segmentation.md)
### 文本表示
[文本表示理论](https://github.com/CHNcreater/NLP_crash_course/blob/main/NLP%20Project%20Pipeline/Word%20Representation.md)  
[一文读懂什么是word2vec](https://zhuanlan.zhihu.com/p/344474638)  
[word2vec词向量的训练](https://github.com/CHNcreater/NLP_crash_course/blob/main/Word%20Embedding/Word2Vec/word2vec_gensim.md)  


## 损失函数 Loss fuction

* 交叉熵损失函数
* [噪声对比估计 Noise Contrastive Estimation](https://github.com/CHNcreater/NLP_crash_course/blob/main/Loss%20Function/Noise%20Contrastive%20Estimation.md)

## 自然语言处理任务

### 文本分类



### 语义匹配



### 序列标注



### 文本生成



### 信息抽取



## 自然语言处理关键技术

自然语言两大分支，分别是自然语言理解（NLU）和自然语言生成（NLG）。两者存在本质的不同。

### 自然语言理解

自然语言理解自底向上的过程，重在分析，从词形（Morphology）、语法（Syntax）、语用（Pragmatics）、篇章（Discourse），到最后的语义解析（Semantics），本质问题是假设管理（Hypothesis Management）。

#### 词法分析 Morphology

三大基础任务

* 分词（word segmentation）
* 词性标注 （POS tagging/part-of-speech tagging）
* 命名实体识别（Name Entity Recognition）

#### 句法分析 Syntax

* CYK算法

#### 语义分析 Semantic



#### 自然语言理解中的难题

[自然语言理解中的难题](https://www.quora.com/What-are-the-major-open-problems-in-natural-language-understanding)

**1. Easy or mostly solved**

- **Spam detection**
- **Part of Speech Tagging** - Example*INPUT:*Profits soared at Boeing Co., easily topping forecasts on Wall Street, astheir CEO Alan Mulally announced first quarter results.*OUTPUT:*Profits/N soared/V at/P Boeing/N Co./N ,/, easily/ADV topping/V forecasts/N on/P Wall/N Street/N ,/, as/P their/POSS CEO/N Alan/N Mulally/N announced/V first/ADJ quarter/N results/N ./.*KEY: N = Noun, V = Verb, P = Preposition, Adv = Adverb*
- **Named Entity Recognition** - Example

*INPUT:*Profits soared at Boeing Co., easily topping forecasts on Wall Street, astheir CEO Alan Mulally announced first quarter results.*OUTPUT:*Profits/NA soared/NA at/NA Boeing/SC Co./CC ,/NA easily/NA topping/NA forecasts/NA on/NA Wall/SL Street/CL ,/NA as/NA their/NA CEO/NAAlan/SP Mulally/CP announced/NA first/NA quarter/NA results/NA ./NA*KEY: NA = No entity, SC = Start Company, CC = Continue Company, SL = Start Location, CL = Continue Location*

**2. Intermediate or making good progress**

- **Sentiment analysis**-Example: Best roast chicken in San Francisco! -- PositiveThe waiter ignored us for 20 minutes. -- Negative

- **Coreference resolution** - Example: "Carter told Mubarak he shouldn't run again." To solve whether "he" is related to "Carter" or "Mubarak".
- **Word sense disambiguation** - Example : I need new batteries for my mouse. - "mouse" is ambiguous here.

- **Parsing** - the basic problem of parsing sentences.
- **Machine Translation** translating sentences from one language to another, best example would be Google translate.
- **Information Translation** - to take a text as input and represent it in a structured form like a database entries.

**3. Hard or still need lot of work**

- **Text Summarization** - to take input as text document(s) and try to condense them into a summary.

- **Machine dialog system** - Example:

  User: I need a flight from New York to London, arriving at 10 pm ?

  System: What day are you leaving?

  User: Tomorrow.

  System: detects the missing information in your sentences.

#### 自然语言理解的主要困难：

主要的困难在于两点：

* 歧义：同一个字面形式有多种可能的分析结果。
* 输入信息不足：需要字面以外的信息辅助才能做出分析和预测。

### 自然语言生成

自然语言生成重在**规划**和**建构**，遵循相反的信息流，从语义到文本，通过一系列的约束条件从语义到文本进行构建。

#### 对话系统



#### 文本摘要

