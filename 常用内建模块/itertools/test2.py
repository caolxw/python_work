# -*- coding: utf-8 -*-

import itertools
#chain() 把迭代对象串联起来
for c in itertools.chain('abc', 'xyz'):
	print(c)

#groupby()把迭代器中的重复元素挑出来
for key, group in itertools.groupby('aabhddnbbba'):
	print(key, list(group))
