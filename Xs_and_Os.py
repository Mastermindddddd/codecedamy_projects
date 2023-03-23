def counting_Xs_and_Os(string):
	countX = 0
	countY = 0

	#counts the number of X's in a string
	for letter in string:
		if letter == 'X':
			countX += 1

	for letter in string:
		if letter == 'Y':
			countY += 1

	if countX == countY:
		return True

	else:
		return False

counting_Xs_and_Os('1xxOnXhymOHGTXhygXnmtXjjhO')
