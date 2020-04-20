
class Evaluator:
	@staticmethod
	def zip_evaluate(coef, words):
		if len(words) != len(coef):
			return -1
		lst = list(zip(coef, words))
		addsum = 0
		for i in lst:
			addsum += i[0] * len(i[1])
		return addsum
	def enumerate_evaluate(coef, words):
		if len(words) != len(coef):
			return -1
		addsum = 0
		lst = enumerate(words)
		for i, words in lst:
			addsum += len(words) * coef[i]
		return addsum

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))
words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))