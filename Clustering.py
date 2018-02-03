import sklearn.cluster.k_means_
import numpy as np
from sklearn.cluster.k_means_ import KMeans

# X is a numpy array/matrix
# K is number of desired clusters
def clusterViaKmeans(X, K):
    kmeans = KMeans(n_clusters=K, random_state=0).fit(X)
    labels = kmeans.labels_
    print('labels', labels)



