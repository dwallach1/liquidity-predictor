import csv 
import random

def read_training_data(fname, col_start, col_end, N=0, dropped=False):
	data = []
	x = 0
	f = open(fname)
	csv_reader = csv.reader(f)
	for line in csv_reader:
	    append_line = [line[i] for i in range(col_start,col_end)]
	    if dropped:
		    if "NA" in append_line:
		    	continue

	    if append_line[0] == '0' and x <= N:
	    	x += 1
	    	continue
	    data.append(append_line)
	f.close()
	print(len(data))
	return data

def get_means(data):
	"""
	get the mean values of each columns to fill missing attribute values
	input:
		a list of lists representing the excel data
 
	returns:
		single list of means associated with each column
	"""
	totals = [[] for x in range(0, 11)]
	entries = [0] * 11
	# data is 2D array -- get each val
	header = 0
	for d in data:
		if header == 0:
			header += 1
			continue
		for i, x in enumerate(d):
			if x != "NA":
				totals[i].append(float(x))
				entries[i] += 1
	
	sums = [sum(total) for total in totals]
	# print ("sums are %s" % sums)
	# print ("entries are %s" % entries)
	means = [sums[i]/float(entries[i]) for i in range(0,11)]
	# print ("means are %s" % means)
	return means

def compute_missing_data(data):
	"""
	fills in the missing attribute with the means of the associated columns 

	inputs:
		a list of lists representing the excel data

	returns:
		the same lists of lists with the missing attributes filled in
	"""
	means = get_means(data)
	for d in data:
		for j,x in enumerate(d):
			if x == 'NA':
				d[j] = means[j]
				# print ("setting value to mean of %s" % means[j])
	return data		

def generate_filled_in_small(N):
	d = read_training_data('data/training_no_missing_attrs.csv',0, 11, N)
	f_out = "data/training_no_missing_attrs_SMALL_" + str(N) + ".csv"
	with open(f_out, "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(d)

def generate_dropped_small(N):
	d = read_training_data('data/training_missing_dropped.csv',0,11, N)
	f_out = "data/training_dropped_SMALL_" + str(N) + ".csv"
	with open(f_out, "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(d)

def generate_filled_in():
	d = read_training_data('data/cs-training.csv')	
	d_new = compute_missing_data(d)
	
	with open("data/training_no_missing_attrs_AB.csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(d_new)

def generate_dropped():
	d_new = read_training_data('data/cs-training.csv', dropped=True)	

	with open("data/training_missing_dropped.csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(d_new)

def main():
	Ns = [90000, 100000, 110000, 120000, 130000]
	for n in Ns:
		generate_filled_in_small(n)
		generate_dropped_small(n)

if __name__ == '__main__':
	main()