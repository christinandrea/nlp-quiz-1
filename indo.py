import os 
import nltk
# cle

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
        
        uni_b = {}

        for x in indoToken:
            if x not in uni_b:
                uni_b[x] = 1
            else:
                uni_b[x] += 1

        print(uni_b)

        

        

    