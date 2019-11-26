from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np
import types


class PreprocessCorpus:
    """
    This class is responisble for preposseing all of the works that appear in the corpus
    - Tokennizes the terms
    - Removes stopwords
    _ Stemm the words
    """
    
    def __init__(self, corpus):
        
        self.ps = PorterStemmer()
        self.append_corpus = []
        self.tokenize_query = []
        self.stop_words = set(stopwords.words("english"))
        
        # This is for the query
        if len(corpus) > 3 and isinstance(corpus, str):
            self._preprocess_query(corpus)

        # This is for corpus
        if len(corpus) > 0 and isinstance(corpus,list):
            for tokens in corpus:
                self._preprocess_corpus(tokens)
            

    def _preprocess_corpus(self, tokens):
        symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
        """
        Let's go ahead and tokenize, remove any stop words, and stemm our list of words
        """
        # First we need to lower case the words
        new_tokens = str(np.char.lower(tokens))
        for i in range(len(symbols)):
            new_tokens = np.char.replace(new_tokens, symbols[i], ' ')
            new_tokens = np.char.replace(new_tokens, "  ", " ")
        new_tokens = np.char.replace(new_tokens, ",", "")
        new_tokens = str(np.char.replace(new_tokens, "'", ""))
        # Then tokenize the words
        new_tokens = word_tokenize(new_tokens)

        new_tokens = [token for token in new_tokens if token not in self.stop_words]
        new_tokens = [self.ps.stem(w) for w in new_tokens]
        self.append_corpus.append(new_tokens)
        
    def get_preprocessed_corpus(self):
        return self.append_corpus
    
    def get_preprocessed_query(self):
        return self.tokenize_query
    
    def _preprocess_query(self,query):
        symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"

        # First we need to lower case the words
        query_tokenize = np.char.lower(query)

        for i in range(len(symbols)):
            query_tokenize = np.char.replace(query_tokenize, symbols[i], ' ')
            query_tokenize = np.char.replace(query_tokenize, "  ", " ")
        query_tokenize = np.char.replace(query_tokenize, ",", "")
        query_tokenize = str(np.char.replace(query_tokenize, "'", ""))

        # Second tokenize our query
        query_tokenize = word_tokenize(query_tokenize)

        query_tokenize = [token for token in query_tokenize if token not in symbols]
        query_tokenize = [token for token in query_tokenize if token not in self.stop_words]
        query_tokenize = [self.ps.stem(w) for w in query_tokenize]
        self.tokenize_query = query_tokenize

    
