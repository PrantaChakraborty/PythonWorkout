def my_sum(*args):
	result = 0
	for number in args:
		result += number
	return result
	
print(my_sum(1, 2, 3, 4))
