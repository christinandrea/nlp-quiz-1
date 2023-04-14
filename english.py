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
        
        uni_b = {}

        for x in englishToken:
            if x not in uni_b:
                uni_b[x] = 1
            else:
                uni_b[x] += 1


        for words,freq in uni_b.items():
            print("{} : {}".format(words,freq))
