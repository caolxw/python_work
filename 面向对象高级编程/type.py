# -*- coding: utf-8 -*-

#用type()创建一个class对象
def fn(self, name = 'world'):
	print('Hello,',name)
Hello = type('Hello', (object,), dict(hello = fn))
#test
h = Hello()
h.hello()