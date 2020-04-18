cookbook = {'cake': {'name': 'cake', 'ingredients': 'flour, sugar, eggs', 'meal': 'dessert','prep_time': '60'},
          'sandwich': {'name': 'sandwich', 'ingredients': 'ham, bread, cheese, tomatoes', 'meal': 'lunch','prep_time': '10'},
		  'ingredients': {'name': 'salad', 'ingredients': 'avocado, arugula, tomatoes, spinach', 'meal': 'lunch','prep_time': '15'}}
while True:
	print('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>>')
	x = int(input())
	if x == 1:
		print("Please enter name of the recipe\n>>")
		i = input()
		cookbook[i] = {}
		cookbook[i]['name'] = i
		print("Please enter ingredients of the recipe\n>>")
		cookbook[i]['ingredients'] = input()
		print("Please enter type of the meal\n>>")
		cookbook[i]['meal'] = input()
		print("Please enter preparation time of the meal\n>>")
		cookbook[i]['prep_time'] = input()
		print(cookbook[i])
	elif x == 2:
		print("Which recipe you want to delete?\n>>")
		recipe = input()
		if cookbook[recipe]['name'] == recipe:
			del(cookbook[recipe])
	elif x == 3:
		print("Please enter the recipe's name to get its details:\n>>")
		i = input()
		if cookbook[i]['name'] == i:
			print('Recipe for:', cookbook[i]['name'])
			print('Ingredients list: ',cookbook[i]['ingredients'])
			print('To be eaten for', cookbook[i]['meal'], '.')
			print('Takes', cookbook[i]['prep_time'], 'minutes of cooking.')
	elif x == 4:
		for i in cookbook:
			print(cookbook[i]['name'])
	elif x == 5:
		break