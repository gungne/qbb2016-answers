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
def Chrome_filter(file,Chromesome):
	filter_Chorme=file["chr"]== Chromesome	
	output_file_1=file[filter_Chorme]
	return output_file_1

file1_dir= sys.argv[1]
file2_dir= sys.argv[2]
chromesome= ["2L","2R","3L","3R","4","X"]
rolling_num=int(sys.argv[3])

file1= pd.read_csv(file1_dir,sep="\t")
file2= pd.read_csv(file2_dir,sep="\t")



title1=re.findall("SRR[0-9]*/",sys.argv[1])[0]
title2=re.findall("SRR[0-9]*/",sys.argv[2])[0]

for chromesome_selected in chromesome:
	file1_sorted=Chrome_filter(file1,chromesome_selected)
	file2_sorted=Chrome_filter(file2,chromesome_selected)
	plt.figure()
	smoothed_1=file1_sorted["FPKM"].rolling(rolling_num).mean()
	smoothed_2=file2_sorted["FPKM"].rolling(rolling_num).mean()
	plt.title("Rolling mean (size = "+ str(rolling_num) + ") for "+ chromesome_selected)
	plt.subplot(3, 1, 1)
	plt.plot(smoothed_1, label=title1)
	plt.ylabel("FPKM")
	plt.subplot(3, 1, 2)
	plt.plot(smoothed_2, label=title2)
	plt.ylabel("FPKM")
	plt.subplot(3, 1, 2)
	plt.plot(smoothed_2, label="merged")
	plt.ylabel("FPKM")
	plt.plot(smoothed_1)
	plt.plot(smoothed_2)
	plt.savefig(chromesome_selected+".png")
	plt.close()