import numpy as np
import os
import sys
import pylab
import scipy
import scipy.cluster.hierarchy as sch
from scipy.stats import ttest_rel

data_obj = open(sys.argv[1] )
# ctcf_ obj = open(sys.argv[2] )

gene_dict={}
content_matrix=[]
header_matrix=[]
Data_mat=[]
labels=[]
for rows in data_obj.readlines():
	if rows.startswith('##'):
		continue
	if rows.startswith('gene'):
		header_matrix = rows.rstrip('\n').split('\t')
		continue
	content_matrix.append(rows.rstrip('\n').split('\t')[0:])
	Data_mat.append(rows.rstrip('\n').split('\t')[1:])
	# labels.append(rows.rstrip('\n').split('\t')[0])
	gene_dict[rows.rstrip('\n').split('\t')[0]]=rows.rstrip('\n').split('\t')[1:]
	# print(rows.rstrip('\n').split('\t')[0])
# Data_mat= content_matrix[:][2:]
# print(Data_mat)
labels = header_matrix[1:]
D= np.matrix(Data_mat)

t, p = ttest_rel([np.float32(x) for x in D[:,1]],[np.float32(x) for x in D[:,0]])

# D = D[index,:]
# D = D[:,index]
# im = axmatrix.matshow(D, aspect='auto', origin='lower')
# axmatrix.set_xticks([])
# axmatrix.set_yticks([])

# Plot colorbar.
# axcolor = fig.add_axes([0.91,0.1,0.02,0.8])
# pylab.colorbar(im, cax=axcolor)

# Display and save figure.
print(p)
