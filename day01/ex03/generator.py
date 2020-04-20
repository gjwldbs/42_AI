import random

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	word = text.split(sep)
	if option == "shuffle":
		random.shuffle(word)
	elif option == "ordered":
		word.sort(key = str.swapcase)
	elif option == "unique":
		word = list(set(word))
	elif not isinstance(text, str) or option != None:
		return 'ERROR'
	return word
