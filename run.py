import pandas as pd
import csv


#read_file_pd = pd.read_csv('girls_in_tech_unis.csv', header=None)
#print(read_file_pd)

largest_column_cnt = 0

with open('girls_in_tech_unis.csv', 'r') as file_csv:
	read_file = csv.reader(file_csv)
	#for row in read_file:
	#	print(row)
	lines = file_csv.readlines()
	for l in lines:
		column_cnt = len(l.split(',')) + 1
		largest_column_cnt = column_cnt if largest_column_cnt < column_cnt else largest_column_cnt

file_csv.close()

column_names = [i for i in range(0, largest_column_cnt)]

df = pd.read_csv('girls_in_tech_unis.csv', header=None, delimiter = ',', names=column_names)
df = df.drop([0, 2, 3, 4])
df = df.drop(columns = [0])
df = df.reset_index(drop=True)
df = df.dropna(axis=1, how='all')

data_info = df.iloc[0][1]

df = df.drop([0])
df = df.reset_index(drop=True)
print(df)

data_info = data_info.splitlines()
print(data_info)