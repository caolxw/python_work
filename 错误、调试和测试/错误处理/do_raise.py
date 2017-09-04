# -*- coding: utf-8 -*-

#抛出错误
def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value: %s'% s)
	return 10 / n

def bar():
	try:
		f00('0')
	except ValueError as e:
		print('ValueError!')
		raise
bar()
		