import pandas as pd

def howManyMedals(data, name):
	df = data[["Year", "Name", "Medal"]]
	df2 = df.loc[df.Name == name, ['Year', 'Medal']]
	df2.dropna(subset=['Medal'], inplace=True)
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
"""
name = 'Kjetil Andr Aamodt'
path = '../data/athlete_events.csv'
data = pd.read_csv(path, sep=",")

#df2 = df2.groupby("Year")["Medal"].count()
#df2 = df2.groupby(["Medal"]).count()
#df2 = df2["Year"].groupby(df2["Medal"]).count()
#df2 = df2.groupby("Year").count()
#print(df2)
#df2 = df2.groupby("Medal").count()
#print(df2.to_dict())

G_df = df2[df2["Medal"] == 'Gold']
#S_df = df2[df2["Medal"] == 'Silver']
#B_df = df2[df2["Medal"] == 'Bronze']
#print(G_df)
#print(G_df.shape[0])
print(G_df)
print(G_df.groupby("Year")["Medal"].count())
"""