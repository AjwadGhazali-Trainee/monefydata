from config import *

class Budget:
	def __init__(self, name=COMMON_DEFAULT_BUDGET_NAME,  alloc=0, categoryList=[]):
		self.name = name
		self.alloc = alloc
		self.categoryList = categoryList