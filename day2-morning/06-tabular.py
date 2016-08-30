#!/usr/bin/env python

import sys 

for line in sys.stdin:
    if line.startwith("t_id"):
        print line.rstrip("\r\n")
        continue
    fields = line.rstrip("\r\n").split("\t")
    print fields
    field.append(length)
    "\t".join(fields)