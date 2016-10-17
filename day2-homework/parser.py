#!/usr/bin/env python

import re 
import sys

flybase = sys.stdin
for i,line in enumerate(flybase):
	if line.find("DROME")==-1:
		continue
	item = line.rstrip("\r\n").split()
	if len(item)==4:
		print(item[2],"\t",item[3])
	else:
		print(item[1],"\t",item[1]+'missing') 