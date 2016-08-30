# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys

sam_file = "/Users/cmdb/data/day2_lunch/SRR072893.sam"

at_count=0
aligment_count= 0

for line in sam_file:
    if line.startwith("@"):
        at_count= at_count + 1
        continue
    aligment_count= aligment_count + 1
    
print(at_count,aligment_count)

