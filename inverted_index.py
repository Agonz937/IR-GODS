import re
import sys
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 
from collections import defaultdict
from collections import Counter
import os


class Query:
    # Query
    def query(self,queryWord,post):
        ps = PorterStemmer()
        data_dict = {}
        for terms in queryWord:
            term1 = ps.stem(terms[0])
            term2 = ps.stem(terms[2])
            if terms[1] == "AND":
                key = "{} {} {}".format(term1,"AND",term2)
                posts = intersect(post[term1],post[term2])
                data_dict.update({key: posts})
            elif terms[1] == "OR":
                key = "{} {} {}".format(term1,"OR",term2)
                posts = union(post[term1],post[term2])
                data_dict.update({key: posts})
            else:
                pass

        return data_dict


    # Find the intersection of the two terms
    def intersect(self,post1, post2):
        id_1 = 0  # for post 1 id's
        id_2 = 0  # for post 2 id's
        answer = []

        while id_1 < len(post1) and id_2 < len(post2):
            if post1[id_1] == post2[id_2]:
                answer.append(post1[id_1])
                id_1 += 1
                id_2 += 1
            elif post1[id_1] < post2[id_2]:
                id_1 += 1
            else:
                id_2 += 1

        if answer == []:
            return -1  # if no querys were made
        else:
            return answer


    # Find the intersection of the two terms
    def union(self,post1, post2):
        id_1 = 0 # for post 1 id's
        id_2 = 0 # for post 2 id's
        answer = []
        
        while id_1 < len(post1) and id_2 < len(post2):
            if post1[id_1] == post2[id_2]:
                answer.append(post1[id_1])
                id_1+=1
                id_2+=1
            elif post1[id_1] < post2[id_2]:
                answer.append(post1[id_1])
                id_1+=1
            else:
                answer.append(post1[id_1])
                id_2+=1

        if answer == []: return -1 # if no querys were made
        else: return answer


class InvertedIndex:

    def __init__(self):
        """ 
        - Create an empty inverted index
        - Create an empty term_Frequency (tf)
        - Create an empty document_frequency (df)
        - Create an instance of PortterStemmer
        - Initialize record id to 0 
        """
        self.inverted_lists = {}
        self.term_frequency = Counter()
        self.document_frequency = {}
        self.ps = PorterStemmer()
        self.record_id = 0

    # def read_from_file(self, documents):
    #     test = []
    #     for document in documents:
    #         with open(document) as file:
    #             for line in file:
    #                 test.append(line)

    #     document_words = [doc.split() for doc in test]
    #     vocab = sorted(set(sum(document_words, [])))
    #     vocab_dict = {k:i for i,k in enumerate(vocab)}


    #     X_tf = np.zeros((len(test), len(vocab)), dtype=int)
    #     for i,doc in enumerate(document_words):
    #         for word in doc:
    #             X_tf[i, vocab_dict[word]] += 1
        
    #     idf = np.log10((X_tf.shape[0])/(X_tf.astype(bool).sum(axis=0)))
        

    #     X_tfidf = X_tf * idf
    #     print(X_tfidf)

    #     scores_1 = np.dot(X_tfidf[1],X_tfidf[0])
    #     print (scores_1)


    def read_from_file(self, file_name):
        self.record_id += 1

        with open(file_name) as file:
            for line in file:
                 # First tokenize each file
                line = word_tokenize(line)
                for word in line:
                    # Stem the word
                    word = self.ps.stem(word)
                    if len(word) > 0:
                        word = word.lower()
                        self.termFrequency(word)
                        if word not in self.inverted_lists:
                            self.inverted_lists[word] = []
                        if self.record_id in self.inverted_lists[word]:
                            continue
                        self.inverted_lists[word].append(self.record_id)
        
        """ Call document frequency to store the result term Frequency"""
        self.documentFrequency() 
    
    def termFrequency(self,word):
        """ Get the frequcies for each of the id """
        self.term_frequency[word] += 1 
     
    def documentFrequency(self):
        """ This is called after we get the term frquency for each the doc """
        self.document_frequency[str(self.record_id)] = self.term_frequency
        self.term_frequency = Counter()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 inverted_index.py <file name> <file name> ...")
        sys.exit(1)
    files = []
    file_name1 = sys.argv[1]
    file_name2 = sys.argv[2]
    file_name3 = sys.argv[3]
    file_name4 = sys.argv[4]
    file_name5 = sys.argv[5]
    file_name6 = sys.argv[6]
    files.append(file_name1)
    files.append(file_name2)
    files.append(file_name3)
    files.append(file_name4)
    files.append(file_name5)
    files.append(file_name6)
    ii = InvertedIndex()
    ii.read_from_file(files)
    # ii.read_from_file(file_name1)
    # ii.read_from_file(file_name2)

    # print("\t\t\t\tTerms and its frequencies")
    # for document, term_frequency in ii.document_frequency.items():
    #     print("\nDocument %s"%(document))
    #     for term, frequency in term_frequency.items():
    #         print("\t%s : %d" % (term, frequency))
    # for word, inverted_list in ii.inverted_lists.items():
    #     print("%s\t%s" % (word, inverted_list))
        # print("%s\t%d" % (word, len(inverted_list)))
