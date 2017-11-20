import sha, itertools

class Challenge():
	def __init__(self, difficulty=9, charset='ABCDEFGHIJKabcdefghijk'):
		self.zeros = difficulty
		self.charset = charset
	
	def hashcash_hash(self, h):
		return int(sha.new(h).hexdigest(), 16)
	
	def tokens(self):
	    for n in itertools.count(1):
	        for c in itertools.combinations(self.charset, n):
				yield ''.join(c)
	
	def number_of_zeros(self, h):
		if h <= 0: return 0
		for i in itertools.count(0):
			if h & (1<<i): return i
		
	def generate(self, s):
		h = sha.new(s).digest()
		for t in self.tokens():
			if self.number_of_zeros(self.hashcash_hash(h+t)) == self.zeros: return t

	def validate(self, s, token):
		return self.number_of_zeros(self.hashcash_hash(sha.new(s).digest() + token))
