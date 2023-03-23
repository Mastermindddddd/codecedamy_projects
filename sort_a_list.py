ef sort_a_list(*numbers, decider):
	if decider == 'asc':
		return sorted(numbers)

	if decider == 'desc':
		return sorted(numbers, reverse=True)

	if decider == 'none':
		return numbers

sort_a_list(4,5,6,7,1,2,3,0,7,43,54, decider = 'desc')
