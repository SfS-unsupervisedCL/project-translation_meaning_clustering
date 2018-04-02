from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
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
                    idx = tokens.index(word)
                    #bow of 5 (2 on the left | 2 on the right)
                    rval.append(' '.join(tokens[idx-2:idx+3]))
                    #print(tokens)
                    #print(tokens[idx-2:idx+3])
                    #print()

                    #use the whole line as bow
                    #rval.append(line.strip())
                    #continue
        return rval

#list of bow's, each containing one of the fruits
fruitsCorpus = readFile(['apple', 'banana', 'oranges', 'watermelons'], 'resources/corpora/OpenSubtitles/small/combined2')

workCorpus = readFile(['office', 'home', 'building', 'house'], 'resources/corpora/OpenSubtitles/small/combined2')

#reduce the amount of the work corpus since its causing memory issues otherwise
workCorpus = workCorpus[0:8000]

#print(len(fruitsCorpus))
#print(len(workCorpus))
#print(fruitsCorpus)
#print(workCorpus)

corpus = np.append(fruitsCorpus, workCorpus)

vectorizer = CountVectorizer()
#vectorizer = TfidfVectorizer()
#vectorizer = HashingVectorizer()
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
print('contains number one x times: ', list(f).count(1))
print('contains number zero x times: ', list(f).count(0))

print('----------------------')

w = kmeans.predict(Xwork)
print(w)
print('contains number one x times: ', list(w).count(1))
print('contains number zero x times: ', list(w).count(0))