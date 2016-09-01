#!/usr/bin/env python

import sys
import re
import fasta

file = open(sys.argv[1])
k=int(sys.argv[2])
kmer_counts={}
fasta_sets= fasta.fasta_parser(file)


for item in fasta_sets:
	for i  in range(0,len(fasta_sets[item])-k):
		kmer = fasta_sets[item][i:i+k]
		kmer=kmer.upper()
		if kmer not in kmer_counts:
			kmer_counts[kmer]=1
		else:
			kmer_counts[kmer]=kmer_counts[kmer]+1

for item in kmer_counts:
	print(item,kmer_counts[item])