#!/usr/bin/env pytho

import sys
import re
import fasta
import fastaP
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

def diff_letters(a,b):
    return sum ( a[i] != b[i] for i in range(len(a)) )

map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

ref_dir= open(sys.argv[1])
data_dir = open(sys.argv[2])

ref_seq=fasta.fasta_parser(ref_dir)
data_seq=fasta.fasta_parser(data_dir)
# print(ref_seq['query'])
scoreboard={}
# print(data_seq) 

n = 3
ref_seg_list=[ref_seq['query'][i:i+n] for i in range(0, len(ref_seq['query']), n)]
for item in data_seq:
	count= 0
	obscure_count=0
	nS = 0
	nN = 0 
	# print(ref_seg_list)
	temp_seg_list= [data_seq[item][i:i+n] for i in range(0, len(data_seq[item]), n)]
	# print(ref_seg_list)
	# print(temp_seg_list)
	for seg in temp_seg_list:
		# print(count)
		# print(seg)
		if seg=='---':
			continue
		else:
			if count>len(ref_seg_list)-1:
				break
			else:
				seg_n=re.sub('T','U',seg)
				ref_seg_n=re.sub('T','U',ref_seg_list[count])
				# print(seg_n)
				# print(ref_seg)
				if '-' in seg_n:
					obscure_count=obscure_count+1
					continue
				diff=0
				if map[ref_seg_n] == map[seg_n]:
					diff =diff_letters(ref_seg_n,seg_n)
					nS =nS + diff
					count= count + 1
				else:
					diff =diff_letters(ref_seg_n,seg_n)
					nN= nN + diff
					count= count + 1
	scoreboard[item]=[nS,nN,obscure_count]

nS_list = []
nN_list = []
dis_list =[]
for item in scoreboard:
	nS_list.append(scoreboard[item][0])
	nN_list.append(scoreboard[item][1])
	dis_list.append(scoreboard[item][1]/(scoreboard[item][0]+1))


nS_list=sorted(nS_list)
nN_list=sorted(nN_list)
dis_list=sorted(dis_list)
fit_nS = stats.norm.pdf(nS_list, np.mean(nS_list), np.std(nS_list)) 
fit_nN = stats.norm.pdf(nN_list, np.mean(nN_list), np.std(nN_list)) 
fit_dis = stats.norm.pdf(dis_list, np.mean(dis_list), np.std(dis_list)) 
plt.figure() 
plt.subplot(3,1,1)
plt.title('Normalized Distribution for nS')
plt.plot(nS_list,fit_nS,'-o')
plt.hist(nS_list,normed=True,alpha=0.5) 
plt.subplot(3,1,2)
plt.title('Normalized Distribution for nN')
plt.plot(nN_list,fit_nN,'-o')
plt.hist(nN_list,normed=True,alpha=0.5) 
plt.subplot(3,1,3)
plt.title('Normalized Distribution for nN/nS')
plt.plot(dis_list,fit_dis,'-o')
plt.hist(dis_list,normed=True,alpha=0.5) 
plt.tight_layout()
plt.savefig('week1_ver1.png')      








