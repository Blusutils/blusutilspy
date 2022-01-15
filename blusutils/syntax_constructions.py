import asyncio
class switch:
	"""Switch/Case construction for multiple equality based on context managers"""
	def __init__(self, match: object, *, mode: str = 'eq') -> None:
		"""Modes: eq (==), ne (!=), gt (>), ge (>=), lo (<), le (<=), is (is literal), in (in literal), it (is instance, isinstance func), sc (is subclass, issubclass func), ic (is corotinue, iscorotinue func"""
		self.match = match
		if mode is None:
			raise TypeError('NoneType object can not be a mode parameter')
		self.mode = mode.lower()
	def __enter__(self) -> None:
		# fuck
		return self.is_equal if self.mode == 'eq' or self.mode == '==' \
			else self.is_not_equal if self.mode == 'ne' or self.mode == '!=' \
				else self.is_greater if self.mode == 'gt' or self.mode == '>' \
					else self.is_greater_or_equal if self.mode == 'ge' or self.mode == '>=' \
						else self.is_lower if self.mode == 'lo' or self.mode == '<' \
							else self.is_lower_or_equal if self.mode == 'le' or self.mode == '<=' \
								else self.is_is if self.mode == 'is' \
									else self.is_in if self.mode == 'in' \
										else self.is_instance if self.mode == 'it' or self.mode == 'isinstance' \
											else self.is_subclass if self.mode == 'sc' or self.mode == 'issubclass' \
												else self.is_corotinue if self.mode == 'ic' or self.mode == 'iscoroutine' \
													else None
														# юхху, лесенка
	def is_equal(self, val) -> bool:
		return val == self.match
	def is_not_equal(self, val) -> bool:
		return val != self.match
	def is_greater(self, val) -> bool:
		return val > self.match
	def is_greater_or_equal(self, val) -> bool:
		return val >= self.match
	def is_lower(self, val) -> bool:
		return val < self.match
	def is_lower_or_equal(self, val) -> bool:
		return val <= self.match
	def is_is(self, val) ->  bool: # XD is_is
		return val is self.match
	def is_in(self, val) -> bool:
		return val in self.match
	def is_instance(self, val) -> bool:
		return isinstance(self.match, val)
	def is_subclass(self, val) -> bool:
		return issubclass(self.match, val)
	def is_corotinue(self, val) -> bool:
		return asyncio.coroutines.iscoroutine(self.match, val)
	def __exit__(self, exc_type, exc_value, exc_traceback):
		pass