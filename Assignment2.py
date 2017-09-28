sssssssssss#!/usr/bin/env python
"""
Parse KNMI data and do simple analysis.
Floor Broekgaarden 10528105
"""

def read_data(filename):
	with open(filename, 'r') as f:
		count = 0
		list_KNMI_data = [] 
		lines = f.readlines()[99:] #skip headers
		for line in lines:
			temp_data_line = []
			split_line = line.split(',') 
			for i in split_line:
				stripped_item = i.strip()
				if stripped_item:
					temp_data_line.append(float(stripped_item))
				else:
					temp_data_line.append(None) #change empty measurements to "None" 
					###maybe still make everything integers, floats etc. 
			list_KNMI_data.append(temp_data_line)
		print list_KNMI_data
	

def plot_data(data):
	
	return

def main(filename):
	data = read_data(filename)
	plot_data(data)
	
if __name__ == '__main__':
	main('test.txt')
