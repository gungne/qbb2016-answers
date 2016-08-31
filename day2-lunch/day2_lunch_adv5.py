#!/usr/bin/env python

import sys
import re

sam = sys.stdin
I_count={}
count=0
for line in sam:
	if line.startswith("@"):
		continue
	item = line.rstrip("\r\n").split("\t")
	if item[5].find("I")!=-1:
		extract = re.findall("[0-9]*I",item[5])[0]
		I_number= re.sub("I","",extract)
		I_count['more than 4']=0
		if int(I_number)>4:
			I_count['more than 4'] = ['more than 4'] +1
			continue
		if I_number not in I_count:
			I_count[I_number]=1
		else:
			I_count[I_number]=I_count[I_number]+1

print(I_count)

			

		






