# -*- coding: utf-8 -*-
#迭代
import itertools

#无限迭代器
natuals = itertools.count(1)
for n in natuals:
	print(n)
	while n >= 1000:
		exit()
#截取有序序列
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

#无限循环传入的序列
cs = itertools.cycle('abc')
for c in cs:
	print(c)

#限定重复次数
ns = itertools.repeat('a', 3)
for n in ns:
	print(n)