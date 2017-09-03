# -*- coding: utf-8 -*-

#限制class里的属性
class Student(object):
	"""docstring for Student"""
	__slots__ = ('name', 'age')
	

s = Student()
s.name = 'Jack'
s.age = 20
#s.job = 'doctor' #不能绑定job属性，会报错
print('%s %s'% (s.name, s.age))

class Graduate(Student):
	"""docstring for Graduate"""
	
	
s2 = Graduate()
s2.job = 'teacher' #__slots__定义的属性对子类没有作用
print(s2.job)	