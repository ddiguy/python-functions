#!/usr/local/bin/python3.6
from itertools import groupby
def keyfunc(s):
	"""
	Sorts based on numbers so that IP's appear in order
    Sorts Python sets based on numbers so that numbers are in order.
    I specifically use it to have IP addresses in proper order.
	Example usage is:
	a = sorted(my_set, key=keyfunc)
	with open('my_file.txt', 'a') as o1:
		for i in a:
			o1.write(i+'\n')
	o1.close()
	"""
	return [int(''.join(g)) if k else ''.join(g) for k, g in groupby('\0'+s, str.isdigit)]
