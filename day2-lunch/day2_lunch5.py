#!/usr/bin/env python

import sys
import re

sam = sys.stdin

n=0
sum_MAPQ=0

for line in sam:
	if line.startswith("@"):
		continue
	item = line.rstrip("\r\n").split("\t")
	n=n+1
	sum_MAPQ=sum_MAPQ + int(item[4])

print(sum_MAPQ/n)
