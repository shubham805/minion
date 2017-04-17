import nltk
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import pprint
class Query(object):
	"""docstring for Query"""
	sentence = ""
	tags = {}
	nounP = {}
	VerbP = {}
	intent = {}
	grammar = "NP: {<DT>?<JJ>*<NN>*}"

	def __init__(self, s):
		super(Query, self).__init__()
		self.sentence = s
	
	def parse_sentence(self):
		s = word_tokenize(self.sentence)
		self.tags = nltk.pos_tag(s)
		return self.tags

	def name_recognition(self):
		self.parse_sentence()
		return nltk.ne_chunk(self.tags, binary=True)	

	def noun_phrase(self):
		self.parse_sentence()
		result = nltk.chunk.ne_chunk(self.tags, binary = True)
		result.draw()
		return result	
		
q = Query("Who launched Cashless India Mission and Gheto?")
pprint.pprint(q.noun_phrase())