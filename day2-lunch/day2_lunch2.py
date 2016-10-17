#!/usr/bin/env python

import sys
import re

sam = sys.stdin
alig_count=0

for line in sam:
	if line.startswith("@"):
		continue
	items = line.rstrip("\r\n").split("\t")


	Match_switch= 0
	for item in items:
		if item=="H0:i:1":
			alig_count = alig_count +1
			break



print(alig_count)
