#lhy
#2015.5

import cPickle
import word2vec

model = word2vec.load("text8.txt")
words = list(model.vocab)
vectors = {}
for i in range(1,len(words)):
    vectors[words[i]] = list(model[words[i]])
print "Vectors ok"

cPickle.dump(vectors,open("../vectors/vectors",'wb'))
print "Data ok"
