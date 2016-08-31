#!/usr/bin/env python

import sys
import re

sam = sys.stdin

count=0
for line in sam:
	if line.startswith("@"):
		continue
	item = line.rstrip("\r\n").split("\t")
	if int(item[1])&int(16):
		count=count+1

print(count)





