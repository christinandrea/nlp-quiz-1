import os 
import nltk
from nltk import * 
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas 
import matplotlib as plt


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
        
        # countVector = TfidfTransformer()
        # wordCountVector = countVector.fit_transform(indoToken)
        # idf = pandas.DataFrame({"feature: ":countVector.get_feature_names_out(),'idf_weights':countVector.idf_})

        # print(idf)
        
        wordFreq = {}

        for words,freq in wordFreq.most_common(25):
            print("{} : {}".format(words,freq))



    
           
        

        

        

    