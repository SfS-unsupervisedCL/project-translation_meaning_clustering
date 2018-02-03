from collections import Counter
import nltk
from nltk import *
import numpy as np


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
