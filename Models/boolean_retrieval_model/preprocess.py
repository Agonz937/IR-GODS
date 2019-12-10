import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import sent_tokenize , word_tokenize
import re
import os
import numpy as np


class Preprocess:
    def __init__(self,corpus):
        self.Stopwords = set(stopwords.words('english'))
        self.courpus = corpus
        self.all_words = []
        self.dict_global = {}

        self._build()
    
    def _build(self):
        """ Get rid of """
        sepcial_words = [self.remove_special_characters(x) for x in self.courpus]
        sepcial_words = [re.sub(re.compile('\d'),'',x) for x in sepcial_words]

        print(sepcial_words)
    
    def finding_all_unique_words_and_freq(self,words):
        words_unique = []
        word_freq = {}
        for word in words:
            if word not in words_unique:
                words_unique.append(word)
        for word in words_unique:
            word_freq[word] = words.count(word)
        return word_freq
    def finding_freq_of_word_in_doc(self,word,words):
        freq = words.count(word)
            
    def remove_special_characters(self,text):
        regex = re.compile('[^a-zA-Z0-9\s]')
        text_returned = re.sub(regex,'',text)
        return text_returned
