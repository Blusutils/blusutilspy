def mixColors(colors) -> int:
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