#!/usr/bin/env python

import sys
import re

sam = sys.stdin

locat_uniq_count= 0
for line in sam:
	if line.startswith("@"):
		continue
	item = line.rstrip("\r\n").split("\t")

	if item[-1] == "NH:i:1":
		locat_uniq_count= locat_uniq_count+1


#problem2
#	Match_switch= 0
#	for char in item[5]:
#		if char=="M":
#			alig_count = alig_count +1
#			break


print(locat_uniq_count)


#print(alig_count)
