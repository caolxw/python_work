# -*- coding: utf-8 -*-
#decorator
def log(func):
	def wrapper(*args, **kw):#wrapper可以接受任意参数的调用
		print('call %s()：'%func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2017-9-1')

now()#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志

#针对带有参数的decorator:
import functools
def log2(text = 'call'):
	def decorator(func):
		@functools.wraps(func)
		def wrapper2(*args, **kw):
			print('%s %s():'% (text, func.__name__))
			return func(*args, **kw)
		return wrapper2
	return decorator

@log2('begin')
def call():
	print('2017-9-1')
call()

@log2('end')
def call():
	print('2017-9-1')
call()

@log2()
def f():
	print('Hello,world!')
f()