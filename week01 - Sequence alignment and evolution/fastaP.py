#!/usr/bin/env python

import sys
import re

file = sys.stdin

def fastaP_parser(file):
	fasta_dict={}
	records = re.findall(">.*\n[A-Za-z \-\n]*",file.read(),re.M)
	for fasta in records:
		id_sq = re.sub("[>\n]","",re.findall(">.*\n",fasta,re.M)[0])
		fasta_dict[id_sq] = re.sub("[\n]","",re.sub(">.*\n","",fasta)) 

	return fasta_dict