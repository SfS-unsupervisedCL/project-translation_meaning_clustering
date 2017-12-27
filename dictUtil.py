import re

class DictElement(object):
    __slots__ = 'key', 'value'

    def __init__(self):
        self.key = ''
        self.value = set()


def replaceAll(regex, s):
    occurrences = re.findall(regex, s)
    for occurrence in occurrences:
        s = s.replace(occurrence, '')
    return s

def before(value, a):
    # Find first part and return slice before it.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]


def createDict(path):
    with open(path, 'r') as f:
        dict_ = {}

        lines = f.readlines()
        lines = [_.strip() for _ in lines]

        for line in lines:
            line = replaceAll('\(.*?\)', line)
            line = replaceAll('\[.*?\]', line)
            if not line.startswith('#'):
                source, translation = line.split('::', 1)
                source = before(source, '{').strip()
                translation = replaceAll('{.*?}', translation)
                translations = translation.split(',')
                if source not in dict_:
                    dictElement = DictElement()
                    dictElement.key = source
                    dict_[source] = dictElement
                for t in translations:
                    t = t.strip()
                    d = dict_[source]
                    d.value.add(t)
        return dict_


#myDict = createDict('resources/dict/en-de-enwiktionary.txt')
#for key in myDict:
#    dEl = myDict[key]
#    print(dEl.key, '-->', dEl.value)




