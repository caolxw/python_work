#创建偏函数
import functools
int2 = functools.partial(int, base = 2)#把int()函数中的base参数固定成2，返回这个函数到int2

print(int2('1010101'))