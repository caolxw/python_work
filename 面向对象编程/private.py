# -*- codeing: utf-8 -*-

#建立私有变量
class Stuend(object):
	"""docstring for Stuend"""
	def __init__(self, name, score):
		
		self.__name = name
		self.__score = score#在外部不可以修改这两个变量的值
#要在外部获得值
	def get_name(self):
		return self.__name

	def get_score(self):
		return 	self.__score
#在外部修改值
	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

bart = Stuend('Jack',90)
print('%s %s'%(bart.get_name(), bart.get_score()))
bart.set_name('Jeason')
bart.set_score(89)
print('%s %s'%(bart.get_name(), bart.get_score()))
bart.set_score(101)