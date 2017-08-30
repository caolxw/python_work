# -*- coding: utf-8 -*-

L = ['Jack','Sam','Adam','Lisa']
i = 0
#迭代
for x in L:
	i = i + 1
	print(i,x)
print('\n')

d = {'Jack': 20, 'Sam': 21, 'Adam': 19}
#迭代dict
print('迭代value')
for value in d.values():
	print(value)
print('迭代key, value')
for k, v in d.items():
	print(k,v)
print('\n')

#判断是否课迭代(整数不可以迭代)
from collections import Iterable
if isinstance(d,Iterable):
	for x in d:
		print(x)
