"""Module with other type of utils
"""
import typing
import datetime
import math
import traceback
import enum

def mix_colors(colors: typing.Union[list, tuple, set]) -> int:
	"""Shitty color mixer for RGB (not RGBA).

	Args:
		colors (typing.Union[list, tuple, set]): collection (list, tuple or set) with three colors: Red, Green, and Blue.

	Raises:
		TypeError: provided collection not is list, tuple or set.

	Returns:
		int: mixed color (withount channels, you can convert to hex-like string using hex() and parse color channels)
	"""
	if not type(colors) in [list, tuple, set]: raise TypeError(f"{type(colors)} is not an {list}, {tuple} or {set}")
	fst = 0x0
	scd = 0x0
	thd = 0x0
	for color in colors:
		if fst < 0xFF:
			clr = hex(color)[2:4] if len(color)>6 else color[2:4]
			fst = int(clr, 16) + fst
		if scd < 0xFF:
			clr2 = hex(color)[4:6] if len(color)>6 else color[4:6]
			scd = int(clr2, 16) + scd
		if thd < 0xFF:
			clr3 = hex(color)[6:8] if len(color)>6 else color[6:8] 
			thd = int(clr3, 16) + thd
	if fst > 0xFF: fst = 0xFF
	if scd >  0xFF: scd = 0xFF
	if thd > 0xFF: thd = 0xFF
	return int(hex(fst)[2:]+hex(scd)[2:]+hex(thd)[2:], 16)

class InformationUnits(enum.Enum):
	"""Enumeration for information quantity units.
	"""
	Bits = 1
	Bytes = Bits*8

	Kibibytes = Bytes*1024
	Mebibytes = Kibibytes*1024
	Gibibytes = Mebibytes*1024
	Tebibytes = Gibibytes*1024
	Pebibytes = Tebibytes*1024

	Kilobytes = Bytes*1000
	Megabytes = Kilobytes*1000
	Gigabytes = Megabytes*1000
	Terabytes = Gigabytes*1000
	Petabytes = Terabytes*1000

	Kibibits = Kibibytes/8
	Mebibits = Mebibytes/8
	Gibibits = Gibibytes/8
	Tebibits = Tebibytes/8
	Pebibits = Pebibytes/8

	Kilobits = Kilobytes/8
	Megabits = Megabytes/8
	Gigabits = Megabits/8
	Terabits = Gigabytes/8
	Petabits = Terabytes/8

def calculate_downloading_time(upcoming: float, speed: float, metrics: typing.Tuple[int, int] = (InformationUnits.Bytes, InformationUnits.Bytes))->typing.Tuple[int, int, int, float]:
	"""Calculate time what you will need to download file(s).

	Args:
		upcoming (float): Size of upcoming file.
		speed (float): Your "download" speed of internet connection.
		metrics (tuple[int, int], optional): A tuple of unit types for the amount of information. The first is the unit for the file size, the second for the speed. Defaults to (Metrics.Bytes, Metrics.Bytes).

	Returns:
		tuple[int, int, int, float]: A tuple consisting of the values of hours (integer), minutes (integer), seconds (integer), and the total number of seconds (float).
	"""
	upcoming = upcoming*metrics[0]
	speed = speed*metrics[1]
	seconds = upcoming//speed
	h = math.floor(seconds/60/60)
	m = math.floor(((seconds-(h*60*60))/60))
	s = math.floor(seconds-(h*60*60)-(m*60))
	return h, m, s, seconds

def anywhere_raise(exc: Exception):
	"""Raises an exception in any place. It may be needed in ternary line (val if condition else __raise__) or in any other place where "raise" can't be used.

	Args:
		exc (Exception): An exception to raise.

	Raises:
		exc: Provided exception.
	"""
	raise exc # genius

def safe_raise(exc: Exception):
	"""Safetly raises an exception. It may be needed when you want to warn user, but not to stop code. Cannot be catched in "try/except".

	Args:
		exc (Exception): Exception to "raise".

	Returns:
		Exception: Passed exception.
	"""
	print(traceback.format_exc(exc)) # also genius
	return exc
