#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016

# inputs : angle.txt
# outputs : angle.png

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#==============================================================================
# read in a file
infile = 'angle.txt'
colnames = ['angle', 'wave','trans', 'refl']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,1,2,3))

print(df.head())
print("\n")


#==============================================================================
## plot wave vs trans
plt.plot(df.wave,df.trans,linewidth=1,color='b')
plt.axhline(y=.05, color = 'm', linestyle='--')

# title and axes labels
plt.title('Plot of wavelength vs transmission probability')
plt.xlabel('Wavelength (nm) ', fontsize=14)
plt.ylabel('Transmittivity', fontsize=14)


# text marker
txt = r'transmission = 5%'
plt.text(410, 0.06, txt)

# axes limit
plt.xlim(400,800)
plt.ylim(0,1.2)

# grid
plt.grid(True)

# save figure
imagename = 'angle.png'
print('{} {}'.format('\noutput image = ',imagename ))
plt.savefig(imagename)
plt.show()
# end
#==============================================================================

