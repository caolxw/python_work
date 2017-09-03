# -*- coding: utf-8 -*-

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)'% self.name
	__repr__ = __str__
#__str__()返回用户看到的字符串
#__repr__()返回程序开发者看到的字符串

print(Student('Michael'))

#__iter__()返回一个迭代对象
class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a = 0
		self.b = 1
	def __iter__(self):
		return self #本身就是迭代对象，返回自己
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100:
			raise StopIteration()
		return self.a

for n in Fib():
	print(n)

#__getitem__()可以像list一样按照下标取出元素，也可以进行切片
class MoreFib(object):
	def __getitem__(self,n):
		if isinstance(n,int):#n是索引
			a,b = 1,1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):#n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L

f = MoreFib()
print('f[3] = %d'%f[3])
print(f[:10])
print(f[2:6])

#在实例本身上调用函数
class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s'% self.name)

p = Person('Ruby')
p()
