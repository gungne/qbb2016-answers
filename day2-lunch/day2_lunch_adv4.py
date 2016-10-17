#!/usr/bin/env python

import sys
import re

sam = sys.stdin

count=0
for line in sam:
	if line.startswith("@"):
		continue
	item = line.rstrip("\r\n").split("\t")
	qual=0
	for char in item[10]:
		qual=qual+ord(char)-33
	if qual/len(item[10])>30:
		count=count+1

print(count)





