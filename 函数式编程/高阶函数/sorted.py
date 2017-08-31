#排序算法
#sorted()
L = [5, 30, -10, -3, 9]
print(L)
print(sorted(L))

print(sorted(L, key=abs))#按照绝对值大小比较
print('\n')

s = ['Adam', 'hello', 'OK', 'someThing','adam']
print(s)
print(sorted(s))
print(sorted(s, key=str.lower))#忽略大小写比较
print(sorted(s, key=str.lower, reverse=True))#忽略大小写比较,并反向排序
print('\n')

student = [('Bob',80), ('Jack', 90), ('Lisa', 85), ('Adam', 67)]
 #按名字排序
def by_name(t):
 	return t[0]
#按成绩排序
def by_score(t):
	return t[1]
print(sorted(student, key=by_name))
print(sorted(student, key=by_score, reverse=True))