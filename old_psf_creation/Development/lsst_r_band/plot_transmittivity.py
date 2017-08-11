#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jun 24, 2016
# Last update : Aug 09, 2016

# Inputs      : filter_2.txt
#               
# Outputs     : filter_2.png
#               

# Info:
# 1. This program plots wavelength vs transmittivity.
#    This reads second(1) and third(2) columns data using pandas_read_csv
#    and converts wavelenght to nm (from micron) when plotting.
#       
 

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# input/output
#infile = 'sed_flat.txt'
infile = 'filter_2.txt'
outimage = infile[0:-3] + 'png'

#==============================================================================
# read in a file
infile = infile
colnames = ['c1', 'c2']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(1,2),
                 skipfooter=42347,engine='python')

# we are reading only for angle 14.2 for filter_2.txt
# comment lines = 5 (we dont have to worry, we count from bottom)
# last line num of 14.2 = 906
# last line of file = 43253
# skipfooter = 43253-906 = 42347

print(df.c1.head() * 1000)
print(df.c1.tail(20) * 1000)
print(df.c2.head())
print(df.c2.tail(20))
print("\n")


#==============================================================================
## plot wave vs trans
plt.plot(df.c1 * 1000 , df.c2,linewidth=1,color='b')

# title and axes labels
plt.title(infile)
plt.xlabel('Wavelength (nm) ', fontsize=14)
plt.ylabel(r'Transmittivity ', fontsize=14)



# axes limit

plt.xlim(-100,1300)
plt.ylim(0,1.1)

# grid
plt.grid(True)

## save figure
outimage = outimage
print('{} {}'.format('\noutput image = ',outimage ))
plt.savefig(outimage)
plt.show()
# end
#==============================================================================

