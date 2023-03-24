def calculator(num1:int, operator, num2:int):
	if operator == '+':
		return num1 + num2

	elif operator == '-':
		return num1 - num2

	elif operator == '/':
		return num1 / num2

	elif operator == 'or':
		return num1 or num2

calculator(4, 'or', 5)
