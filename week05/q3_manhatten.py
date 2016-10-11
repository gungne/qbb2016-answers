#!/usr/bin/env python

import sys
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from sklearn.decomposition import PCA
import os
import re

from assocplots.manhattan import *

def listdir_nohidden(path):
    list_t = []
    for f in os.listdir(path):
        if not f.startswith('.'):
            list_t.append(f)
    return list_t  

#ls the database
cur_dir = os.getcwd()
storage_dir = 'data'
db_list = listdir_nohidden(os.path.join(cur_dir,'data'))

for file in db_list:
	trait_name = re.sub('plink.','',file)
	trait_name = re.sub('.qassoc','',trait_name)

	data=np.genfromtxt(os.path.join(storage_dir,file), dtype=None,skip_header = 1)

	#from github package assocplots


	chrs = [str(i) for i in range(1,16)]
	chrs_names = np.array([str(i) for i in range(1,16)])
	chrs_names[1::2] = ''

	cmap = plt.get_cmap('viridis')
	colors = [cmap(i) for i in [0.0,0.33,0.67,0.90]]

	# Alternatively you can input colors by hand
	from matplotlib.colors import hex2color
	colors = ['#1b9e77', "#d95f02", '#7570b3', '#e7298a']
	# Converting from HEX into RGB
	colors = [hex2color(colors[i]) for i in range(len(colors))]


	manhattan(     data['f8'], data['f2'], data['f0'].astype(str), trait_name,
	               type='single',
	               chrs_plot=[str(i) for i in range(1,16)],
	               chrs_names=chrs_names,
	               cut = 0,
	               title='SNP associated with '+trait_name,
	               xlabel='chromosome',
	               ylabel='-log10(p-value)',
	               lines= [5],
	               colors = colors)

	plt.savefig(trait_name+'.png', dpi=300)

