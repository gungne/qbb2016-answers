#!/usr/bin/env python

import sys
import re

sam = sys.stdin
alig_count=0

for line in sam:
	if line.startswith("@"):
		continue
	item = line.rstrip("\r\n").split("\t")
	if item[2]!="*":
		
		alig_count=alig_count+1


print(alig_count)
