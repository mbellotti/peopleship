import peopleship.libs.proofofwork as proof

class TestProofofWork():
	
	def test_zeros(self):
		c = proof.Challenge()
		assert c.number_of_zeros(12) == 2
	
	def test_charset(self):
		'''Set a different charset and test that the token returned has only those characters'''
		c = proof.Challenge(3, "123456789")
		t = c.generate('test')
		chars = set('ABCDEFGHIJKabcdefghijk')
		assert not any([(c in chars) for c in t])
	
	def test_full_process(self):
		s = 'hello world, please make me a hash'
		c = proof.Challenge()
		t = c.generate(s)
		assert c.validate(s,t) == 9