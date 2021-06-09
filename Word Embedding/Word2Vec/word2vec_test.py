from timeit import main
from gensim.models import Word2Vec
from gensim.test.utils import common_texts
from gensim.models import KeyedVectors

def train():
    # 训练和保存模型
    model = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)
    model.save("word2vec.model")
    wv = model.wv
    wv.save("word2vec.wordvectors")


def test():
    # 模型加载
    model = Word2Vec.load("word2vec.model")
    print(model.wv['computer'])
    print(model.wv[[1,2,3]])
    print(model.wv.get_index('computer'))
    print(model.wv.most_similar('computer',topn=10))
    wv = KeyedVectors.load("word2vec.wordvectors", mmap='r')
    vector = wv['computer']
    print(type(wv.vectors))
    print(wv.vectors.shape)

if __name__=="__main__":
    train()
    # test()