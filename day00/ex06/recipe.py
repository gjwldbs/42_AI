cookbook = {1: {'name': 'cake', 'ingredients': 'flour, sugar, eggs', 'meal': 'dessert','prep_time': '60'},
          2: {'name': 'sandwich', 'ingredients': 'ham, bread, cheese, tomatoes', 'meal': 'lunch','prep_time': '10'},
		  3: {'name': 'salad', 'ingredients': 'avocado, arugula, tomatoes, spinach', 'meal': 'lunch','prep_time': '15'}}
i = 3
while True:
	print('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>>')
	x = int(input())
	if x == 1:
		cookbook[i] = {}
		print("Please enter name of the recipe\n>>")
		cookbook[i]['name'] = input()
		print("Please enter ingredients of the recipe\n>>")
		cookbook[i]['ingredients'] = input()
		print("Please enter type of the meal\n>>")
		cookbook[i]['meal'] = input()
		print("Please enter preparation time of the meal\n>>")
		cookbook[i]['prep_time'] = input()
		print(cookbook[i])
		i += 1
	elif x == 2:
		print("Which recipe you want to delete?\n>>")
		recipe = input()
		i =
		if cookbook[i]['name'] == recipe:
			del(cookbook[i])
	elif x == 3:
		print("Please enter the recipe's name to get its details:\n>>")
		n = input()
		if n == 'cake':
			i = 1
		elif n == 'sanwich':
			i = 2
		elif n == 'salad':
			i = 3
		print('Recipe for:', cookbook[i]['name'])
		print('Ingredients list: ',cookbook[i]['ingredients'])
		print('To be eaten for', cookbook[i]['meal'], '.')
		print('Takes', cookbook[i]['prep_time'], 'minutes of cooking.')
	elif x == 4:
		i = 0
		for i in cookbook:
			print(cookbook[i]['name'])
			i += 1
		break
	elif x == 5:
		break