#!/usr/bin/env python

import sys
import re

file = sys.stdin

def fasta_parser(file):
	fasta_dict={}
	records = re.findall(">.*\n[ATCGatcg\-\n]*",file.read(),re.M)
	for fasta in records:
		id_sq = re.sub("[>\n]","",re.findall(">.*\n",fasta,re.M)[0])
		fasta_dict[id_sq] = re.sub("[\n]","",re.sub(">.*\n","",fasta)) 

	return fasta_dict