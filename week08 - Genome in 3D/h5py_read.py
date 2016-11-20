import h5py
import numpy as np
import os
import sys


file = h5py.File("Out.heat")

data_obj = open(sys.argv[1] )
# ctcf_ obj = open(sys.argv[2] )

ctcf_dict= {}
r_matrix=[]
chrX_matrix=[]
for rows in data_obj.readlines():
	if rows.startswith('##'):
		continue
	if rows.startswith('#Chromosome'):
		header_matrix = rows.rstrip('\n').split('\t')
		continue
	r_matrix.append(rows.rstrip('\n').split('\t')[0:])
	# print(rows.rstrip('\n').split('\t')[0])
	if rows.rstrip('\n').split('\t')[0] == 'chrX':
		chrX_matrix.append(rows.rstrip('\n').split('\t')[0:])
		ctcf_dict[rows.rstrip('\n').split('\t')[1]]=rows.rstrip('\n').split('\t')[0:]



counts = file['0.counts'][...]
expexted = file['0.expected'][...]
regions = file['regions'][...]
positions = file['0.positions'][...]

ratio = np.log(counts/(expexted))

# print(positions[1][1])
# print(positions)
for  index,range_chr in enumerate(positions):
	# print(range_chr)
	output= 0;
	for key in ctcf_dict:
		if int(ctcf_dict[key][1])<range_chr[1] and  int(ctcf_dict[key][1])>=range_chr[0]:
			output = 1 
			break
	if output==0:
		continue
	max_hit= ratio[index][0]
	index_hit = 0
	last_maxhit= max_hit
	for index_r,number in enumerate(ratio[index]):
		if number >= max_hit:
			last_maxhit= max_hit 
			max_hit= number
			index_hit= index_r
	if max_hit == last_maxhit:
		print('multiple hit found')
	print(positions[index],positions[index_hit])


# print(ratio)
# print(ctcf_dict)


