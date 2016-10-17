#!/usr/bin/env python

import sys
import re

sam = sys.stdin

m=0

for line in sam:
	if line.startswith("@"):
		continue
	item = line.rstrip("\r\n").split("\t")
	if item[2]!="*":
		m=m+1
		print(item[2])
		if m==11:
			break

