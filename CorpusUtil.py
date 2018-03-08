from collections import Counter
import nltk
from nltk import *
import numpy as np
import xml.etree.ElementTree as ET
import tmx


trigram_measures = nltk.collocations.TrigramAssocMeasures()
bigram_measures = nltk.collocations.BigramAssocMeasures()




class CorpusUtil(object):

    __slots__ =  'tokenFrequencies', 'nGramFrequencies', 'neighbors'

    def __init__(self):
        self.tokenFrequencies = Counter()
        self.nGramFrequencies = Counter()
        self.neighbors = {}

    def countTokenFreqFromCorpus(self, path):
        with open(path, 'r', encoding='latin1') as f:
            lines = f.readlines()
            for line in lines:
                tokens = line.split()[1:]
                for t in tokens:
                    t = t.lower()
                    self.tokenFrequencies[t] += 1

    #once the object is created same ngram size needs to be used for this particular instance, since it is stored to
    #the instance variable "nGramFrequencies"
    def countNGramFrequenciesFromCorpus(self, path, n):
        with open(path, 'r', encoding='latin1') as f:
            lines = f.readlines()
            for line in lines:
                ngrams_ = ngrams(line.split()[1:], n)
                for gram in ngrams_:
                    self.nGramFrequencies[gram] += 1

    #returns all possible neighbors for a specific word in the corpus
    #for n it returns all possible n-1 and n+1
    def findNeighbors(self, path, token):
        token = token.lower()
        with open(path, 'r', encoding='latin1') as f:
            lines = f.readlines()
            for line in lines:
                tokens = line.split()[1:]
                for idx, t in enumerate(tokens):
                    t = t.lower()
                    if t == token:
                        before = idx-1
                        after = idx+1
                        if before >= 0:
                            if token not in self.neighbors.keys():
                                self.neighbors[token] = set()
                            self.neighbors[token].add(tokens[before])#add the n-1 token
                        if after < len(tokens):
                            if token not in self.neighbors.keys():
                                self.neighbors[token] = set()
                            self.neighbors[token].add(tokens[after])#add the n+1 token


class AlignedCorpusUtil(object):
    __slots__ = 'alignedSentences', 'tokenFrequenciesSource', 'tokenFrequenciesTarget', 'bigramFrequenciesSource'

    def __init__(self):
        self.alignedSentences = {}
        self.tokenFrequenciesSource = Counter()
        self.tokenFrequenciesTarget = Counter()
        self.bigramFrequenciesSource = Counter()

    def readAligedCorpus(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        body = root.find('body')
        for tu in body.findall('tu'):
            de = ''
            en = ''
            for tuv in tu.findall('tuv'):
                atr = tuv.attrib
                lang = atr.get('{http://www.w3.org/XML/1998/namespace}lang')

                if lang == 'de':
                    for seg in tuv.findall('seg'):
                        de = seg.text
                elif lang == 'en':
                    for seg in tuv.findall('seg'):
                        en = seg.text

            self.alignedSentences[de] = en

    def readTokenizedAlignedCorpora(self, path, lang):
        if lang.lower().strip() == 'de':
            treeDE = ET.parse(path)
            rootDE = treeDE.getroot()
            for w in rootDE.findall('*/*/*/w'):
                word = w.text.lower().strip()
                self.tokenFrequenciesSource[word] += 1
            for w in rootDE.findall('*/*/*/*/w'):
                word = w.text.lower().strip()
                self.tokenFrequenciesSource[word] += 1

        if lang.lower().strip() == 'en':
            treeEN = ET.parse(path)
            rootEN = treeEN.getroot()
            for w in rootEN.findall('*/*/*/w'):
                word = w.text.lower().strip()
                self.tokenFrequenciesTarget[word] += 1
            for w in rootEN.findall('*/*/*/*/w'):
                word = w.text.lower().strip()
                self.tokenFrequenciesTarget[word] += 1
            for w in rootEN.findall('*/*/*/*/*/w'):
                word = w.text.lower().strip()
                self.tokenFrequenciesTarget[word] += 1

    def sourceBigramsFromAlignedCorpus(self, pathDe):
        treeDE = ET.parse(pathDe)
        rootDE = treeDE.getroot()
        words1 = []
        for w in rootDE.findall('*/*/*/w'):
            word = w.text.lower().strip()
            words1.append(word)
        #get bigrams
        for idx,val in enumerate(words1):
            if idx < len(words1)-1:
                self.bigramFrequenciesSource[(val,words1[idx+1])] += 1

        words2 = []
        for w in rootDE.findall('*/*/*/*/w'):
            word = w.text.lower().strip()
            words2.append(word)
        #get bigrams
        for idx,val in enumerate(words2):
            if idx < len(words2)-1:
                self.bigramFrequenciesSource[(val,words2[idx+1])] += 1





print('start')
c = AlignedCorpusUtil()
path = 'resources/corpora/Europarl/de-en.tmx'
c.readAligedCorpus(path)

import glob, os
de_path = 'resources/corpora/Europarl/Europarl_de/xml/de/'
en_path = 'resources/corpora/Europarl/Europarl_en/xml/en/'

for file in os.listdir(de_path):
    if file.endswith(".xml"):
        c.readTokenizedAlignedCorpora(de_path+file, 'de')

for file in os.listdir(en_path):
    if file.endswith(".xml"):
        c.readTokenizedAlignedCorpora(en_path+file, 'en')

c.sourceBigramsFromAlignedCorpus('resources/corpora/Europarl/Europarl_de/xml/de/ep-00-01-17.xml')
bigrams = c.bigramFrequenciesSource
mostCommon = bigrams.most_common(100)

count = 0
sentences = c.alignedSentences
for sent in sentences:
    if ' haus ' in sent:
        if ' house ' in sentences[sent]:
            count += 1

print('haus translated as house: ', count)
print('haus on its own: ', c.tokenFrequenciesSource['haus'])
print('house on its own: ', c.tokenFrequenciesTarget['house'])

for bi in mostCommon:
    print(bi)

