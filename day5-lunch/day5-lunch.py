#!/usr/bin/env python

import sys
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

Ensemble_file_dir=sys.argv[1]

# window_input =sys.argv[3] 


Ensemble = pd.read_csv(Ensemble_file_dir,"\t")

print(Ensemble[Ensemble["feature"]=="start_codon"])