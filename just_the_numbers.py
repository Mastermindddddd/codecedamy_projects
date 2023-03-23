def only_numbers(*list):
	intergers = []
	
	for num in list:
		if isinstance(num, int) and num >= 0:
			intergers.append(num)
	return intergers

only_numbers(1,'eggs',4,'dog',5,'g',9,43,55,'fg',5,'g',5,6,6)
