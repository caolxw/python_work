# -*- coding: utf-8 -*-
#断言 assert

def foo(s):
	n = int(s)
	assert n != 0 #断言失败，会自动抛出异常
	return 10 / n

a = input()
print(foo(a))

#可以用 -0 来关闭assert
#python -0 test3.py