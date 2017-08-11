#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jun 24, 2016
# Last update : Aug 09, 2016

# Inputs      : a sed file (zipped or non_zipped), e.g. 
#               km01_7000.fits_g40_7180.gz
# Outputs     : input.png, e.g.
#               km01_7000.fits_g40_7180.gz.png

# Info:
# 1. This program plots the given sed datafile
#       
 

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# input/output
#infile = 'sed_flat.txt'
infile = 'seds/broadband.sed'
outimage = infile[0:-4] + '.png'

#==============================================================================
# read in a file
infile = infile
colnames = ['c0', 'c1']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,1))

print(df.head())
print("\n")


#==============================================================================
## plot wave vs trans
plt.plot(df.c0,df.c1,linewidth=1,color='b')

# title and axes labels
plt.title(infile)
plt.xlabel('Wavelength (nm) ', fontsize=14)
plt.ylabel(r'Flux (ergs cm-2 s-1 nm-1)', fontsize=14)



# axes limit
# uncomment for broadband.sed
# comment for sed_flat.txt
plt.xlim(500,700)
plt.ylim(1e-12,7e-12)

# grid
plt.grid(True)

## save figure
outimage = outimage
print('{} {}'.format('\noutput image = ',outimage ))
plt.savefig(outimage)
plt.show()
# end
#==============================================================================

