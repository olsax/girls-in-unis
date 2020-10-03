# libraries and data
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np
import pandas as pd
import csv

largest_column_cnt = 0

with open('girls_in_tech_unis.csv', 'r') as file_csv:
	read_file = csv.reader(file_csv)
	lines = file_csv.readlines()
	for l in lines:
		column_cnt = len(l.split(',')) + 1
		largest_column_cnt = column_cnt if largest_column_cnt < column_cnt else largest_column_cnt
file_csv.close()

column_names = [i for i in range(0, largest_column_cnt)]

df = pd.read_csv('girls_in_tech_unis.csv', header=None, delimiter = ',', names=column_names)
df = df.drop([0, 2, 3, 4]).drop(columns = [0])
df = df.reset_index(drop=True).dropna(axis=1, how='all')

df = df.drop([0])
df = df.reset_index(drop=True).rename(columns={1: "area", 2: "year", 3: "count"})
df['count'] = pd.to_numeric(df['count'])
df['count'] = df['count'].fillna(0)

#dataframe without POLSKA values
df_wp = df[df.area != 'POLSKA']

#plot work
mpl.style.use('seaborn')
sns.set_style("darkgrid")
sns.set_palette("deep", 14)
fig, ax = plt.subplots()

for key, grp in df_wp.groupby(['area']):
    ax = grp.plot(ax=ax, kind='line', x='year', y='count', label=key, figsize=(9,4))

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.legend(loc='upper center', bbox_to_anchor=(1.2, 1.0),
          ncol=1, fancybox=True, shadow=True, fontsize='small')
plt.title("number of girls attending technical universities in 2010 to 2015 in each of the voivodeships in Poland", fontsize=11, backgroundcolor='lavender', color='slategrey', fontweight='bold', pad=10)

plt.show()

