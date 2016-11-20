import numpy as np
import os
import sys
import pylab
import scipy
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

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
fig = plt.figure()

# dendro=fig.add_subplot(111)
Y = sch.linkage(D, method='centroid')
Z = sch.dendrogram(Y, orientation='right', labels=labels, no_plot= True)
D_new=np.zeros((500,6))
# for 
# print(Z['leaves'][1])
labels_new=labels
for index,idx in enumerate(Z['leaves']):
	D_new[index,:]=np.float32(D[idx,:])
	labels_new[index]=labels[idx]

print(D_new)
ax= fig.add_subplot(111)
heatmap=ax.matshow(D_new, aspect='auto', origin='lower', cmap=pylab.cm.YlGnBu)
fig.colorbar(heatmap)
ax.set_yticks(np.arange(1, 500, 1.0))
#format settings 
ax.set_yticklabels(['']+labels_new)
ax.set_xticklabels(['']+header_matrix[1:])

# fig.show()
fig.savefig('heatmap.png')