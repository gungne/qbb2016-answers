#!/usr/bin/env python


import sys
import pandas as pd
import matplotlib.pyplot as plt
# for i, line in enumerate(open(sys.argv[1])):
# 		if i==0:
# 			continue
# 		fields = line. rstrip("\r\n").split(",")
# 		print(fields[0])

df= pd.read_csv(sys.argv[1],sep="\t")
# print(df.head())
# print(df.describe())
df_roi=df["chr"]=="3L"

df_chrom=df[df_roi]
smoothed=df_chrom["FPKM"].rolling(200).mean()

plt.figure()
plt.plot(smoothed)
plt.title("Chromesome 3L, FPKM rolling = 200")
plt.savefig("smoothed.png")
plt.close()