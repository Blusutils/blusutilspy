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
				 is (is literal), in (in literal), it (is instance of class, isinstance func), 
				ic (is subclass of class, issubclass func).
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
														# юхху, лесенка из тернарок!
	def __exit__(self, exc_type, exc_value, exc_traceback):
		pass

class globalswitch(switch):
	"""Switch/Case construction for global usage. Supports __call__
	
	Example usage:
	```py
	switch = globalswitch() # globalswitch with '==' mode
	with switch("str") as case:
		... # your checks
	```"""
	def __init__(self, match: object = None, *, mode: str = 'eq') -> None:
		"""Initialize GlobalSwitch object

		Args:
			match (Any): Object to check equality
			mode (str, optional): Mode for equality check. 
				Available modes: eq (==), ne (!=), gt (>), ge (>=), lo (<), le (<=),  
				 is (is literal), in (in literal), it (is instance of class, isinstance func), 
				ic (is subclass of class, issubclass func).
				 Defaults to 'eq' ('equals', == literal).

		Raises:
			TypeError: provided parameter "mode" isn't a string (i. e. it is NoneType or integer)
		"""
		super().__init__(match, mode = mode)

	def __call__(self, match: object = None, *, mode: str = None):
		"""Update object to check equality using funtion-like call

		Args:
			match (object): Object to replace already setted object for check
		"""
		self.match = match or self.match
		if mode is None: return
		if not isinstance(mode, str):
			raise TypeError(f'parameter must be {str}')
		self.mode = mode.lower()