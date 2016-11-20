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

for rows in data_obj.readlines():
	if rows.startswith('##'):
		continue
	if rows.startswith('#CHROM'):
		header_matrix = rows.rstrip('\n').split('\t')
		continue
	rall_matrix.append(rows.rstrip('\n').split('\t'))
	r_matrix.append(rows.rstrip('\n').split('\t')[9:])


# # print(snp_dict[1])
x_matrix= np.matrix(r_matrix).transpose()
pca=PCA(n_components= 2)
x_plot= pca.fit(x_matrix)


plt.figure()
plt.title('PCA 1st/2nd')
plt.scatter(x_plot.components_[0],x_plot.components_[1])
plt.savefig("q1_pca.png")
plt.close()