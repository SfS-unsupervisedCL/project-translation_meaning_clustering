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
                    #use the whole line as bow
                    rval.append(line.strip())
                    continue
        return rval

#list of bow's, each containing one of the fruits
fruitsCorpus = readFile(['apple', 'banana', 'oranges', 'watermelons'], 'resources/corpora/OpenSubtitles/small/combined')

workCorpus = readFile(['office', 'home', 'building', 'house'], 'resources/corpora/OpenSubtitles/small/combined')

workCorpus = workCorpus[0:3000]

#print(len(fruitsCorpus))
#print(len(workCorpus))

corpus = np.append(fruitsCorpus, workCorpus)

vectorizer = CountVectorizer()
X = vectorizer.fit(corpus)
#print(vectorizer.get_feature_names())

Xfruits = vectorizer.transform(fruitsCorpus).toarray()
Xwork = vectorizer.transform(workCorpus).toarray()

Xcombined = np.vstack((Xfruits, Xwork))

kmeans = KMeans(n_clusters=2, init='random').fit(Xcombined)
#kmeansMinibatch = MiniBatchKMeans(n_clusters=2, init='random').fit(Xcombined)
#labels = kmeans.labels_
np.set_printoptions(threshold=np.nan)
#print('labels', labels)

f = kmeans.predict(Xfruits)
print(f)

print('----------------------')

w = kmeans.predict(Xwork)
print(w)