#!/usr/bin/env python

import sys
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import re
from scipy.stats import gaussian_kde

file_dir =sys.argv[1] 

ctab_data= pd.read_csv(file_dir,sep="\t")

FPKM_data= ctab_data["FPKM"].tolist()

density=gaussian_kde(FPKM_data)
# print(MA_data_Y)
# print(ctab_data[filter_FPKM])

#script below from stack overflow
plt.figure()
plt.title("FPKM {} in Density view".format(re.findall("SRR[0-9]*/",file_dir)))
xs = np.linspace(0,10,100)
density.covariance_factor = lambda : .25
density._compute_covariance()
plt.plot(xs,density(xs))
plt.savefig("task4density.png")
plt.close()