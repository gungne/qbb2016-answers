#!/usr/bin/env python

import sys
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA


df = pd.read_csv(sys.argv[1],index_col=0)

n,p= df.shape

# df = df.T
pca = PCA()

fit= pca.fit(df)

x=pca.transform(df)


plt.figure()
plt.plot(fit.components_.T[:8,:10])
plt.plot(fit.components_.T[8:,:10])
plt.xticks(range(8))
plt.legend()
plt.show()