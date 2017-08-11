#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016


# Imports
from __future__ import print_function
from __future__ import division
import numpy as np


infile = r'burrows.sed'

with open(infile, 'r') as f:
    data = f.readlines()

##=============================================================================
# get number of comments line
comments_lines = 0
for line in data:
    if line.strip().startswith('#'):
        comments_lines += 1
    else:
        break

print('{} {} {}'.format('comment_lines = ',comments_lines, '\n\n'))

##=============================================================================


lambda_start = 531.0
lambda_end = 696.0

# step between sed0 and sed1
step = (lambda_end-lambda_start) / 20.0


# sed file has decimal precision 1 so round off step to one precision
step = float(str(round(step, 1)))
print('{} {} {}'.format('lambda_start = ',lambda_start, 'nm'))
print('{} {} {}'.format('lambda_end = ',lambda_end, 'nm'))
print('{} {} {}'.format('step = ',step, ' nm\n'))

breakpoints = np.arange(lambda_start,lambda_end,step)
breakpoints = np.append(breakpoints, lambda_end)

print('{} {}{}'.format('breakpoints = \n', breakpoints,'' ))
print('{} {}{}'.format('\nlen breakpoints = ', len(breakpoints),'' ))


##=============================================================================
# get indices of these breakpoints
infile = r"burrows.sed"
idx = 0
lin_num = []
tmpidx = 0
with open(infile,'r') as fi:
    data = fi.readlines()
    for line in data:
        idx += 1
        for value in list(breakpoints):
            if line.startswith(str(round(value,1))):
                tmpidx = idx
                lin_num.append(tmpidx)
print('{} {} {}'.format('\nlin_num = \n',lin_num, '\n'))
#==============================================================================




#==============================================================================
def replace_line(infile, line_num, text):
    ''' This function replaces a given line number
        Usage: replace_line(infile, line_num, text)
    '''


    
    lines = open(infile, 'r').readlines()
    lines[line_num] = text
    out = open(infile, 'w')
    out.writelines(lines)
    out.close()
#==============================================================================




print('{} {}{}'.format('data[0] = \n', data[0],'' ))
print('{} {}{}'.format('lin_num[0] = ', lin_num[0],'' ))
print('{} {}{}'.format('lin_num[1] = ', lin_num[1],'' ))
print('{} {}{}'.format('lin_num[19] = ', lin_num[19],'' ))
print('{} {}{}'.format('lin_num[20] = ', lin_num[20],'\n' ))
##=============================================================================



## write out 20 output files
print('{} {} {}'.format('\nwriting 20 output files ...','', ''))
nfiles = 20
i = 0

for i in range(nfiles):
    outfile = 'seds/catalog{:d}.sed'.format(i)
    with open(outfile, 'w') as f:
        
        # add equal chunk_size data to all files
        lower = lin_num[i] -1
        upper = lin_num[i+1] -1

	#f.write(''.join(data))
	f.write( ''.join (  data[:comments_lines] ))

        for line in data:
            if not line.startswith('#'):
	        row=line.split()
		tmp = str(row[0]) + '    0.0\n'
	        f.write(''.join(tmp))

	#print('{} {}{}'.format('\ni = ', i,'' ))
	j = 0
        for j in range(lin_num[i], lin_num[i+1],1):
	    #pass
	    #print('{} {}{}'.format('j= ', j,'' ))
	    replace_line(outfile, j-1, data[j-1] )
	    #print('{} {}{}'.format('data[j] = ', data[j],'' ))

    # add one more line to last file
    if i == 19:
        replace_line(outfile, j, data[j] )
        

# write out file with range lambda_start to lambda_end
print('{} {} {}'.format('\nwriting combined sed ...','', ''))
outfile = 'combined.sed'
with open (outfile, 'w') as f:

    # write comments
    f.write( ''.join (  data[:comments_lines] ))

    # change columns two to zeros
    for line in data:
       if not line.startswith('#'):
        row=line.split()
        tmp = str(row[0]) + '    0.0\n'
        f.write(''.join(tmp))

    # replace line between lambda_start and lambda_end
    for j in range(lin_num[0], lin_num[20],1):
        replace_line(outfile, j-1, data[j-1] )
    
    # add one more line
    replace_line(outfile, j, data[j] )









            

