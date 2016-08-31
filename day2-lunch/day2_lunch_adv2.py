#!/usr/bin/env python

import sys
import re

sam = sys.stdin

count=0
for line in sam:
	if line.startswith("@"):
		continue
	item = line.rstrip("\r\n").split("\t")
	if item[2]=="2L" and int(item[3])<=20000 and int(item[3])>=10000:
		count=count+1

print(count)



