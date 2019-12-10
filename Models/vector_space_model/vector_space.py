"""
This class focuses on the vector space model and will compute all
of the documents that we have stored in our data folder.
"""
import types
import math
import numpy as np
from Models.vector_space_model.tf_idf import TFIDF
from Models.vector_space_model.preprocess import PreprocessCorpus
from collections import Counter
from nltk.tokenize import word_tokenize


class VectorSpaceModel:

    def __init__(self, corpus):
        if type(corpus) != list and corpus != []:
            print("Must be send as a list")

        self.tf_idf = ""
        self.N = len(corpus)
        self.total_vocab_size = 0
        self.total_vocab = []
        self.D = ""

        if self.N > 0:
            self.tf_idf = TFIDF(corpus)
            self._build(self.tf_idf)

    def _build(self, tf_idf):
        self.tf_idf_result, self.total_vocab_size, self.total_vocab = tf_idf.get_results()
        self.D = np.zeros((self.N, self.total_vocab_size))


        for i in self.tf_idf_result:
            try:
                ind = self.total_vocab.index(i[1])
                self.D[i[0]][ind] = self.tf_idf_result[i]
            except:
                pass

    def _vectorize_query(self, tokens):
        Q = np.zeros(len(self.total_vocab))
        counter = Counter(tokens)
        words_count = len(tokens)

        query_weights = {}
        for token in np.unique(tokens):
            tf = counter[token] / words_count
            df = self.tf_idf.doc_freq(word=token)
            idf = math.log((self.N)/(df))

            # print("token: {}\n\ttf: {}\n\tdf: {}\n\tidf: {}\n\t".format(token,tf,df,idf))

            try:
                ind = self.total_vocab.index(token)
                Q[ind] = tf * idf
            except:
                pass
        return Q

    def _cosine_sim(self, a, b):
        cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        return cos_sim

    def search(self, k, query):
        preprocess_query = PreprocessCorpus(query).get_preprocessed_query()
        query_vector = self._vectorize_query(preprocess_query)

        d_cosine = []
        for d in self.D:
            d_cosine.append(self._cosine_sim(query_vector,d))
        out = np.array(d_cosine).argsort()[-k:][::-1]
        print(d)
        print(out)


# doc1 = "new york times"
# doc2 = "new york post"
# doc3 = "los angeles times"
# doc4 = "Nothing to see here "

# doc5 = "RAndom as shit here"
# doc6 = "what the hell are yall looking at"
# doc7 = "Omg i love new york"
# doc8 = "Hell to nah this aint shit "

# doc9 = "well well well what do we have here"
# doc10 = "look what i found"
# doc11 = "So I guess we meet again my young lee"
# doc12 = "I have a big secret to tell you grandpapa "


# documents = []

# documents.append(doc1)
# documents.append(doc2)
# documents.append(doc3)
# documents.append(doc4)

# documents.append(doc5)
# documents.append(doc6)
# documents.append(doc7)
# documents.append(doc8)

# documents.append(doc9)
# documents.append(doc10)
# documents.append(doc11)
# documents.append(doc12)



# vector_model = VectorSpaceModel(documents)

# vector_model.search(k=4,query="look what i found")