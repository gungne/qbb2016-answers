#!/usr/bin/env python

import re 
import sys

def defaults_output(option="default"):
	if option == "ignore":
		pass
	elif option == "default":
		print("mismatch")
	else:
		print("option error")


mapping_file = open(sys.argv[1])
ctab_file = open(sys.argv[2])
option = sys.argv[3]

flydict={}
for line in mapping_file:
	item=line.rstrip("\r\n").split("\t")
	AC=item[0]
	gene_id = re.sub(" ","",item[1])
	flydict[gene_id]=AC
	#print(gene_id)

m=0
for line_ctab in ctab_file:
	#print(line_ctab)
	target = re.findall(r"gene_id \"[0-9A-Za-z]*\"",line_ctab)
	#print(target)
	extracted= re.sub(r"gene_id |\"","",str(target))
	extracted= re.sub(r"\[\'|\'\]","",extracted)
	#print(extracted)
	if extracted in flydict:
		m=m+1
		output = []
		print(extracted,"\t",line_ctab) 
		if m==100:
			break
	else:
		m=m+1
		defaults_output(option)
		if m==1000:
			break

#	extracted= re.sub("\"","",extracted)



