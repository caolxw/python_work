#filter用于过滤序列
#参数：函数和序列
#返回：Iterator

#用filter求素数
def _odd_iter():#构造从3开始的奇数序列
	n = 1
	while True:
		n = n + 2
		yield n

#定义一个筛选函数
def _not_divisible(n):
	return lambda x: x % n > 0 
	#lambda 定义了一个匿名函数 冒号前为参数，冒号后为函数体。可读性不高。

#定义一个生成器，不断返回下一个素数
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

#打印1000以内的素数
for n in primes():
	if n < 1000:
		print(n)
	else:
		break