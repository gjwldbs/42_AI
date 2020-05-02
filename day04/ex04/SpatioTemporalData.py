import pandas as pd

class SpatioTemporalData:
	def __init__(self, data):
		self.data = data
	def when(self, location):
		df = self.data.loc[self.data.City == location,'Year'].unique()
		return df
	def where(self, date):
		df = self.data.loc[self.data.Year == date,'City'].unique()
		return df
