# -*- coding: utf-8 -*-

#创立对象
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age):
		
		self.name = name
		self.age = age

	#定义一个方法
	def show_infor(self):
		print('name:',self.name,'\nage: %s'% self.age)

bart = Student('Bob',20)
bart.show_infor()
bart.score = 80#python允许对实例对象绑定任何数据
print('score:',bart.score)