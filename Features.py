import numpy as np
import CorpusUtil
from CorpusUtil import *
import numpy as np
import Clustering
from Clustering import *


class Features(object):
    __slots__ = 'word2MonolingualFeatureVector', 'word2BilingualFeatureVector', 'word2CombinedFeatureVector', 'corpusUtil', 'ngramSize'

    def __init__(self):
        self.word2MonolingualFeatureVector = {}
        self.word2BilingualFeatureVector = {}
        self.word2CombinedFeatureVector = {}
        self.corpusUtil = CorpusUtil()
        self.ngramSize = 2

    def feedCorpusUtil(self, path, targetTranslations):
        for p in path:
            self.corpusUtil.countTokenFreqFromCorpus(p)
            self.corpusUtil.countNGramFrequenciesFromCorpus(p, self.ngramSize)
            for t in targetTranslations:
                self.corpusUtil.findNeighbors(p, t)

    def reverseDict(self, dict):
        return {v: k for k, v in dict.items()}

    def getMonolingualFeatures(self, path, targetTranslations):
        #feed the corpus object with data
        self.feedCorpusUtil(path, targetTranslations)
        neighbors = set()
        for n in self.corpusUtil.neighbors:
            neighbors = neighbors.union(self.corpusUtil.neighbors[n])

        featureMatrix = []

        for t in targetTranslations:
            featureVektor = []

            targetTranslationCount = self.corpusUtil.tokenFrequencies[t]
            for neighbor in neighbors:
                # ignoring direction
                bigramCount = self.corpusUtil.nGramFrequencies[(neighbor, t)]
                neighborCount = self.corpusUtil.tokenFrequencies[neighbor]

                pmi = 0
                if bigramCount != 0 and neighborCount != 0 and targetTranslationCount != 0:
                    pmi = np.log2(bigramCount / (neighborCount * targetTranslationCount))

                featureVektor.append(pmi)

            featureMatrix.append(featureVektor)
            self.word2MonolingualFeatureVector[t] = featureVektor
        return featureMatrix, targetTranslations


    def getBilimgualFeatures(self, path):
        return 0



spitze = ['tip', 'peak', 'lead', 'spike', 'lace', 'cusp', 'top', 'point', 'front']
verstehen = ['understand', 'comprehend', 'know']
liebe = ['love']
gesundheitlich = ['hygienic', 'sanitary']
Gesundheit = ['health', 'soundness', 'strength', 'stability']
stellen = ['park', 'put', 'set', 'stand']
gut = ['good', 'nice']
problem = ['issue', 'problem', 'problems']
colocar = ['collocate', 'invest', 'locate', 'place', 'position', 'put']
unter = ['below', 'under']
abhängig = ['dependent', 'addicted']
reich = ['rich', 'wealthy', 'prolific', 'affluent']

features = Features()

coca = ['resources/corpora/COCA/w_mag_2012.txt',
        'resources/corpora/COCA/w_acad_2012.txt',
        'resources/corpora/COCA/w_news_2012.txt',
        'resources/corpora/COCA/w_spok_2012.txt',
        'resources/corpora/COCA/w_fic_2012.txt']

glowbe = ['resources/corpora/GloWbe/w_au_b.txt',
          'resources/corpora/GloWbe/w_bd_b.txt',
          'resources/corpora/GloWbe/w_bd_g.txt',
          'resources/corpora/GloWbe/w_ca_b.txt',
          'resources/corpora/GloWbe/w_ca_g.txt',
          'resources/corpora/GloWbe/w_gb_b.txt',
          'resources/corpora/GloWbe/w_gb_g.txt',
          'resources/corpora/GloWbe/w_gh_b.txt',
          'resources/corpora/GloWbe/w_gh_g.txt',
          'resources/corpora/GloWbe/w_hk_b.txt',
          'resources/corpora/GloWbe/w_hk_g.txt',
          'resources/corpora/GloWbe/w_ie_b.txt',
          'resources/corpora/GloWbe/w_ie_g.txt',]


europarl_tokenized = [
    'resources/corpora/Europarl/Europarl.en'
]

openSubs = [
    'resources/corpora/OpenSubtitles/small/xaa'
]


monoResult = features.getMonolingualFeatures(openSubs,
                                             verstehen + problem)

for mr in monoResult[0]:
    print(mr)

print('printing features: done')
print()


mostCommon = features.corpusUtil.tokenFrequencies.most_common(500)
for m in mostCommon:
    print(m)


print()

comprehend = features.corpusUtil.tokenFrequencies['comprehend']
print('comprehend', comprehend)

print()
X = np.array(monoResult[0])
labels = clusterViaKmeans(X, 2)

print()

for l,m in zip(labels, monoResult[1]):
    print(l, m)



