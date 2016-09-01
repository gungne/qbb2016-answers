#!/usr/bin/env python

import sys
import re
import fasta
import operator

file = open(sys.argv[1])
query = open(sys.argv[2])
k=int(sys.argv[3])
kmer_counts={}
fasta_sets = fasta.fasta_parser(file)
query_sets = fasta.fasta_parser(query)
for count,query_item in enumerate(query_sets):
	if count==2:
		break
	query_id = query_item 
	query_seq = query_sets[query_id].upper()



query_dict={}
for j in range(0,len(query_seq)-k,k):
		kmer_q= query_seq[j:j+k]
		kmer_q= kmer_q.upper()
		if kmer_q not in query_dict:
			query_dict[kmer_q]=[j]
		else:
			query_dict[kmer_q].append(j)
#print(len(query_seq),j)

#print(query_dict)


for item in fasta_sets:
	#print(fasta_sets[item])
	fasta_sets[item]=fasta_sets[item].upper()
	temp_dict={}
	match_dict={}
	for i in range(0,len(fasta_sets[item]) - k):
		kmer = fasta_sets[item][i:i+k]
		kmer = kmer.upper()
		if kmer in query_dict:
			for start_loc in query_dict[kmer]:
				assembly=''
				origin_loc = i
				query_loc = start_loc
				j=0
				boot_loc=i+k

				if len(fasta_sets[item])>i+k+1 and len(query_seq)>start_loc+k+1:
					target_loc_char=fasta_sets[item][i+k+1]
					query_loc_char=query_seq[start_loc+k+1]
				else:
					break

				while target_loc_char == query_loc_char:
					boot_loc=boot_loc+1
					j=j+1
					#print("target_loc_char")
					if len(fasta_sets[item])>boot_loc and len(query_seq)>start_loc+k+j:
						target_loc_char= fasta_sets[item][boot_loc]
						query_loc_char= query_seq[start_loc+k+j]
					else:
						break

					assembly= fasta_sets[item][origin_loc:boot_loc]

				for n in range(0,k):
					if 	target_loc_char== fasta_sets[item][i-n] and query_loc_char== query_seq[start_loc-n]:
						assembly= fasta_sets[item][origin_loc-n:boot_loc]
					else:
						break
				#print(origin_loc)
				i=boot_loc
				if len(assembly)>0 :
					match_dict[assembly]=len(assembly)
				else:
					pass
		else:
			pass
	
	count=0
	print(item,len(match_dict))
	for results,lengths in sorted(match_dict.items(), key=operator.itemgetter(1),reverse=True):
		count=count+1
		if count==2:
			break
		print(results,lengths) 





		




