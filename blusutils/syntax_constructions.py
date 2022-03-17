"""Module with syntax constructions
"""
class switch:
	"""Switch/Case construction for multiple equality based on context managers"""
	def __init__(self, match: object, *, mode: str = 'eq') -> None:
		"""Initialize Switch object

		Args:
			match (Any): Object to check equality
			mode (str, optional): Mode for equality check. 
				Available modes: eq (==), ne (!=), gt (>), ge (>=), lo (<), le (<=),  
				 is (is literal), in (in literal), it (is instance, isinstance func), 
				ic (is subclass, issubclass func)
				 Defaults to 'eq' ('equals', == literal).

		Raises:
			TypeError: provided parameter "mode" isn't a string (i. e. it is NoneType or integer)
		"""
		self.match = match
		if not isinstance(mode, str):
			raise TypeError(f'parameter must be {str}')
		self.mode = mode.lower()
	def __enter__(self) -> None:
		# fuck
		return (lambda match: match == self.match) if self.mode == 'eq' or self.mode == '==' \
			else (lambda match: match != self.match) if self.mode == 'ne' or self.mode == '!=' \
				else (lambda match: match > self.match) if self.mode == 'gt' or self.mode == '>' \
					else (lambda match: match >= self.match) if self.mode == 'ge' or self.mode == '>=' \
						else (lambda match: match < self.match) if self.mode == 'lo' or self.mode == '<' \
							else (lambda match: match <= self.match) if self.mode == 'le' or self.mode == '<=' \
								else (lambda match: match is self.match) if self.mode == 'is' \
									else (lambda match: match in self.match) if self.mode == 'in' \
										else (lambda match: isinstance(self.match, match)) if self.mode == 'it' or self.mode == 'isinstance' \
											else (lambda match: issubclass(self.match, match)) if self.mode == 'ic' or self.mode == 'issubclass' \
													else None
														# юхху, лесенка
	def __exit__(self, exc_type, exc_value, exc_traceback):
		pass