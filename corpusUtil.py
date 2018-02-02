from collections import Counter
import nltk
from nltk import *
import numpy as np

trigram_measures = nltk.collocations.TrigramAssocMeasures()
bigram_measures = nltk.collocations.BigramAssocMeasures()

def getTokenFreqFromCorpus(path):
    with open(path, 'r', encoding='latin1') as f:
        lines = f.readlines()
        counter = Counter()
        for line in lines:
            tokens = line.split()[1:]
            for t in tokens:
                counter[t] += 1
        return counter

def getNGramCountsFromCorpus(path, n):
    with open(path, 'r', encoding='latin1') as f:
        lines = f.readlines()
        ngramCounter = Counter()
        for line in lines:
            ngrams_ = ngrams(line.split()[1:], n)
            for gram in ngrams_:
                ngramCounter[gram] += 1
        return ngramCounter

#returns all possible neighbors for a specific word in the corpus
#for n it returns all possible n-1 and n+1
def getNeighbors(path, token):
    token = token.lower()
    with open(path, 'r', encoding='latin1') as f:
        lines = f.readlines()
        neighbors = set()
        for line in lines:
            tokens = line.split()[1:]
            for idx, t in enumerate(tokens):
                t = t.lower()
                if t == token:
                    before = idx-1
                    after = idx+1
                    if before >= 0:
                        neighbors.add(tokens[before])#add the n-1 token
                    if after < len(tokens):
                        neighbors.add(tokens[after])#add the n+1 token

        return neighbors


#counter = getTokenFreqFromCorpus('resources/corpusData/think_sent.txt')
#bigramCounter = getNGramCountsFromCorpus('resources/corpusData/think_sent.txt', 2)

#print(bigramCounter)
#print(bigramCounter[('it','then')])
#print(bigramCounter[('then', 'it')])

#neighbors = getNeighbors('resources/corpusData/think_sent.txt', 'nice')
#print(neighbors)
#print(neighbors)

#neighborsBiggerOne = []
#for neighbor in neighbors:
#    if counter[neighbor] > 10:
#        neighborsBiggerOne.append(neighbor)

#print(neighborsBiggerOne)










