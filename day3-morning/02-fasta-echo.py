#!/usr/bin/env python

import sys
import re
import fasta

file = sys.stdin
operand_1= fasta.fasta_parser(file)
print(operand_1)