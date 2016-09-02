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
start= output["start"]+500
end=output["start"]+500
filtered_output = pd.concat([output["chr"],start,end,output["t_name"]], axis=1)
print(filtered_output)