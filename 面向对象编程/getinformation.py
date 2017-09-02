# -*-coding: utf-8 -*-
class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self):
		self.y = 9
	def power(self):
		return self.y * self.y

#测试对象的属性
obj = MyObject()

if hasattr(obj, 'x'):#有属性‘x’吗
	print(obj.x)
else:
	setattr(obj, 'x', 19)#设置属性x
	print(getattr(obj, 'x'))#获取属性x
#获得对象的方法
if hasattr(obj, 'power'):
	fn = getattr(obj, 'power')
	print(fn())