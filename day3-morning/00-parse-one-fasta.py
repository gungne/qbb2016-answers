#!/usr/bin/env python

import sys
import re

file = sys.stdin


fasta_dict={}
records = re.findall(">.*\n[ATCGatcg\n]*",file.read(),re.M)
for fasta in records:
	id_sq = re.sub("[>\n]","",re.findall(">.*\n",fasta,re.M)[0])
	fasta_dict[id_sq] = re.sub("[\n]","",re.sub(">.*\n","",fasta)) 

for id_sq in fasta_dict:
	print(id_sq,fasta_dict[id_sq])