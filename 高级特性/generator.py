# -*-coding: utf-8 -*-
#生成器
g = (x * x * x for x in range(10))
for n in g:
	print(n)
print('\n')

#打印斐波拉契数列
def fib(max):
	n, a, b = 0, 0 ,1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
for x in fib(10):
	print(x)
print('\n')
#打印杨辉三角
def tringles(line):
	n = 1
	L = [1]
	while n < line + 1:
		yield L
		L1 = [1]#定义新的list
		for i in range(0, len(L) - 1):
			L1.append(L[i] + L[i + 1])
			i = i + 1
		L1.append(1)
		L = L1
		n = n + 1
	return 'done'
for x in tringles(10):
	print(x)