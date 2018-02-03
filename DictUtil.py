import re
import csv

class DictElement(object):
    __slots__ = 'key', 'value', 'dictionary'

    def __init__(self):
        self.key = ''           #helper var for creating the dictionary
        self.value = set()      #helper var for creating the dictionary
        self.dictionary = {}    #actual dictionary which is created via "createDict"

    def replaceAll(self, regex, s):
        occurrences = re.findall(regex, s)
        for occurrence in occurrences:
            s = s.replace(occurrence, '')
        return s

    def before(self, value, a):
        # Find first part and return slice before it.
        pos_a = value.find(a)
        if pos_a == -1: return ""
        return value[0:pos_a]


    def createDict(self, path):
        with open(path, 'r') as f:
            dict_ = {}

            lines = f.readlines()
            lines = [_.strip() for _ in lines]

            for line in lines:
                line = self.replaceAll('\(.*?\)', line)
                line = self.replaceAll('\[.*?\]', line)
                if not line.startswith('#'):
                    source, translation = line.split('::', 1)
                    source = self.before(source, '{').strip()
                    translation = self.replaceAll('{.*?}', translation)
                    translations = translation.split(',')
                    if source not in dict_:
                        dictElement = DictElement()
                        dictElement.key = source
                        dict_[source] = dictElement
                    for t in translations:
                        t = t.strip()
                        d = dict_[source]
                        d.value.add(t)
            self.dictionary = dict_


    def extractDictionaryToFile(self, fileName):
        with open(fileName, 'w') as output:
            out = csv.writer(output, delimiter='\t')
            d = self.dictionary
            for key in d:
                dEl = d[key]
                key = dEl.key
                val = list(dEl.value)
                out.writerow([key] + [val])


#dict = DictElement()
#dict.createDict('resources/dict/de-en-enwiktionary.txt')
#myDict = dict.dictionary
#for key in myDict:
#    dEl = myDict[key]
#    print(dEl.key, '-->', dEl.value)

#sdict.extractDictionaryToFile('de-en-formated.txt')




