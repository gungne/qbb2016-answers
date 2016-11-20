#!/usr/bin/env pytho

import sys
import re
import fasta
import fastaP

nr_fasta= open(sys.argv[1])
protein_fasta=open(sys.argv[2])
nr_dict=fasta.fasta_parser(nr_fasta)
protein_dict=fastaP.fastaP_parser(protein_fasta)
aligned_dict={}

for gi in protein_dict:
	temp_prot=protein_dict[gi]
	# print(temp_prot)
	temp_fasta=nr_dict[gi]
	# print(temp_fasta)
	result=''
	count=0
	for base in temp_prot:
		if base=='-':
			result=result+'---'
			continue
		else:
			result= result+temp_fasta[count*3:count*3+3]
			count=count+1
	aligned_dict[gi]=result

for gi in aligned_dict:
	print('>'+gi)
	print(aligned_dict[gi])
# print(result)
# print(count)