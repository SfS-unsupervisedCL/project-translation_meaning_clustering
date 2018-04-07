from collections import Counter
import sys
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.feature_extraction import DictVectorizer
import sklearn.cluster.k_means_
from sklearn.cluster.k_means_ import KMeans, MiniBatchKMeans
from sklearn.cluster import SpectralClustering, DBSCAN
from sklearn. decomposition import PCA, KernelPCA, SparsePCA, TruncatedSVD, IncrementalPCA
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import numpy as np
from nltk.corpus import stopwords

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import pandas as pd
from pandas.plotting import scatter_matrix

def readFile(words, path):
    with open(path, 'r', encoding='utf8') as f:
        rval = []
        stop_words = set(stopwords.words('english'))
        for idx in range(len(words)):
            rval.append(Counter())

        lines = f.readlines()
        for line in lines:
            tokens = line.split()

            for i, word in enumerate(words):
                if(word in tokens):
                    tokens = [token.lower() for token in tokens if token.isalpha() and not token in stop_words]
                    counter = rval[i]
                    idx = tokens.index(word)
                    #bow of 5 (2 on the left | 2 on the right)
                    bow = tokens[idx-2:idx+3]
                    #print(bow)
                    for w in bow:
                        counter[w] += 1
        return rval


corpus = readFile(['apple', 'banana', 'oranges', 'watermelons', 'strawberries', 'grape', 'peach',
                   'cherry', 'pear', 'plum', 'melon', 'lemon', 'coconut', 'lime',
                   'office', 'home', 'building', 'house', 'apartment', 'city', 'town', 'village'], 'resources/corpora/OpenSubtitles/small/combined2')
#'office', 'home', 'building', 'house', 'flat', 'skyscraper', 'apartment', 'commune', 'bureau'
#'chair', 'table', 'door', 'floor'
#'apple', 'banana', 'oranges', 'watermelons'
#'sister', 'brother', 'father', 'mother'
#'nose', 'eyes', 'mouth', 'face'

vectorizer = DictVectorizer()
X = vectorizer.fit_transform(corpus).toarray()

sc = StandardScaler()
X_std = sc.fit_transform(X)

#pca = PCA(n_components=2)
pca = KernelPCA(n_components=3, kernel='rbf')
#pca = SparsePCA()
#pca = TruncatedSVD()
#pca = IncrementalPCA()
X_pca = pca.fit_transform(X_std)


kmeans = KMeans(n_clusters=2, init='random').fit(X_pca)
f = kmeans.predict(X_pca)

print(f)
print('contains number one x times: ', list(f).count(1))
print('contains number zero x times: ', list(f).count(0))


#plot function from my warmup assignment
def plot(f):
    arr = np.array(f)
    if arr.shape[1] == 2:
        x1 = arr[:, 0]
        x2 = arr[:, 1]

        plt.scatter(x1, x2)
        plt.show()

    elif arr.shape[1] == 3:

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x = []
        y = []
        z = []
        for line in f:
            x.append(float(line[0]))
            y.append(float(line[1]))
            z.append(float(line[2]))

        ax.scatter(x, y, z, c='r', marker='o')

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        plt.show()

    else:
        m = np.array(f, dtype=float)
        # first make some fake data with same layout as yours
        data = pd.DataFrame(m)
        # now plot using pandas
        scatter_matrix(data, alpha=0.2, figsize=(6, 6), diagonal='kde')
        plt.show()


plot(X_pca)