#!/usr/bin/env python

import sys
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from statsmodels.regression.linear_model import OLS as ols



data_file_dir=sys.argv[1]
tab_file_dir=sys.argv[2]


# window_input =sys.argv[2] 
#extension .bed and columns chromosome, start, end, t_name

tab_file = pd.read_csv(tab_file_dir,"\t",names=["name","size","covered","sum","mean0","mean"])
data_file= pd.read_csv(data_file_dir,"\t")



chromesome_type=["X","3R","3L","2R","2L","4"]
result_df=[]
for item in chromesome_type:
	result_df.append(data_file[data_file["chr"] == item])

data_df= pd.concat(result_df).sort(["t_name"])

# print(data_df)
tab_file=tab_file.sort(["name"])
print(len(tab_file["sum"]),len(data_df["FPKM"]))


if len(tab_file["sum"])==len(data_df["FPKM"]):
	ols_md= ols(tab_file["sum"].tolist(),data_df["FPKM"].tolist())

results = ols_md.fit()
print(results.summary())

