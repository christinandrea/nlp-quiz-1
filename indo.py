import os 
import nltk
from nltk import * 
from nltk.corpus import stopwords


indo = os.chdir('indo')

indoFiles = os.listdir(indo)

for i in indoFiles:
    if i.endswith('.txt'):
        files = open(i,'r').read()

        lower = files.lower()

        stopword = set(stopwords.words("indonesian"))

        regex =  RegexpTokenizer('\W+', gaps = True)
        tokenizedWords = regex.tokenize(lower)

        indoToken = []
        for words in tokenizedWords:
            if words not in stopword:
                indoToken.append(words)
        
        wordFreq = {}

        for x in indoToken:
            if x not in wordFreq:
                wordFreq[x] = 1
            else:
                wordFreq[x] += 1

        for words,freq in wordFreq.items():
            print("{} : {}".format(words,freq))
           
        

        

        

    