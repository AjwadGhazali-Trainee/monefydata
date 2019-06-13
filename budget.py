from config import DAILY

class Budget:
	def __init__(self, name='', percentage=0, frequency=DAILY, fixedExpense=0, categoryList=[]):
		self.name = name
		self.allocation = percentage
		self.frequency = frequency
		self.fixedExpense = fixedExpense
		self.categoryList = categoryList