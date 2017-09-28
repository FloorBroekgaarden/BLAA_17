#!/usr/bin/env python
"""
Created 28/09/2017
Program that opens KNMI data, reads in the data,
and makes a simple plot of monthly anomaly
Parse KNMI data and do simple analysis.
Floor Broekgaarden 10528105
"""
import matplotlib.pyplot as plt


def read_data(filename):
	with open(filename, 'r') as f:
		data,list_data,years,months = [], [], [], []
		anomaly_month,unc_month,anomaly_year,unc_year = [],[],[],[]
		anomaly_5year,unc_5year,anomaly_10year,unc_10year = [],[],[],[]
		anomaly_20year,unc_20year = [],[]
		lines = f.readlines()
		#skip headers and stop after reading first part data
		count = 0 
		for line in lines:
			if line.startswith(' ') and not line[1:].strip():
				count +=1 
				if count ==2:
					break 

			if not line.startswith('%') and line[1:].strip():
				temp_data_line = []
				split_line = line.split() #split at ' '
				years.append(int(split_line[0]))
				months.append(int(split_line[1]))
				anomaly_month.append(float(split_line[2]))
				unc_month.append(float(split_line[3]))
				anomaly_year.append(float(split_line[4]))
				unc_year.append(float(split_line[5]))
				anomaly_5year.append(float(split_line[6]))
				unc_5year.append(float(split_line[7]))
				anomaly_10year.append(float(split_line[8]))
				unc_10year.append(float(split_line[9]))
				anomaly_20year.append(float(split_line[10]))
				unc_20year.append(float(split_line[11]))
			data = [years,months,anomaly_month,unc_month,anomaly_year, \
			unc_year,anomaly_5year,unc_5year,anomaly_10year,\
			unc_10year,anomaly_20year,unc_20year]
		return data 
	
def plot_data(data):
	plt.figure(1) 
	years = data[0]
	anomaly_month = data[2]
	plt.xlabel('year')
	plt.ylabel('Temperature monthly anomaly [Celcius]')
	plt.title('Plot of monthly anomaly vs year')
	plt.plot(years,anomaly_month,c='g')
	plt.xlim([1850,2017])
	plt.savefig('Temperature_vs_monthly_anomaly.pdf', format='pdf', dpi=1200)
	plt.show()


def main(filename): #main program
	data = read_data(filename)
	plot_data(data)
	
if __name__ == '__main__':
	main('Land_and_Ocean_complete2.txt')	 #textfile with data
