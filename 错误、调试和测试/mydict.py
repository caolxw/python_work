# -*- coding: utf-8 -*-
#单元测试

class Dict(dict):
	"""docstring for Dict"""
	def __init__(self, **kw):
		super().__init__(**kw)
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError

	def __setattr__(self, key, value):
		self[key] = value
		