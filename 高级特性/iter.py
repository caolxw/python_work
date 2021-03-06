# -*- coding: utf-8 -*-
from collections import Iterable, Iterator

print('Iterable? [1,2,3]', isinstance([1,2,3],Iterable))
print('Iterator? [1,2,3]', isinstance([1,2,3],Iterator))
print('Iterator? iter([1,2,3])', isinstance(iter([1,2,3]),Iterator))
print('\n')
#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

#iter list with index
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A',  'B', 'C']):
	print(i, value)