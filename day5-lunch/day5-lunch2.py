#!/usr/bin/env python

import sys
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

data_file_dir=sys.argv[1]


# window_input =sys.argv[2] 
#extension .bed and columns chromosome, start, end, t_name

data_start_codon = pd.read_csv(data_file_dir,"\t")

# start_codon_dict={}
# Ensemble_start_codon=Ensemble_start_codon[Ensemble_start_codon["feature"]=="start_codon"]
# print(Ensemble_start_codon.to_string(index=False))
# print(data_start_codon)
chromesome_type=["X","3R","3L","2R","2L","4"]
result_df=[]
for item in chromesome_type:
	result_df.append(data_start_codon[data_start_codon["chr"] == item])


output= pd.concat(result_df)
start_ref=output["start"].tolist()
end_ref=output["end"].tolist()
chr_ref=output["chr"].tolist()
t_name_ref=output["t_name"].tolist()
start_list=[]
end_list=[]
chromesome_list=[]
t_name_list= []
for index,item in enumerate(output["strand"]):
	if item == "+":
		start_list.append(start_ref[index]-500)
		end_list.append(start_ref[index]+500)
		chromesome_list.append(chr_ref[index])
		t_name_list.append(t_name_ref[index])
	else:
		start_list.append(end_ref[index]-500)
		end_list.append(end_ref[index]+500)
		chromesome_list.append(chr_ref[index])
		t_name_list.append(t_name_ref[index])
		
for index, item in enumerate(chromesome_list):
	print(chromesome_list[index],"\t",start_list[index],"\t",end_list[index],"\t",t_name_list[index])





# print(bed_data)





