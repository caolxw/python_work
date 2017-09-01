def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

#若返回一个列表，列表的每个元素都是函数
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1, f2, f3 = count()
print (f1())
print (f2())
print (f3())
#结果全部都是9
#每次返回的函数地址存放在fs列表里,在最后调用的时候变量i指向3，所以所有结果都是9

#如果一定要引用循环
def count2():
	def f2(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f2(i))
	return fs

f4, f5, f6 = count2()
print(f4())
print(f5())
print(f6())
#当i=1时，f2(1)即让j指向1，
#当i=2时，f2(2)即让j指向2，此时j不是count的局部变量，不会影响到i=1是f(1)中j的指向。即函数f的参数绑定循环变量当前的值, 而不是循环变量本身。