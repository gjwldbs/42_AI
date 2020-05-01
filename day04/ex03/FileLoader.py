import pandas as pd

class FileLoader:
	def load(self, path):
		data = pd.read_csv(path, sep=",")
		print("Loading dataset of dimesions {} x {}".format(data.shape[0],data.shape[1]))
		return data
	def display(self, df, n):
		if n > 0:
			return df.head(n)
		elif n < 0:
			return df.tail(1)