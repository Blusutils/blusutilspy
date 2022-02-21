"""Module with other type of utils
"""
import typing, datetime, math
def mix_colors(colors: typing.Union[list, tuple, set]) -> int:
	"""Shitty color mixer for RGB (not RGBA).

	Args:
		colors (typing.Union[list, tuple, set]): collection (list, tuple or set) with three colors: Red, Green, and Blue.

	Raises:
		TypeError: provided collection not is list, tuple or set.

	Returns:
		int: mixed color (withount channels, you can convert to hex-like string using hex() and parse color channels)
	"""
	if not type(colors) in [list, tuple, set]: raise TypeError(f"{type(colors)} not an iterable collection")
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
	if fst > 0xFF:
		fst = 0xFF
	if scd >  0xFF:
		scd = 0xFF
	if thd > 0xFF:
		thd = 0xFF
	return int(hex(fst)[2:]+hex(scd)[2:]+hex(thd)[2:], 16)

class Metrics:
    """Enumeration for information quantity units.
    """
    Bits = 1
    Bytes = Bits*8
    Kilobytes = Bytes*1024
    Megabytes = Kilobytes*1024
    Gigabytes = Megabytes*1024
    Terabytes = Gigabytes*1024
    Petabytes = Terabytes*1024

def calculate_downloading_time(upcoming: float, speed: float, metrics: typing.Tuple[int, int] = (Metrics.Bytes, Metrics.Bytes))->typing.Tuple[int, int, int, float]:
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