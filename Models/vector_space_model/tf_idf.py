import types
import numpy as np
from collections import Counter
from Models.vector_space_model.preprocess import PreprocessCorpus
from Models.vector_space_model.document_frequency import DocumentFrequency

class TFIDF:
    """This class will calculate the TF IDF """
    def __init__(self, corpus):
        
        if type(corpus) != list and corpus != []:
            print("A list must be send")

        # Lets get the total number of documents
        self.N = len(corpus)
        
        self.document_frequency = {}
        self.tf_idf = {}
        self.total_vocabulary = []
        self.processed_corpus = []
        self.total_vocabulary_size = 0

        if len(corpus) > 0:
            self._do_preprocess(corpus)

    def _do_preprocess(self,corpus):
        """ Lets preprocess the terms, get the document frequency, total vocabulary, and size """
        self.processed_corpus = PreprocessCorpus(corpus).get_preprocessed_corpus()
        self.document_frequency = DocumentFrequency(self.processed_corpus).get_document_frequency()
        self.total_vocabulary = [terms for terms in self.document_frequency]
        self.total_vocabulary_size = len(self.document_frequency)

        # No we calculate the TF-IDF
        self._calculate_tf_idf()

    
    def _calculate_tf_idf(self):
        """ Calculate TF_IDF """
        for i in range(self.N):
            tokens = self.processed_corpus[i]
            counter = Counter(tokens)
            words_count = len(tokens)

            for token in np.unique(tokens):
                tf = counter[token]/words_count
                df = self.doc_freq(token)
                idf = np.log10((self.N+1)/(df+1))
                self.tf_idf[i,token] = tf * idf
                #print("token: {}\n\tN: {}\n\ttf: {}\n\tdf: {}\n\tidf: {}\n\ttf_idf: {}\n".format(token,self.N,tf,df,idf,(tf*idf)))

    
    def doc_freq(self,word):
        count = 0
        try:
            count = self.document_frequency[word]
            return count
        except:
            pass
        return count

    def get_results(self):
        return self.tf_idf,self.total_vocabulary_size,self.total_vocabulary
    


