__author__ = 'Nick Hirakawa'

from Models.bm25.parse import *
from Models.bm25.query import QueryProcessor
import operator


class BM25:
	""" This is the model for the BM25 """
	def __init__(self, corpus):
	 self.cp = CorpusParser(files=corpus)

	def search(self):
		self.qp = QueryParser(filename='Models/bm25/text/queries.txt')
		self.qp.parse()
		self.cp.parse()
		queries = self.qp.get_queries()
		proc = QueryProcessor(queries, self.cp.get_corpus())
		results = proc.run()
		qid = 0
		for result in results:
			sorted_x = sorted(result.items(), key=operator.itemgetter(1))
			sorted_x.reverse()
			index = 0
			for i in sorted_x[:10]:
				tmp = (i[0], index, i[1])
				print('{:>12}\t{:>12}\t{:>12}'.format(*tmp))
				index += 1
			qid += 1


# def main():
# 	qp = QueryParser(filename='Models/bm25/text/queries.txt')
# 	cp = CorpusParser(files='Models/bm25/text/corpus.txt')
# 	qp.parse()
# 	queries = qp.get_queries()
# 	cp.parse()
# 	corpus = cp.get_corpus()
# 	proc = QueryProcessor(queries, corpus)
# 	results = proc.run()
# 	qid = 0
# 	for result in results:
# 		sorted_x = sorted(result.items(), key=operator.itemgetter(1))
# 		sorted_x.reverse()
# 		index = 0
# 		for i in sorted_x[:10]:
# 			tmp = (i[0], index, i[1])
# 			print('{:>1}\t{:>2}\t{:>12}'.format(*tmp))
# 			index += 1
# 		qid += 1

