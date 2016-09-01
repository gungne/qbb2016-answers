#!/usr/bin/env python

import sys
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import re


file1_dir =sys.argv[1] 
file2_dir =sys.argv[2] 
ctab1_data= pd.read_csv(file1_dir,sep="\t")
ctab2_data= pd.read_csv(file2_dir,sep="\t")
# print(ctab_data)
FPKM1_data = np.log2(ctab1_data["FPKM"] +1).tolist()
FPKM2_data = np.log2(ctab2_data["FPKM"] +1).tolist()
# print(FPKM1_data)
MA_data_M=[]
MA_data_A=[]
# print(FPKM1_data)

for i,out in enumerate(FPKM1_data):
	# print(FPKM2_data[i])
	MA_data_M.append(FPKM1_data[i]-FPKM2_data[i])

for j,out in enumerate(FPKM1_data):
	MA_data_A.append(0.5*(FPKM1_data[j]+FPKM2_data[j])) 

# print(MA_data_Y)
# print(ctab_data[filter_FPKM])
plt.figure()
plt.title("MA for {} in MA view".format(re.findall("SRR[0-9]*/",file1_dir),re.findall("SRR[0-9]*/",file2_dir)))

plt.scatter(x=MA_data_A,y=MA_data_M)
plt.show()
plt.savefig("task3MA.png")
plt.close()