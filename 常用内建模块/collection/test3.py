# -*- coding: utf-8 -*-

#实现一个先入先出的dict 当容量超出限制，先删除最早添加的Key

from collections import OrderedDict

class LastUpdateOrderedDict(OrderedDict):
	"""docstring for LastUpdateOrderedDict"""
	def __init__(self, capacity):
		super(LastUpdateOrderedDict, self).__init__()
		self.capacity = capacity

	def __setitm__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity :
			last = self.popitem(last=Flase)
			print('remove:',last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitm__(self, key, value)