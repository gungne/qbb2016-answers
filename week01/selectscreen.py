#!/usr/bin/env pytho

import sys
import re
import fasta
import fastaP

ref_dir= open(sys.argv[1])
data_dir = open(sys.argv[2])

ref_seq=fasta.fasta_parser(ref_dir)
data_seq=fasta.fasta_parser(data_dir)
# print(ref_seq['query'])
scoreboard={}

for seq in data_seq:
	dN=0
	dS=0
	for chara in seq: 
		if char=='-':
			continue
		else:

