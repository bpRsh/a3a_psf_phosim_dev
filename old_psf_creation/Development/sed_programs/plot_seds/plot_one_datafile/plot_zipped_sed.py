#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jun 24, 2016
# Last update :

# Inputs      : a sed file (zipped or non_zipped), e.g. 
#               km01_7000.fits_g40_7180.gz
# Outputs     : input.png, e.g.
#               km01_7000.fits_g40_7180.gz.png

# Info:
# 1. This program plots the given zipped/unzipped datafile
#       

## Input/output info:
## infile = 'km01_7000.fits_g40_7180.gz'
## outimage = infile + '.png'
## 
## 

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#==============================================================================
# read in a file
infile = 'km01_7000.fits_g40_7180.gz'
colnames = ['c0', 'c1']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,1))

print(df.head())
print("\n")


#==============================================================================
## plot wave vs trans
plt.plot(df.c0,df.c1,linewidth=1,color='b')
plt.axhline(y=.05, color = 'm', linestyle='--')

# title and axes labels
plt.title(infile)
plt.xlabel('Wavelength (nm) ', fontsize=14)
plt.ylabel('Flux', fontsize=14)



# axes limit
plt.xlim(500,700)
#plt.ylim(0,0.2)

# grid
plt.grid(True)

## save figure
outimage = infile + '.png'
print('{} {}'.format('\noutput image = ',outimage ))
plt.savefig(outimage)
plt.show()
# end
#==============================================================================

