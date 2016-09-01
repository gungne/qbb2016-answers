#!/usr/bin/env python

import sys
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import re

def plot_sex(metadata_dir,ctab_dir,sex):
	metadata= pd.read_csv(metadata_dir)


	metadata_roi= metadata["sex"]==sex
	metadata_result= metadata[metadata_roi]

	FPKM_list=[]
	name_list=[]
	for i,file_dir in enumerate(metadata_result["sample"].tolist()):
		file = open(ctab_dir + file_dir+"/t_data.ctab" )
		sample= pd.read_csv(file,sep="\t")
		filtered_data= sample[sample["gene_name"]=="Sxl"]
		# print(type(filtered_data["FPKM"].values.mean()))
		FPKM_list.append(filtered_data["FPKM"].values.mean())
		name_list.append(metadata_result["stage"].tolist()[i])
		#plt.plot(filtered_data["FPKM"].values.mean())#labels=metadata_result["sample"].tolist()[i]
		# plt.plot(range(0,i+1), FPKM_list,'bo-')
	return FPKM_list,name_list

file_dir =sys.argv[1] 
ctab_data= pd.read_csv(file_dir,sep="\t")
# print(ctab_data)

filter_FPKM= ctab_data["FPKM"]>0
# print(ctab_data[filter_FPKM])

plt.figure()
plt.title("Histogram for {} in log view".format(re.findall("SRR[0-9]*/",file_dir)))
plt.hist(np.log(ctab_data[filter_FPKM]["FPKM"].tolist()))
plt.savefig("task2histo.png")
plt.close()