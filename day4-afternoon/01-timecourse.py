#!/usr/bin/env python

import sys
import pandas as pd 
import matplotlib.pyplot as plt


def TimeCourse(metadata,ctab):
	df_meta = pd.read_csv(metadata)



metadata_dir =sys.argv[1] 
ctab_dir = sys.argv[2]

metadata= pd.read_csv(metadata_dir)


metadata_roi= metadata["sex"]=="female"
metadata_result= metadata[metadata_roi]

FPKM_list=[]
plt.figure()
for file_dir in metadata_result["sample"].tolist():
	file = open(ctab_dir + file_dir+"/t_data.ctab" )
	sample= pd.read_csv(file,sep="\t")
	filtered_data= sample[sample["gene_name"]=="Sxl"]
	# print(filtered_data["FPKM"].values)
	plt.xscale("log")
	plt.boxplot(filtered_data["FPKM"].values,label=metadata_result["stage"])
plt.show()
plt.close()
