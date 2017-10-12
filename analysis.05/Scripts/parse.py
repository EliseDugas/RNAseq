#!/usr/bin/python2.7

import sys


## usage : python parse.py <filename>

filename = sys.argv[1]


f = open (filename, "r")

for line in f :
	p_adj_value = line.split("\t")[6].strip()
	if p_adj_value != 'NA' and float(p_adj_value) < 0.01 :
		print line.split("\t")[0]


