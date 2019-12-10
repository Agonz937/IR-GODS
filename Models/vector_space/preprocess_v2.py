from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from num2words import num2words
import numpy as np
import types

class PreprocessV2:

    def __init__(self, corpus):
        self.append_corpus = []
        self.preprocessed_query = ""
        self.stop_words = stopwords.words('english')

        # This is for the query
        # if len(corpus) > 3 and isinstance(corpus, str):
        #     self._preprocess_query(corpus)
        if len(corpus) > 3 and isinstance(corpus, str):
            self.preprocessed_query = self.preprocess_query(corpus)
        # This is for corpus
        if len(corpus) > 0 and isinstance(corpus,list):
            for tokens in corpus:
                self.preprocess(tokens)

    def get_preprocessed_query(self):
        return self.preprocessed_query

    def get_preprocessed_corpus(self):
        return self.append_corpus

    def preprocess(self,data):
        data = self.convert_lower_case(data)
        data = self.remove_punctuation(data) 
        data = self.remove_apostrophe(data)
        data = self.remove_stop_words(data)
        data = self.convert_numbers(data)
        data = self.stemming(data)
        data = self.remove_punctuation(data)
        data = self.convert_numbers(data)
        data = self.stemming(data)
        data = self.remove_punctuation(data) 
        data = self.remove_stop_words(data) 
        self.append_corpus.append(data)
    

    def preprocess_query(self,data):
        data = self.convert_lower_case(data)
        data = self.remove_punctuation(data) 
        data = self.remove_apostrophe(data)
        data = self.remove_stop_words(data)
        data = self.convert_numbers(data)
        data = self.stemming(data)
        data = self.remove_punctuation(data)
        data = self.convert_numbers(data)
        data = self.stemming(data)
        data = self.remove_punctuation(data) 
        data = self.remove_stop_words(data) 
        return data

    def convert_lower_case(self,data):
        return np.char.lower(data)

    def remove_stop_words(self,data):
        words = word_tokenize(str(data))
        new_text = ""
        for w in words:
            if w not in self.stop_words and len(w) > 1:
                new_text = new_text + " " + w
        return new_text
    
    def remove_punctuation(self,data):
        symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
        for i in range(len(symbols)):
            data = np.char.replace(data, symbols[i], ' ')
            data = np.char.replace(data, "  ", " ")
        data = np.char.replace(data, ',', '')
        return data
    
    def remove_apostrophe(self,data):
        return np.char.replace(data, "'", "")

    def stemming(self,data):
        stemmer= PorterStemmer()
        
        tokens = word_tokenize(str(data))
        new_text = ""
        for w in tokens:
            new_text = new_text + " " + stemmer.stem(w)
        return new_text
    
    def convert_numbers(self,data):
        tokens = word_tokenize(str(data))
        new_text = ""
        for w in tokens:
            try:
                w = num2words(int(w))
            except:
                a = 0
            new_text = new_text + " " + w
        new_text = np.char.replace(new_text, "-", " ")
        return new_text


