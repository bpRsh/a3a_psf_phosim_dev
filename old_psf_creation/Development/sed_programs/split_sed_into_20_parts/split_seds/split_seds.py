#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016


# Imports
import numpy as np
import os
import shutil
import time

# start time
start_time = time.time()

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
print('{} {} {}'.format('\nlin_num = \n',lin_num, ''))             # [ 2313 ...  3953 3963]
print('{} {} {}'.format('\nlen lin_num = \n',len(lin_num), '\n'))  # 22
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
print('{} {}{}'.format('len data = ', len(data),'' ))
print('{} {}{}'.format('last data = ', data[(len(data)-1)],'' ))
print('{} {}{}'.format('lin_num[0] = ', lin_num[0],'' ))
print('{} {}{}'.format('lin_num[1] = ', lin_num[1],'' ))
print('{} {}{}'.format('lin_num[19] = ', lin_num[19],'' ))
print('{} {}{}'.format('lin_num[20] = ', lin_num[20],'' ))
print('{} {}{}'.format('lin_num[21] = ', lin_num[21],'' ))
##=============================================================================

# remove output directory if exists, and create new
outfolder = 'seds'

# delete the output folder, to create again
shutil.rmtree(outfolder, ignore_errors=True)

# create output dir
os.mkdir(outfolder)


##=============================================================================
## write out 20 output files
print('{} {} {}'.format('\nwriting 20 output files ...','', '\n'))
nfiles = 20
i = 0

for i in range(nfiles):
    outfile = outfolder + r'/' + 'catalog{:d}.sed'.format(i)
    with open(outfile, 'a') as f:

        # print
        print('{} {} {}'.format('writing to the file ',outfile, '...'))
        
        # add equal chunk_size data to all files
        lower = lin_num[i] -1
        upper = lin_num[i+1] -1

        #write comment lines
        f.write( ''.join (  data[:comments_lines] ))

        for line in data:
            if not line.startswith('#'):
                row=line.split()
                tmp = str(row[0]) + '    0.0\n'
                f.write(''.join(tmp))

	    ##print('{} {}{}'.format('\ni = ', i,'' ))
        j = 0
        for j in range(lin_num[i], lin_num[i+1],1):
            #print('{} {}{}'.format('j= ', j,'' ))
            replace_line(outfile, j-1, data[j-1] )
	        ##print('{} {}{}'.format('data[j] = ', data[j],'' ))

    ## add extra lines from index20 to index21 to last file
    # -1 is for 695.0
    if i == 19:
        for j in range(lin_num[20]-1, lin_num[21],1):    
            replace_line(outfile, j, data[j] )
        

# write out file with range lambda_start to lambda_end
outfile = outfolder + r'/' + 'broadband.sed'
print('{} {} {}'.format('writing to the file ',outfile, '...'))
with open (outfile, 'a') as f:

    # write comments
    f.write( ''.join (  data[:comments_lines] ))

    # change column two to zeros
    for line in data:
       if not line.startswith('#'):
        row=line.split()
        tmp = str(row[0]) + '\t' + '0.0\n'
        f.write(''.join(tmp))

    # replace line between lambda_start and lambda_end
    for j in range(lin_num[0], lin_num[21],1):
        replace_line(outfile, j-1, data[j-1] )
    
    # add one more line
    replace_line(outfile, j, data[j] )





# time taken by the program
end_time   = time.time()
time_taken = (end_time - start_time) 
print('{} {:.2f} {}'.format('\nTime taken to run this program = ',time_taken, ' seconds'))
