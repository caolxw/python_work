# -*- coding: utf-8 -*-

# @property装饰器作用：把一个方法变成属性调用
class Student(object):
	
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('Score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('Score must between 0~100')
		self._score = value

	#定义一个制度属性
	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value


	@property
	def age(self):
		return 2017 - self._birth

s = Student()
s.score = 60
print(s.score)
#会报错 s.score = 120

s.birth = 1998
print(s.age)
#s.age = 20
#print(s.age)#会报错，不能设置

#小练习
class Screen(object):
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height

#test
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?'% s.resolution
# assert 断言 用来测试表示式，其返回值为假，就会触发异常。


