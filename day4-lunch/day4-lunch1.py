#!/usr/bin/env python


import sys
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# for i, line in enumerate(open(sys.argv[1])):
# 		if i==0:
# 			continue
# 		fields = line. rstrip("\r\n").split(",")
# 		print(fields[0])
def SxlFPKM_filter(Sxl_file):
	filter_Sxl=Sxl_file["gene_name"]== "Sxl"
	output_file_1=Sxl_file[filter_Sxl]
	filter_FPKM= output_file_1["FPKM"]>0
	output_file_2=output_file_1[filter_FPKM]
	return output_file_2

file1= sys.argv[1]
file2= sys.argv[2]

Sxl_file1= pd.read_csv(file1,sep="\t")
Sxl_file2= pd.read_csv(file2,sep="\t")

Sxl_sorted1=SxlFPKM_filter(Sxl_file1)
Sxl_sorted2=SxlFPKM_filter(Sxl_file2)

FPKM_file1=np.log(Sxl_sorted1["FPKM"].tolist())
FPKM_file2=np.log(Sxl_sorted2["FPKM"].tolist())
plt.figure()
title1=re.findall("SRR[0-9]*/",sys.argv[1])[0]
title2=re.findall("SRR[0-9]*/",sys.argv[2])[0]
plt.boxplot([FPKM_file1,FPKM_file2],labels=[title1,title2])
plt.title("Sxl expression")
plt.savefig("Sxl.png")
plt.close()