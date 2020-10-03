# libraries and data
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import seaborn as sns
import numpy as np
import pandas as pd
import csv

largest_column_cnt = 0
#changing font of charts
csfont = {'fontname':'Consolas'}

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

total_count_area = df_wp.groupby('area')['count'].sum().tolist()

max_count_area = int(max(total_count_area))
min_count_area = int(min(total_count_area))


##PLOT WORK

#multiple lines plot
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

#barplot
mpl.style.use('seaborn')
sns.set_style("dark")

fig, ax = plt.subplots(figsize=(9,5))

#ci - size of confidence intervals on bars
ax = sns.barplot(y= total_count_area, x = df_wp['area'].unique(), data = df_wp, palette=("RdPu_d"), alpha=0.8, linewidth=2, ci=0)
plt.xticks(rotation='vertical', **csfont)
box = ax.get_position()
ax.set_position([box.x0, box.y0 + 0.25, box.width, box.height*0.75])

#keep tick labels but remove axis label names
ax.set_ylabel(' ')
ax.set_xlabel(' ')

plt.title("ranked voivodeships in Poland according to the number of girls attending technical universities from 2010 to 2015", fontsize=10, backgroundcolor='whitesmoke', color='palevioletred', fontweight='bold', pad=10, **csfont)
plt.show()


#radar chart

mpl.style.use('seaborn')
sns.set_style("dark")

fig = plt.figure(figsize=(6,6))

ax = plt.subplot(polar="True")

cateogries = df_wp['area'].unique()
N = len(cateogries)

values = total_count_area
values += values[:1]

angles = [n/float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

plt.polar(angles, values, linewidth=1.0, linestyle='solid', color='slateblue')
plt.fill(angles, values, 'mediumpurple', alpha=0.6)

plt.tick_params(axis ='x', pad = 10)
plt.xticks(angles[:-1], cateogries, color="darkslateblue", size=8)

ax.set_rlabel_position(25)
plt.yticks(color="grey", size=8)
plt.ylim(min_count_area, max_count_area)

box = ax.get_position()
ax.set_position([box.x0, box.y0-0.05, box.width*0.9, box.height])

plt.title('number of girls attending technical universities in 2010 to 2015 \n in each of the voivodeships in Poland shown with radar chart', color='slateblue', weight='bold', size=13, position=(0.5, 1.1), horizontalalignment='center', verticalalignment='center', pad=30)
plt.show()
