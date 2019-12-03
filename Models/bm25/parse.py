__author__ = 'Nick Hirakawa'
import re



class CorpusParser:

	def __init__(self, files):
		self.files = files
		#self.regex = re.compile('^#\s*\d+')
		self.corpus = dict()

	# def parse(self):
	# 	with open(self.files, encoding="'ISO-8859-1'") as f:
	# 		s = ''.join(f.readlines())
	# 	blobs = s.split('#')[1:]
	# 	for x in blobs:
	# 		text = x.split()
	# 		docid = text.pop(0)
	# 		self.corpus[docid] = text

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


if __name__ == '__main__':
	corpus = read_json.ReadFiles()
	corpus = corpus.get_list()
	# cp = CorpusParser(files=courpus)
	# cp.parse()
	# courpus = cp.get_corpus()
	
	# for key,value in courpus.items():
	# 	if key < 10:
	# 		print("key: {}\nvalue: {}".format(key,value))
