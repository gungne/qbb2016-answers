#!/usr/bin/env python

import sys
import pandas as pd 

base= sys.argv[1]
df = pd.read_csv(base +"fastq/samples.csv")
d= {}
for _,sample,sex ,stage in df.itertuples():
	col_df = d[sex +"_ "+stage] =pd.read_table(base+"results/stringtie/"+sample+"/t_data.ctab", index_col = "t_name")["FPKM"]



df=pd.DataFrame(d)

df.to_csv(sys.stdout)