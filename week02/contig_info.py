#!/usr/bin/env python

import fasta
import sys
import os
import re
contig_dir =sys.argv[1]

contigs_dict= fasta.fasta_parser(open(contig_dir))
# print(contigs_dict)

sum_len=0
contig_len=[]
count=0
for index,item in enumerate(contigs_dict):
	if index == 0:
		max_contig=len(contigs_dict[item])
		min_contig=len(contigs_dict[item])
	else:
		if len(contigs_dict[item])>max_contig:
			max_contig=len(contigs_dict[item])
		if len(contigs_dict[item])<min_contig:
			min_contig=len(contigs_dict[item])
	contig_len.append(len(contigs_dict[item]))
	sum_len=sum_len+len(contigs_dict[item])
	count=count+1
temp_sum=0
for contig in sorted(contig_len):
	temp_sum=temp_sum+contig
	if temp_sum>sum_len/2:
		n50=contig
		break



average_contig = sum_len/count
print(re.sub('/.*week02/','',contig_dir))
print('min: {} max: {} average: {} n50: {}'.format(min_contig,max_contig,average_contig,n50))