import numpy as np
import os
import sys
import pylab
import scipy
# import pyplot 
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import KMeans

data_obj = open(sys.argv[1] )
# ctcf_ obj = open(sys.argv[2] )

gene_dict={}
content_matrix=[]
header_matrix=[]
Data_mat=[]
genes=[]
for rows in data_obj.readlines():
	if rows.startswith('##'):
		continue
	if rows.startswith('gene'):
		header_matrix = rows.rstrip('\n').split('\t')
		continue
	content_matrix.append(rows.rstrip('\n').split('\t')[0:])
	Data_mat.append(rows.rstrip('\n').split('\t')[1:3])
	genes.append(rows.rstrip('\n').split('\t')[0])
	gene_dict[rows.rstrip('\n').split('\t')[0]]=rows.rstrip('\n').split('\t')[1:]
	# print(rows.rstrip('\n').split('\t')[0])
# Data_mat= content_matrix[:][2:]
# print(Data_mat)
D= np.matrix(Data_mat)

# print(D)
fig = pylab.figure()
# axdendro = fig.add_axes([0.09,0.1,0.2,0.8])
kmeans_d = KMeans(n_clusters=7, random_state=0).fit(D)
labels = kmeans_d.labels_
# print(labels)
# print(centroids)
count=0
for index,lbel in enumerate(labels):
	count=count+1
	if int(lbel) == 0:
		print(genes[index])


colors = ["g.","r.","y.","b.","m.","c.","k."]

for i in range(len(D)):
    plt.plot(D[i,0],D[i,1], colors[labels[i]], markersize = 5)

fig.show()
fig.savefig('kmean.png')