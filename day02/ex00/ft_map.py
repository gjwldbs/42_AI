def ft_map(function_to_apply, list_of_inputs):
	pass
#C style
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
	squared.append(i * 2)
print(squared)
#Python style
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * 2, items))
print(squared)
"""
Even type can be changed
ex) map(str, items)
"""