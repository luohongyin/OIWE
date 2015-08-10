#lhy
#2015.4

import cPickle
import random

class Analysis():
    def __init__(self):
        self.vectors = cPickle.load(open("vectors",'rb'))
        self.words = self.vectors.keys()
        self.scale = len(self.vectors[self.words[0]])
        self.dimensions = {}

    def dimension_analysis(self):
        self.topWords = {}
        for i in range(self.scale):
            self.dimensions[i] = {}
        for i in range(len(self.words)):
            vector = list(self.vectors[self.words[i]])
            for j in range(len(vector)):
                if vector[j] > 0:
                    self.dimensions[j][self.words[i]] = vector[j]
        for i in range(self.scale):
            self.topWords[i] = []
            dictionary = {}
            for (key,value) in self.dimensions[i].items():
                if value not in dictionary:
                    dictionary[value] = [key]
                else:
                    dictionary[value].append(key)
            index = dictionary.keys()
            index.sort()
            for j in range(len(index)):
                self.topWords[i].extend(dictionary[index[j]])
        print "Top Words ok"
        outHandle = open("words",'w')
        for i in range(len(self.topWords)):
            d = len(self.topWords[i])
            words = self.topWords[i][d - 5:d]
            location = int(5 * random.random())
            words.insert(location,self.topWords[i][0])
            words.append(str(location))
            string = ' '.join(words)
            outHandle.write(string + '\n')
        outHandle.close()
        print "Data Ready"
