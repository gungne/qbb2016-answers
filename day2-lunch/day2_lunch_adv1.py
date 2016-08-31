#!/usr/bin/env python

import sys
import re

sam = sys.stdin

plus_count=0
minus_count=0
none_count=0
for line in sam:
	if line.startswith("@"):
		continue
	item = line.rstrip("\r\n").split("\t")
	for char in item[6]:
		if char=="N":
			if int(item[1])&int(32) == True:
				minus_count= minus_count + 1
			else:
				plus_count = plus_count+1 
		else:
			none_count=none_count+1


print(plus_count,minus_count,none_count)

