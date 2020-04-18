import sys
import string

if not (sys.argv[2]).isdigit() or (sys.argv[1]).isdigit():
	print("Error")
else:
	sentence = sys.argv[1]
	words = sentence.split(' ')
	wordcnt = sentence.count(' ') + 1
	i = 0
	while i < wordcnt:
		if len(words[i].strip(string.punctuation)) > int(sys.argv[2]):
			print(words[i].strip(string.punctuation))
		i += 1
