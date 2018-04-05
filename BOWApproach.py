from collections import Counter
import sys

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.feature_extraction import DictVectorizer
import sklearn.cluster.k_means_
from sklearn.cluster.k_means_ import KMeans, MiniBatchKMeans
from sklearn.cluster import SpectralClustering, DBSCAN
from sklearn. decomposition import PCA, KernelPCA, SparsePCA, TruncatedSVD, IncrementalPCA
import numpy as np

def readFile(words, path):
    with open(path, 'r', encoding='utf8') as f:
        rval = []
        for idx in range(len(words)):
            rval.append(Counter())

        lines = f.readlines()
        for line in lines:
            tokens = line.split()

            for i, word in enumerate(words):
                if(word in tokens):
                    counter = rval[i]
                    idx = tokens.index(word)
                    #bow of 5 (2 on the left | 2 on the right)
                    bow = tokens[idx-2:idx+3]
                    for w in bow:
                        counter[w] += 1
                    #print(tokens)
                    #print(tokens[idx-2:idx+3])
                    #print()

                    #use the whole line as bow
                    #rval.append(line.strip())
                    #continue
        return rval

#list of bow's, each containing one of the fruits
#fruitsCorpus = readFile(['apple', 'banana', 'oranges', 'watermelons'], 'resources/corpora/OpenSubtitles/small/combined2')
#workCorpus = readFile(['office', 'home', 'building', 'house'], 'resources/corpora/OpenSubtitles/small/combined2')
corpus = readFile(['apple', 'banana', 'oranges', 'watermelons', 'office', 'home', 'building', 'house'], 'resources/corpora/OpenSubtitles/small/combined2')
#'office', 'home', 'building', 'house'
#'chair', 'table', 'door', 'floor'
#'apple', 'banana', 'oranges', 'watermelons'
#'sister', 'brother', 'father', 'mother'
#'nose', 'eyes', 'mouth', 'face'

#reduce the amount of the work corpus since its causing memory issues otherwise
#workCorpus = workCorpus[0:8000]

#print(len(fruitsCorpus))
#print(len(workCorpus))
#print(fruitsCorpus)
#print(workCorpus)

#sys.exit()

#corpus = np.append(fruitsCorpus, workCorpus)

vectorizer = DictVectorizer()
#vectorizer = CountVectorizer()
#vectorizer = TfidfVectorizer()
#vectorizer = HashingVectorizer()
X = vectorizer.fit_transform(corpus).toarray()
print('X...')
print(X)
#print(vectorizer.get_feature_names())

#Xfruits = vectorizer.transform(fruitsCorpus).toarray()
#Xwork = vectorizer.transform(workCorpus).toarray()

#Xcombined = np.vstack((Xfruits, Xwork))

#pca = PCA()
pca = KernelPCA()
#pca = SparsePCA()
#pca = TruncatedSVD()
#pca = IncrementalPCA()
X = pca.fit_transform(X)


kmeans = KMeans(n_clusters=2, init='random').fit(X)
#f = SpectralClustering(n_clusters=2).fit_predict(X)
#f = DBSCAN().fit_predict(X)

#kmeansMinibatch = MiniBatchKMeans(n_clusters=2, init='random').fit(Xcombined)
#labels = kmeans.labels_
#np.set_printoptions(threshold=np.nan)
#print('labels', labels)

f = kmeans.predict(X)
print(f)
print('contains number one x times: ', list(f).count(1))
print('contains number zero x times: ', list(f).count(0))

print('----------------------')

#w = kmeans.predict(Xwork)
#print(w)
#print('contains number one x times: ', list(w).count(1))
#print('contains number zero x times: ', list(w).count(0))