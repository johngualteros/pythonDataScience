import matplotlib.pyplot as plt
import pandas as pd

s = pd.Series([18, 49, 9, 32, 81, 64, 3])
s.plot(kind='bar')
plt.savefig('plot.png')

# graph linear
df = pd.read_csv('https://www.sololearn.com/uploads/ca-covid.csv')
df[df['month'] == 18]['cases', 'deaths'].plot()

# graph bar
df = df.groupby('month')[['cases', 'deaths']].sum()
df.plot(kind='bar', stacked=True)  # barh for bars alignment horizontal

"""
more types of graphs are
box,
hist,
area,
pie
"""

# graph dispersion
var = df[df["month"] == 6][["cases", "deaths"]].plot(kind="scatter", x='cases', y='deaths')

df[['cases', 'deaths']].plot(kind='area', legend=True, color=['#12323d', '#1243fe'])
plt.xlabel('Days in June')
plt.ylabel('number')
plt.suptitle('Covid 19 in June')
