def hide_numbers(credit_card):
	last_four_digits = credit_card[-4:]
	print('************' + last_four_digits)
	return '************' + last_four_digits

hide_numbers('98147647864677')
