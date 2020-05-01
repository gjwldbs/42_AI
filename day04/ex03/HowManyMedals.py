import pandas as pd
"""
def howManyMedals(data, name):
	df = data[["Year", "Name", "Medal"]]
	pass
"""
name = 'Kjetil Andr Aamodt'
path = '../data/athlete_events.csv'
data = pd.read_csv(path, sep=",")
df = data[["Year", "Name", "Medal"]]
df2 = df[df["Name"] == name]
df2 = df2.groupby("Year")["Medal"].count()
print(df2.to_dict())
"""
G_df = df2[df2["Medal"] == 'Gold']
#S_df = df2[df2["Medal"] == 'Silver']
#B_df = df2[df2["Medal"] == 'Bronze']
#print(G_df)
#print(G_df.shape[0])
print(G_df)
print(G_df.groupby("Year")["Medal"].count())
"""