#!/usr/bin/env python

import sys
import re

sam = sys.stdin
#alig_count=0
#count=0
#locat_uniq_count= 0
#m=0
#n=0
#sum_MAPQ=0
plus_count=0
minus_count=0
none_count=0
for line in sam:
	if line.startswith("@"):
		continue
	item = line.rstrip("\r\n").split("\t")
	Match_switch= 0
	for char in item[5]:
		if char=="N":
			if item[2]==
			break
#problem5
#	n=n+1
#	sum_MAPQ=sum_MAPQ + int(item[4])

#print(sum_MAPQ/n)
#problem4
#	print(item[2])
#	m=m+1
#	if m==11:
#		break


#problem3
#	if item[-1] == "NH:i:1":
#		locat_uniq_count= locat_uniq_count+1
#problem1
#	count= count +1 

#problem2
#	Match_switch= 0
#	for char in item[5]:
#		if char=="M":
#			alig_count = alig_count +1
#			break


#print(locat_uniq_count)


#print(alig_count)
