# -*- coding: utf-8 -*-

class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print('Animal is running...')
class Dog(Animal):
	"""docstring for Dog"""
	#Dog继承了Animal
	pass

a = Animal()
a.run()
d = Dog()
d.run()
		
class Cat(Animal):
	"""docstring for Cat"""
	def run(self):
		#可以重写run方法
		print('Cat is running...')

	def eat(self):
		#子类也可以有自己的方法
		print('Cat is eating...')

c = Cat()
c.run()
c.eat()
#可以判断一个变量是否是某个类型
print('a 是 Animal类型：',isinstance(a, Animal))
print('a 是 Dog类型：',isinstance(a, Dog))
print('d 是 Animal类型：',isinstance(d, Animal))
print('d 是 Dog类型：',isinstance(d, Dog))

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(c)
#不是Animal的子类
class Timer(object):
	"""docstring for Timer"""
	def run(self):
		print('Start...')

t = Timer()
run_twice(t)