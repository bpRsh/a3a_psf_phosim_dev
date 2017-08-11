#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 20, 2016


# inputs : burrows.sed and filter_2.txt
# outputs: trial_seds/   and may be, angle.txt, angle_trans.txt

# This program reads in sed file (burrows.sed) and filter file (filter_2.txt)
# choose filter range such that wavelength lies between 5% of transmissivity.
# lambda_start <= (trans=0.05)  and lambda_end > (trans=0.05)
# then breaks wavelength range into 20 waverangeBorders, create sed for these waverangeBorders
# with corresponding fluxes from sed file.


# Imports
import numpy as np
import pandas as pd
import os, shutil

# read in sed file 'burrows.sed'
#==============================================================================
# read in a file
#
infile = 'burrows+2006c91.21_T1350_g4.7_f100_solar'
colnames = ['wave', 'flux']
print('{} {} {} {}'.format('\nreading file: ', infile, '','' ))
df1 = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,1))

print('{} {} {} {}'.format('inputfile header: \n', df1.head(),'','\n'))

# change second column all flux = 0.0
df1a = df1.copy()
df1a.flux = 0.0


# read in filter file 'filter_2.txt'
#==============================================================================
# read in a file
#
infile = 'filter_2.txt'
colnames = ['angle','wave','trans','refl']
print('{} {} {} {}'.format('\nreading file: ', infile, '','' ))
df2 = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,1,2,3))
#==============================================================================

df2.wave = df2.wave * 1000.0 # micron to nm
print('{} {} {}'.format('input file header: \n', df2.head(),'\n'))

# angle = 14.2
df3 = df2[df2.angle.values==14.2]
df3.to_csv('angle.txt',index=None,header=None,sep='\t')


# trans >= 0.05
df4 = df3[df3.trans.values>=0.05]
df4.to_csv('angle_trans.txt',index=None,header=None,sep='\t')

# add a line to trans >= 0.05 from filter_2.txt
##=============================================================================

# print last line of angle_trans.txt
n = len(df4.trans)
print('{} {} {}'.format('last line of angle_trans.txt :\n',df4.iloc[[n-1]], '\n'))

# print value of wave from last line of angle_trans.txt
lambda_start = df4.wave.values[0]
print('{} {} {}'.format('lambda_start = ',lambda_start, 'nm\n'))



lambda_end_temp = df4.wave.values[n-1]
print('{} {} {}'.format('last lambda = ',lambda_end_temp, ''))
print('{} {} {}'.format('last value of wavelength of angle_trans.txt = ',lambda_end_temp, '\n\n'))





# find index for this value in filter_2.txt
myindices = df2.wave[df2.wave == lambda_end_temp].index.tolist()
print('{} {} {}'.format('index of that value in filter_2.txt = \n',myindices, ''))
print('{} {} {}'.format('type myindex',type(myindices), '\n'))


# print myindex line of filter_2.txt
n = myindices[0]
line = df2.iloc[[n]]
line2 = df2.iloc[[n+1]]
print('{} {} {}'.format('\nmyindex line from angle.txt:\n',line, ''))
print('{} {} {}'.format('\nnext line from angle.txt:\n',line2, '\n\n'))

# get lambda_end
lambda_end = df2.wave.values[n+1]



# step between sed0 and sed1
step = (lambda_end-lambda_start) / 20.0


# sed file has decimal precision 1 so round off step to one precision
step = float(str(round(step, 1)))
print('{} {} {}'.format('lambda_start = ',lambda_start, 'nm'))
print('{} {} {}'.format('lambda_end = ',lambda_end, 'nm'))
print('{} {} {}'.format('step = ',step, ' nm\n'))

waverangeBorders = np.arange(lambda_start,lambda_end,step)
for i in range(len(waverangeBorders)):
    waverangeBorders[i] = float(str(round(waverangeBorders[i], 1)))
    print('{} {} {}{}'.format('waverangeBorder',i, ' = ', waverangeBorders[i]))



# add last wavelength lambda_end to the numpy ndarray
print('{} {} {}'.format('\ntype waverangeBorders = ',type(waverangeBorders), ''))
waverangeBorders = np.append(waverangeBorders, [lambda_end])

for i in range(len(waverangeBorders)):
    waverangeBorders[i] = float(str(round(waverangeBorders[i], 1)))
    print('{} {} {}{}'.format('waverangeBorder',i, ' = ', waverangeBorders[i]))

#=============================================================================
# get indices of these values from burrows.sed
indices = []

print('{} {} {}'.format('\n\nindex for wavlength in sed file','', ''))
print('{} {} {}'.format('add three to index (two comments, first index is zero)','', ''))
for j in range( len(list(waverangeBorders)) ):
    print("\n")
    print(j)
    print (waverangeBorders[j])
    value = str(waverangeBorders[j])
    value = float(value)
    tmpindex = df1.wave[df1.wave == value ].index.tolist()[0]
    print(tmpindex)
    indices.append(tmpindex)


# print myindex line of burrows.sed
n0 = indices[0]
line0 = df1.iloc[[n0]]
n21 = indices[21]
line21 = df1.iloc[[n21]]
print('{} {} {}'.format('\nmyindex line from sed file :\n',line0, '\n\n'))
print('{} {} {}'.format('\nmyindex line from sed file :\n',line21, '\n\n'))

#==============================================================================
# remove output directory if exists, and create new
outfolder = 'seds/'

# delete the output folder, to create again
shutil.rmtree(outfolder, ignore_errors=True)

# create output dir
os.mkdir(outfolder)

#==============================================================================
# create 20 output files with only comments
print("\n\n")
infile = 'burrows+2006c91.21_T1350_g4.7_f100_solar'
nfiles = 20
comments = []
i = 0
with open(infile, 'r') as fi:
    for i in range(nfiles):
        outfile = (outfolder+'catalog{:d}.sed'.format(i))
        #print('{} {} {}'.format('outfile = ',outfile, ''))
        with open (outfile, 'a') as fo:
            fi.seek(0)
            for line in fi.readlines():
                if line.startswith('#'):
                    comments.append(line)
                    #print(line)
                    fo.write(line)
                    i += 1


print('{} {} {}'.format(r'indices[21] = ',indices[21], ''))
## append data to output files, which had only comments
###=============================================================================
nfiles = 20
for i in range(nfiles-1):
    print("\n")
    print(i)
    print(indices[i])

    df = df1.copy()
    df[:indices[i]] = 0.0
    df[indices[i+1]:] = 0.0
    df.wave = df1.wave

    outfile = outfolder + 'catalog{:d}.sed'.format(i)
    print('{} {}{}'.format('outfile = ', outfile,'' ))
    df.to_csv(outfile,index=None,header=None,sep='\t',mode='a')
    

# add extra values to last file
df = df1.copy()
df[:indices[19]] = 0.0
df[indices[21]+1:] = 0.0
df.wave = df1.wave
outfile = outfolder + 'catalog19.sed'
df.to_csv(outfile,index=None,header=None,sep='\t',mode='a')


# create broadband.sed with only comments
outfile = 'seds/broadband.sed'
infile = 'burrows+2006c91.21_T1350_g4.7_f100_solar'
with open (outfile, 'a') as fo,open(infile, 'r') as fi:
    for line in fi.readlines():
        if line.startswith('#'):
            comments.append(line)
            #print(line)
            fo.write(line)
            i += 1



# add values to broadband.sed
df = df1.copy()
df[:indices[0]] = 0.0
df[indices[21]+1:] = 0.0
df.wave = df1.wave
outfile ='seds/broadband.sed'
df.to_csv(outfile,index=None,header=None,sep='\t',mode='a')





   
