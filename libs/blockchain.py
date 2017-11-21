import json
from time import time

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.transactions = []
		
	def create_block(self):
		pass
	
	def new_transaction(self, d):
		pass
		
	@property
	def last_block(self):
		pass