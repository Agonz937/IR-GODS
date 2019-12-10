import numpy as np
from Models.vector_space.preprocess_v2 import PreprocessV2
from collections import Counter

class VectorSpace:
    def __init__(self,corpus):
        self.tfidf = []
        self.idf = []
        self.documets_words = []
        self.vocab_dict = {}
        self.vocab = []
        # This is for corpus
        if len(corpus) > 0 and isinstance(corpus,list):
            self._build(corpus=corpus)

    def _build(self,corpus):
        #print("Im being build in Vector Space Class")
        data = corpus
        document_words = PreprocessV2(data).get_preprocessed_corpus()
        #print("Done preprocessing documents")
        self.document_words = [doc.split() for doc in document_words]
        #print("Done tokenzing documents")
        self.vocab = sorted(set(sum(self.document_words, [])))
        #print("Done getting each vocab")
        self.vocab_dict = {k:i for i,k in enumerate(self.vocab)}
        #print("Done getting setting vocab_dic")


        #print("Computing X_tf, idf, and TFIDF")
        X_tf = self._get_tf(corpus=data,vocab=self.vocab,vocab_dict=self.vocab_dict,document_words=self.document_words)
        self.idf = self._get_idf(X_tf=X_tf)
        self.tfidf = self.compute_tf_idf(X_tf=X_tf,idf=self.idf)

        #print("Done computing TFIDF ready to Query")


    def compute_tf_idf(self,X_tf,idf):
        return X_tf * idf

    def _get_tf(self,corpus,vocab,vocab_dict,document_words):
        X_tf = np.zeros((len(corpus), len(vocab)), dtype=int)
        for i,doc in enumerate(document_words):
            for word in doc:
                X_tf[i, vocab_dict[word]] += 1
        return X_tf

    def _get_idf(self,X_tf):
        return np.log10((X_tf.shape[0])/(X_tf.astype(bool).sum(axis=0)))

    def _cosine_sim(self, a, b):
        check = (np.linalg.norm(a) * np.linalg.norm(b))
        denominator = 1 if check == 0 else check
        cos_sim = np.dot(a, b) / denominator
        return format(cos_sim, ".4f")

    def search(self,queries):
        query_result = []
        for query in queries:
            data = query
            processed_query = PreprocessV2(data).get_preprocessed_query()
            processed_query = processed_query.split()
            query_vector = self._get_tf_query(processed_query)

            d_cosine = {}
            for i,d in enumerate(self.tfidf):
                pos = i + 1
                d_cosine[pos] = self._cosine_sim(query_vector,d)
            
            d_cosine = sorted(d_cosine.items(), key = lambda kv:(kv[1],kv[0]), reverse=True)

            query_result.append(d_cosine)
        return query_result

        

    def _get_tf_query(self,query):
        Q = np.zeros(len(self.vocab))
        counter = Counter(query)

        for token in np.unique(query):
            try:
                Q[self.vocab_dict[token]] = counter[token] * self.idf[self.vocab_dict[token]]
            except:
                pass
        return Q
        

