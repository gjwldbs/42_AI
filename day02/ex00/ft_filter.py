def ft_filter(function_to_apply, list_of_inputs):
	pass
#C style
target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
def is_even(n):
	return True if n % 2 == 0 else False
for value in target:
	if is_even(value):
		result.append(value)
print(result)
#Python style
target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, target))
print(result)