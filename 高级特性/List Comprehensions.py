# -*- coding: utf-8 -*-

#列表生成式
L1 = [x * x for x in range(1,11)]
print(L1)

#for循环后面还可以加上判断
L2 = [x + x for x in range(1,21) if x % 3 == 0]
print(L2)

d = {'A': 'Adam', 'B': 'Bob', 'C': 'Candy'}
L3 = [k + '=' + v for k, v in d.items()]
for x in L3:
	print(x)
print('\n')

#把list中所有字符串变成小写
L4 = [s.lower() for s in d.values()]
print(L4)

L = ['Hello','World',18,'Apple',None]
print(L)
print('\n')
#找出字符串元素并转换成小写
l = [s.lower() for s in L if isinstance(s, str)]
print(l)