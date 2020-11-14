class Website:
	def __init__(self):
		self.length = 0
		self.data = {}

	def add(self, item):
		self.data[self.length] = item
		self.length+=1

