import csv
import statistics
import sys
from split_data import split_data

def read_data_from_file(path):
	with open(path, 'r', newline='') as csvfile:
		data = list(csv.reader(csvfile, delimiter=','))
		data.pop(0)
	return data

if len(sys.argv) == 3:
	path = sys.argv[1]
	interval = sys.argv[2]
	
if len(sys.argv) == 2:
	path = sys.argv[1]
	interval = 300
else:
	print("Укажите имя файла")

data = read_data_from_file(path)
splitdata = split_data(data, interval)

def calculate_statistics(splitdata):
	for j in splitdata:
		start_time = j[0][0]
		end_time = j[-1][0]
		
		values =[int(y[1]) for y in j]

		length = len(values)

		median = statistics.median(values)

		mean = statistics.mean(values)

		mode = statistics.mode(values)
		
		print(start_time, "-", end_time, " ", "length:",length, "median:",median, "mean:",mean, "mode:",mode)

calculate_statistics(splitdata)	