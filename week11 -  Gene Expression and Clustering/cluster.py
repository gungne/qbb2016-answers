import numpy as np
import os
import sys
import pylab
import scipy
import scipy.cluster.hierarchy as sch


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
	labels.append(rows.rstrip('\n').split('\t')[0])
	gene_dict[rows.rstrip('\n').split('\t')[0]]=rows.rstrip('\n').split('\t')[1:]
	# print(rows.rstrip('\n').split('\t')[0])
# Data_mat= content_matrix[:][2:]
# print(Data_mat)
D= np.matrix(Data_mat)
fig = pylab.figure()


Y = sch.linkage(D, method='centroid')
Z = sch.dendrogram(Y, orientation='right', labels=labels )

# idx = Z['leaves']
# D = D[idx,:]
# D = D[:,idx]
pylab.matshow(D, aspect='auto', origin='lower', cmap=pylab.cm.YlGnBu)


fig.show()
fig.savefig('dendrogram.png')