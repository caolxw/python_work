#高阶函数
#把函数作为参数传入，这样的函数称为高阶函数

#map()
#参数：函数 和 Iterable
#返回：Iterable
def f(x):
	return x * x * x

L = list(range(11))
l = map(f,L)
print(list(l))

#reduce()
from functools import reduce
def add(x,y):
	return x * 10 + y

t = reduce(add, [1,3,4,5])
print(t)#把序列变成整数
print('\n')

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
	return name.capitalize();
L = ['ADAM', 'bob', 'JAck', 'jeaSon']
print(list(map(normalize, L)))

#请编写一个prod()函数，可以接受一个list并利用reduce()求积
def fn(x,y):
	return x * y
def prod(L):
	return reduce(fn, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

