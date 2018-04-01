from sklearn.feature_extraction.text import CountVectorizer
import sklearn.cluster.k_means_
from sklearn.cluster.k_means_ import KMeans, MiniBatchKMeans
import numpy as np

def readFile(words, path):
    with open(path, 'r', encoding='utf8') as f:
        rval = []
        lines = f.readlines()
        for line in lines:
            tokens = line.split()

            for word in words:
                if(word in tokens):
                    rval.append(line.strip())
                    continue
        return rval


fruitsCorpus = readFile(['apple', 'banana', 'oranges', 'watermelons', 'grapefruit', 'mangoes', 'tomatoes', 'pears', 'pineapples',
    'potato', 'broccoli', 'carrot', 'tomato', 'spinach'], 'resources/corpora/OpenSubtitles/small/xaa')
workCorpus = readFile(['office', 'home', 'building'], 'resources/corpora/OpenSubtitles/small/xaa')
corpus = fruitsCorpus + workCorpus

print(len(fruitsCorpus))
print(len(workCorpus))

vectorizer = CountVectorizer()
X = vectorizer.fit(corpus)
#print(vectorizer.get_feature_names())

print('------------------------')
Xfruits = vectorizer.transform(fruitsCorpus).toarray()
print('------------------------')
Xwork = vectorizer.transform(workCorpus).toarray()

Xcombined = np.append(Xfruits, Xwork)

#kmeans = KMeans(n_clusters=2, init='random').fit(Xcombined)
kmeansMinibatch = MiniBatchKMeans(n_clusters=2, init='random').fit(Xcombined)
#labels = kmeans.labels_
#print('labels', labels)