import pandas as pd

def proportionBySport(data, year, sport, sex):
	df = data[["Year", "Sex", "Name", "Sport"]]
	df = df.drop_duplicates(["Year","Name"])
	df2 = df[(df["Year"] == year) & (df["Sex"] == sex)]
	df3 = df2[df2["Sport"] == sport]
	return (df3.shape[0] / df2.shape[0])