import random

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
i = random.randint(1, 99)
cnt = 0
while True:
	print("\nWhat's your guess between 1 and 99?\n>>")
	x = input()
	if x == "exit":
		print("Goodbye!")
		break
	#elif (x.isalpha()):
	#	print("That's not a number.")
	#	cnt += 1
	elif i < x:
		print("Too high!")
		cnt += 1
	elif i > x:
		print("Too low!")
		cnt += 1
	elif x == 42:
		print("The answer to the ultimate question of life, the universe and everything is 42. Congratulations! You got it on your first try!")
		break
	elif x == i:
		cnt += 1
		print("Congratulations, you've got it!")
		print("You won in ", cnt," attempts!")
		break