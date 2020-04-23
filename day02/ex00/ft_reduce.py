from functools import reduce
#from python-3 'reduce' is not a built in func anymore
def ft_reduce(function_to_apply, list_of_inputs):
	pass
#C style
def f(x, y):
	return x + y
a = [1, 2, 3, 4, 5]
result = 0
result = reduce(f, a)
print(result)
#Python style
a = [1, 2, 3, 4, 5]
result = 0
result = reduce(lambda x, y: x + y, a)
print(result)