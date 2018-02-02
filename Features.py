import numpy as np
import corpusUtil
from corpusUtil import *
import numpy as np
import clustering
from clustering import *


class Features(object):
    __slots__ = 'word2MonolingualFeatureVector', 'word2BilingualFeatureVector', 'word2CombinedFeatureVector'

    def __init__(self):
        self.word2MonolingualFeatureVector = {}
        self.word2BilingualFeatureVector = {}
        self.word2CombinedFeatureVector = {}

    def getMonolingualFeatures(self, path, targetTranslations):
        neighbors = set()
        for t in targetTranslations:
            neighbors = neighbors.union(getNeighbors(path, t))

        featureMatrix = []

        tokenFrequencies = getTokenFreqFromCorpus(path)
        bigramFrequencies = getNGramCountsFromCorpus(path, 2)

        for t in targetTranslations:
            featureVektor = []

            targetTranslationCount = tokenFrequencies[t]
            for neighbor in neighbors:
                # ignoring direction
                bigramCount = bigramFrequencies[(neighbor, t)]
                bigramCount += bigramFrequencies[(t, neighbor)]

                neighborCount = tokenFrequencies[neighbor]

                pmi = 0
                if bigramCount != 0:
                    pmi = np.log2(bigramCount / (neighborCount * targetTranslationCount))

                featureVektor.append(pmi)

            featureMatrix.append(featureVektor)
            self.word2MonolingualFeatureVector[t] = featureVektor

        return featureMatrix



features = Features()
monoResult = features.getMonolingualFeatures('resources/corpusData/think_sent.txt', ['nice', 'good', 'proper', 'solid', 'amazing'])

for mr in monoResult:
    print(mr)

print('printing features: done')
print()

#print(features.word2MonolingualFeatureVector['nice'])
#print(features.word2MonolingualFeatureVector['good'])
#print(features.word2MonolingualFeatureVector['proper'])
#print(features.word2MonolingualFeatureVector['solid'])
#print(features.word2MonolingualFeatureVector['amazing'])

X = np.array(monoResult)

clusterViaKmeans(X, 2)
