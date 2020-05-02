import pandas as pd

def howManyMedalsByCountry(data, team):
	df = data[["Year", "Team", "Medal"]]
	df2 = df.loc[df.Team == team, ['Year', 'Medal']]
	df2.dropna(subset=['Medal'], inplace=True)
	df2 = df2.drop_duplicates()
	res = {}
	for index, row in df2.iterrows():
		if row['Year'] not in res.keys():
			res[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
		if row['Medal'] == 'Gold':
			res[row['Year']]['G'] += 1
		elif row['Medal'] == 'Silver':
			res[row['Year']]['S'] += 1
		elif row['Medal'] == 'Bronze':
			res[row['Year']]['B'] += 1
	return res