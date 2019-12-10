__author__ = 'Nick Hirakawa'
import re



class CorpusParser:

	def __init__(self, files):
		self.files = files
		#self.regex = re.compile('^#\s*\d+')
		self.corpus = dict()

	def parse(self):
		for i in range(len(self.files)):
			doc = self.files[i]
			self.corpus[str(i+1)] = doc.split()

	def get_corpus(self):
		return self.corpus


class QueryParser:

	def __init__(self, filename):
		self.filename = filename
		self.queries = []

	def parse(self):
		with open(self.filename) as f:
			lines = ''.join(f.readlines())
		self.queries = [x.rstrip().split() for x in lines.split('\n')[:-1]]
		

	def get_queries(self):
		return self.queries


