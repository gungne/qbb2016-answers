#!/usr/bin/env python


import sys
import pandas as pd
# for i, line in enumerate(open(sys.argv[1])):
# 		if i==0:
# 			continue
# 		fields = line. rstrip("\r\n").split(",")
# 		print(fields[0])

df= pd.read_csv(sys.argv[1],sep="\t")
# print(df.head())
# print(df.describe())

df_roi1=df["FPKM"]>1000
df_roi2=df["cov"]>10
# print(df[df_roi]))
# df_roi= df["gene_name"]=="fzo"
# print(df[df_roi])
print((pd.merge(df[df_roi1],df[df_roi2],on="gene_name")).describe())