# -*- coding: utf-8 -*-
#捕捉错误
try:
	print('try...')
	a = input()
	r = 10 / int(a)
	print('result:',r)
except ValueError as e:
	print('ValuError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
else:
	print('no error')
finally:
	print('finally')
print('END')

#try...catch 可以跳跃多层调用