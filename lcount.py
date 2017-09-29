#!/usr/local/bin/python3.6

def lcount(keyword, fname):
	"""
	Function used to count the number of times something is in file
	
	Sample usage:
	num_dns_rec = lcount('Obsolete', 'my_file.txt')
	"""
	with open(fname, 'r') as fin:
		return sum([1 for line in fin if keyword in line])
