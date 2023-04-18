# import os 
# import nltk
# from nltk import * 
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.feature_extraction.text import CountVectorizer
# import pandas 
# import matplotlib as plt


# indo = os.chdir('indo')

# indoFiles = os.listdir(indo)

# for i in indoFiles:
#     if i.endswith('.txt'):
#         files = open(i,'r').read()

#         lower = files.lower()

#         stopword = set(stopwords.words("indonesian"))

#         regex =  RegexpTokenizer('\W+', gaps = True)
#         tokenizedWords = regex.tokenize(lower)

#         indoToken = []
#         for words in tokenizedWords:
#             if words not in stopword:
#                 indoToken.append(words)
        
#         # countVector = TfidfTransformer()
#         # wordCountVector = countVector.fit_transform(indoToken)
#         # idf = pandas.DataFrame({"feature: ":countVector.get_feature_names_out(),'idf_weights':countVector.idf_})

#         # print(idf)
        
#         wordFreq = {}

#         for words,freq in wordFreq.most_common(25):
#             print("{} : {}".format(words,freq))


from nltk.corpus import stopwords
import re,os
import nltk
from nltk import * 
from nltk.stem import * 
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

dir = "indo/"
listFile = os.listdir(dir)

filedir = {}
final = []
stemmer = StemmerFactory()
idn_stemmer = stemmer.create_stemmer()
stopword = list(set(stopwords.words("indonesian")))
emp_file = []
clean_docs = []
for files in listFile:
    emp_file.append(files)

    with open(dir+files,'r') as corpus:
        print(corpus)
        content = corpus.read()
        content = content.lower()
        content = idn_stemmer.stem(content)
        clean_docs.append(content)



tfidf_vec = TfidfVectorizer(stop_words=stopword)
tfidf_wm = tfidf_vec.fit_transform(clean_docs)
tfidf_term = tfidf_vec.get_feature_names_out()

df_tfidfvect = pd.DataFrame(data = tfidf_wm.toarray(),index = listFile,columns = tfidf_term)
print("TD-IDF Vectorizer \n")
print(df_tfidfvect)
           
        

        

        

    