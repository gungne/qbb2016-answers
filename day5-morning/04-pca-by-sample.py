#!/usr/bin/env python

import sys
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA


df = pd.read_csv(sys.argv[1],index_col=0)

n,p= df.shape

df = df.T
pca = PCA()

fit= pca.fit(df)

x=pca.transform(df)
colors=[]
# print(x)

for name in df.T.columns:
	if "female" in name:
		colors.append("purple")
	else:
		colors.append("orange")


plt.figure()

# plt.scatter(x[:,0],x[:,1],c=colors,edgecolor = "None")
# colnames= df.T.columns
# for i in range(len(colnames)):
# 	plt.annotate(colnames[i],(x[i,0],x[i,1]))
n_pcs= 4
x2=x[:,:n_pcs]
for i in range(n_pcs):
	for j in range(n_pcs):
		plt.subplot(n_pcs,n_pcs,i + j*n_pcs + 1 )
		plt.scatter(x2[:,i],x2[:,j],c=colors,edgecolor = "None")
plt.show()