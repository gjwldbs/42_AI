import pandas as pd

def youngestFellah(data, year):
	df = data[["Year", "Sex", "Age"]]
	df_f = df[(df["Year"] == year) & (df["Sex"] == 'F')]
	df_m = df[(df["Year"] == year) & (df["Sex"] == 'M')]
	f_younge = df_f.min()['Age']
	m_younge = df_m.min()['Age']
	print("{{'f': {}, 'm': {}}}".format(f_younge, m_younge))
