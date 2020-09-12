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

data_info = df.iloc[0][1]

df = df.drop([0])
df = df.reset_index(drop=True).rename(columns={1: "Area", 2: "Year", 3: "Count"})

data_info = data_info.splitlines()

years_str = data_info[0][6:]
years_int = years_str.split(", ")
years_int = [int(year) for year in years_int]

areas = data_info[1][18:]
areas = areas.split(", ")

