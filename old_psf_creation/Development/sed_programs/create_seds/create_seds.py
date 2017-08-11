#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date      : Jun 22, 2016
# Last update: 

# Inputs    : sed_flat.txt
# Outputs   : seds/broadband.sed and narrowband*.sed

# Info:
# 1. This program takes in ONE input_sed_file and creates TWENTY_ONE output_sed files.
# 2. The input sed file has two columns: wavelength (nm) and flux (ergs/cm^2/s/nm)
#    wavelength varies from 300 nm to 1200 nm.
# 3. We can plot wavelength vs flux and see the sed, which looks like Capital PI
# 4. To create output_seds from this input_sed_file, we first decrease the
#    flux at 500 nm wavelength by a factor of 100 so that when phosim software
#    uses this flux to normalize all the values, it will have lesser impact.
#    i.e. sed_flat.txt    : 500.000  3.97290e-12
#         narrowband*.sed : 500.000  3.9728999999999995e-14
#         broadband.sed   : 500.000  3.9728999999999995e-14
# 5. Now, from the LSST_RED_BAND_FILTER_FILE we see that the values of wavelength
#    where transmission is NOT <= 5%.
#    We found that the wavelength range to be 531-696 nm.
# 6. So, we will take the wavelength range only between this range and set all
#    the other wavelength fluxes to zero EXCEPT for 500 nm case.



# sed_info:
# source_input_sed_file: phosim/data/SEDs/flatSED/sed_flat.txt
# column0              : wavelength (300-1200 nm)
# column1              : flux (ergs/cm^2/s/nm)
# e.g.                 : phosim/data/SEDs/kurucz/km01_7000.fits_g40_7120

# filter_info:
# source_red_band_filter_lsst : phosim/data/lsst/filter_2.txt
# We take wavelength range such that transmission <= 5%, and we get 531 nm - 696 nm.
# We can plot sed_file and see the flat peak and negligible bottom fluxes.



# Imports
import numpy as np
import os
import shutil
import time

# start time
start_time = time.time()
print('\nCurrent time: ', time.ctime())

## Input/output files
## infile = r'sed_flat.txt'
## outfolder = 'seds'
## outfile = outfolder + r'/' + 'narrowband{:d}.sed'.format(i)
## outfile = outfolder + r'/' + 'broadband.sed'


# read input sed file
infile = r'km01_7000.fits_g40_7120.sed'
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

##=============================================================================
# get normalize line of 500 nm

lookup = '500.0'
normalize_line = ''
normalize_line_num = 0
with open(infile) as f:
    for num, line in enumerate(f, 1):
        if lookup in line:
            normalize_line = line
            normalize_line_num = num - 1
            #print ('normalize line = ', line)
            #print ('normalize line num = ', num)

print('{} {} {}'.format('normalize_line            : ',normalize_line, ''))
print('{} {} {}'.format('normalize_line_num        : ',normalize_line_num, ''))
print('{} {} {}'.format(r'data[normalize_line_num]  :',data[normalize_line_num], ''))

# decrease the flux of normalize line by a factor of 100
wave,flux = normalize_line.split()
print('{} {} {}'.format('wave = ',wave, ''))
print('{} {} {}'.format('flux = ',flux, ''))

flux = float(flux) / 1.0
normalize_line = str(wave) + '  ' + str(flux)
print('{} {} {}'.format('normalize_line = ',normalize_line, ''))



#=============================================================================
# from red band filter of lsst : phosim/data/lsst/filter_2.txt
# we take wavelength range such that transmission <= 5%, and we get 531 nm - 696 nm

lambda_start = 531.0  
lambda_end = 696.0

# step between sed0 and sed1
step = (lambda_end-lambda_start) / 20.0


# sed file has decimal precision 1, so round off step to one precision
step = float(str(round(step, 0)))
print('{} {} {}'.format('\nlambda_start = ',lambda_start, 'nm'))
print('{} {} {}'.format('lambda_end = ',lambda_end, 'nm'))
print('{} {} {}'.format('step = ',step, ' nm\n'))

breakpoints = np.arange(lambda_start,lambda_end,step)
breakpoints = np.append(breakpoints, lambda_end)

print('{} {}{}'.format('breakpoints = \n', breakpoints,'' ))
print('{} {}{}'.format('\nlen breakpoints = ', len(breakpoints),'' ))


##=============================================================================
# get indices of these breakpoints
infile = infile
idx = 0
lin_num = []
tmpidx = 0
with open(infile,'r') as fi:
    data = fi.readlines()
    for line in data:
        idx += 1
        for value in list(breakpoints):
            if (str(round(value,1))) in line:
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
    lines[line_num] = lines[line_num].lstrip() # lstrip removes leading spaces
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
shutil.rmtree(outfolder, ignore_errors=True)
os.mkdir(outfolder)


##=============================================================================
## write out 20 output files
print('{} {} {}'.format('\nwriting 20 output files ...','', '\n'))
nfiles = 20
i = 0

for i in range(nfiles):
    outfile = outfolder + r'/' + 'narrowband{:d}.sed'.format(i)
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
                tmp = str(row[0]) + '  0.0\n'
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
    # rewrite normalized line at 500 nm from input sed to all output files
    replace_line(outfile, normalize_line_num, normalize_line + '\n')

        
##=============================================================================
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
        tmp = str(row[0]) + '  ' + '0.0\n'
        f.write(''.join(tmp))

    # replace line between lambda_start and lambda_end
    for j in range(lin_num[0], lin_num[21],1):
        replace_line(outfile, j-1, data[j-1] )
    
    # add one more line
    replace_line(outfile, j, data[j] )
    

# rewrite normalized line at 500 nm from input sed to all output files
replace_line(outfile, normalize_line_num, normalize_line + '\n')
##=============================================================================

# output info
print('{} {} {}'.format('\ninput sed            : ',infile, ''))
print('{} {} {}'.format('output folder        : ',outfolder, ''))
print('{} {} {}'.format('output broadband sed :',outfile, ''))


# time taken by the program
end_time   = time.time()
time_taken = (end_time - start_time)
print('\nCurrent time                   = ', time.ctime())
print('{} {:.2f} {}'.format('Time taken to run this program = ',time_taken, ' seconds'))
