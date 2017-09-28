'''
Parser etc. KNMI data

Floor Broekgaarden


'''
import numpy as np 
import matplotlib.pyplot as plt

ind_TX = 14 # make something from Dict
ind_YYYYMMDD = 1

def read_station_locations(file_obj): 
# look for start of the first part of the header
	for line in file_obj:
		if line.startswith('# STN'):
			break
	# parse the station locations until an empty line is reached
	station_locations = []
	for line in file_obj:
		if line.startswith('#') and not line[1:].strip():
			break
		#print 'STATION LOCATION', line
		sline = line.split(None, 5)
		temp_sline = []
		for j in range(len(sline)):
				if j ==1:
					temp_sline.append(int(sline[j][0:3]))
				elif j==2 or j==3 or j==4:
					temp_sline.append(float(sline[j]))
				elif j==5: 
					temp_sline.append(str(sline[j][:-2]))
		station_locations.append(temp_sline)	
	return station_locations


def read_abbreviations(file_obj):
# parse abbreviations until an empty line is reached
	abbreviations = {}
	for line in file_obj:
		if line.startswith('#') and not line[1:].strip(): #empty further
			break
		else:
			sline = line.split()
        	abbreviations[sline[1]] = ' '.join(sline[3:])
		#print 'ABBREVIATOIN', line
	return abbreviations


def read_column_names(file_obj):
	"""Read column names from KNMI data file"""  #How does this one know to start at line 5? with next()? 
	column_names = [cn.strip() for cn in next(file_obj).split(',')[1:]] #start at 1 as we don't need STN
	return column_names

def read_data(file_obj):
	"""Read the weather observations from the KNMI data file
	returns data as a list of lists with observations"""

	data = [] 
	count = 0 
	#a =0
	for line in file_obj:
		if line.startswith('#') and not line[1:].strip(): #skip empty line with '#'
			break 
	for line in file_obj:
		#a += 1
		#print(' This is one line for floor %s' %line)
	 	#if a == 3:
		#	break

		temp_line = []
	 	split_line = line.split(',') 
	 	for i in split_line:
	 		strip_split_line = i.strip()
	 		if strip_split_line:
	 			if not temp_line:
	 				temp_line.append(int(strip_split_line))
	 			elif len(temp_line) ==1:
	 				temp_line.append(int(strip_split_line))
	 			else:
	 				temp_line.append(float(strip_split_line))   #look at which others should be integers instead of floats can be easily added
	 		else:
	 			temp_line.append(None) #change empty measurements to "None" 
	 	data.append(temp_line)
	return data 
	# lines = file_obj.readlines()[99:] #skip headers # verander dit naar next()
	# for line in lines:
	# 	temp_line = []
	# 	split_line = line.split(',') 
	# 	for i in split_line:
	# 		strip_split_line = i.strip()
	# 		if strip_split_line:
	# 			temp_line.append(float(strip_split_line))
	# 		else:
	# 			temp_line.append(None) #change empty measurements to "None" 
	# 		data.append(temp_line)
	# print data
	#return 

# parse the body of the data file here
def read_knmi_data_file(filename):
	"""Fully parse the KNMI data file"""
	with open(filename, 'r') as f:
		station_locations = read_station_locations(f)
		abbreviations = read_abbreviations(f)
		column_names = read_column_names(f)
		data = read_data(f)

	return station_locations, abbreviations, column_names, data


def plot_max_temperature(data, abbreviations,station_locations, station_number):
	TX_mask_station = []
	YYYYMMDD_mask_station = []
	number_measurements =0
	for i in range(len(data)):
		if data[i][0] == station_number:
			TX_mask_station.append(data[i][ind_TX])
			YYYYMMDD_mask_station.append(data[i][ind_YYYYMMDD])
			if data[i][ind_TX] != None:
				number_measurements += 1.
	for i in range(len(station_locations)):
		if station_locations[i][0] == station_number:
			station_name = station_locations[i][4]
	print('number = %s' %number_measurements)

	#if number_measurements != 0:
	#	mean_TX = sum(TX_mask_station)*(float(number_measurements))**-1
	#else:
	#	mean_TX =None
	plt.figure(1)		
	plt.xlabel('%s'%abbreviations['YYYYMMDD'])
	plt.ylabel('%s'%abbreviations['TX'])
	plt.title('Plot of maximum temperature for station %s (%s)'%(station_number,station_name) ) #add name of station
	plt.plot(TX_mask_station,c='g',label='data')
	#plt.plot([min(YYYYMMDD_mask_station), max(YYYYMMDD_mask_station)], [mean_TX, mean_TX], 'k-',label='mean max T')
	plt.legend
	print(TX_mask_station[300:380])
	print(min(YYYYMMDD_mask_station))
	print(max(YYYYMMDD_mask_station))

	#plt.xlim([1850,2017])
	plt.show()

	return 


def main():
	"""Parse the KNMI data file and plot the max temperature at the Bilt."""
	station_locations, abbreviations, column_names, data = 	read_knmi_data_file('KNMI_20170914.txt')
	print(station_locations)
	print(abbreviations['YYYYMMDD'])
	print(column_names[1])
	ind_TX = 14 # make something from Dict
	ind_YYYYMMDD = 1 #make something from Dict
	print len(data)
	print data[40][ind_YYYYMMDD]
	plot_max_temperature(data, abbreviations,station_locations, station_number=260)

if __name__ == '__main__':
	main()

	#test.txt
	#KNMI_20170926.tx

	
