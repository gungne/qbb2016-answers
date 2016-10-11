#!/usr/bin/env python

import sys
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from sklearn.decomposition import PCA
import vcf
import re
import csv

gene_dir = sys.argv[1]
data_obj = open(sys.argv[1],'r')


snp_dict={}
header_matrix= []
rall_matrix=[]
r_matrix=[]
x_matrix=[]
freq_snp=[]

for rows in data_obj.readlines():
	if rows.startswith('##'):
		continue
	if rows.startswith('#CHROM'):
		header_matrix = rows.rstrip('\n').split('\t')
		continue
	rall_matrix.append(rows.rstrip('\n').split('\t'))
	r_matrix.append(rows.rstrip('\n').split('\t')[9:])


# # print(snp_dict[1])
# x_matrix= np.matrix(r_matrix).transpose()
# pca=PCA(n_components= 2)
# x_plot= pca.fit(x_matrix)
for rows in r_matrix:
	int_rows=sum(int(num) for num in rows)/len(rows)
	freq_snp.insert(-1,int_rows)
	# x_ratio= floor(int_rows/len(rows)*10)/10
# print(freq_snp) 


plt.figure()
plt.title('SNP_freq')
plt.hist(freq_snp,alpha=0.6)
plt.xlabel('Frequency of the SNP')
plt.ylabel('number of SNP')
plt.savefig("q2_freq.png")
plt.close()