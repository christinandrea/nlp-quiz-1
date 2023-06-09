# -*- coding: utf-8 -*-
"""english.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RiT40jSskJ7JKCz5dAAgWQCwLrjmVxKO
"""

import re,os
import nltk
from nltk import * 
from nltk.stem import * 
from nltk.corpus import stopwords
import matplotlib as plt

nltk.download('all')

dir = "english/"
listFile = os.listdir(dir)

print(listFile)

filedir = {}
items = []

for fileName in listFile:
    filedir[fileName] = {}

for i in listFile:
    final = []
    files = open(dir+i,'r').read()
    lowertext = files.lower()

    oneline = lowertext.replace('\n', '')
    final.append(oneline)

    # print(final)
    # print(len(final))
    
    teks = ''
    teks += final[0]
    print(teks)
    # print(type(teks))

    new = re.sub('[^A-Za-z0-9]+',' ',teks)
    print(new)

    print()

    items.append(new)
    

    stopword = set(stopwords.words("english"))
    regex =  RegexpTokenizer('\W+', gaps = True)

    englishToken = []

    for words in final:
        tokenizedWords = regex.tokenize(words)
        # print(tokenizedWords)

    for words in tokenizedWords:
        if words not in stopword:
            englishToken.append(words)
            # print(englishToken)
            
    wordFreq = FreqDist(englishToken)
    # print(wordFreq)

    for terms,freq in wordFreq.most_common(25):
        filedir[i][terms] = [freq][0]

print(filedir)

print(items)
print(len(items))
print(type(items))
for i in items:
    print(i)

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

lststopwords = list(stopword)

tfidf_vector = TfidfVectorizer(stop_words=lststopwords)
tfidf_wm = tfidf_vector.fit_transform(items)
tfidf_term = tfidf_vector.get_feature_names_out()

df_tfidfvect = pd.DataFrame(data = tfidf_wm.toarray(), index = listFile, columns = tfidf_term)
print("TD-IDF Vectorizer \n")
print(df_tfidfvect)