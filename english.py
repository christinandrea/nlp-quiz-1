import os
import nltk

from nltk import *
from nltk.corpus import stopwords

english = os.chdir('english')
englishFiles = os.listdir(english)

for i in englishFiles:
    if i.endswith('.txt'):
        files = open(i,'r').read()

        lower = files.lower()

        stopword = set(stopwords.words("english"))

        regex =  RegexpTokenizer('\W+', gaps = True)
        tokenizedWords = regex.tokenize(lower)

        englishToken = []
        for words in tokenizedWords:
            if words not in stopword:
                englishToken.append(words)
        
        wordFreq = {}

        for x in englishToken:
            if x not in wordFreq:
                wordFreq[x] = 1
            else:
                wordFreq[x] += 1


        for words,freq in wordFreq.items():
            print("{} : {}".format(words,freq))
