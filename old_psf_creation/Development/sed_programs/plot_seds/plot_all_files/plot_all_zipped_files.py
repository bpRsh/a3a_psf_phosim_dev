#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jun 24, 2016
# Last update :

# Inputs      : all .gz file in a folder
#               
# Outputs     : input + .png

# Info:
# 1. This program plots all .gz datafiles from a folder.
#       

## Input/output info:
## for fname in glob.glob('*.gz'):
## outimage = fname[0:-2] + '.png'
## 
## 
 

# Imports
import glob
import matplotlib.pyplot as plt
import numpy as np


for fname in glob.glob('*.gz'):

    # pring readin file
    print('{} {} {}'.format('\nreading file : ',fname, ''))

    # get the data
    x,y = np.genfromtxt(fname,delimiter=None,usecols=(0,1),dtype=float,unpack=True)

    fig, ax = plt.subplots()
    ax.plot(x,y)

    title = str(fname)
    ax.set_title(title)
    ax.set_xlabel('wavelength (nm)',fontsize=16,fontweight="bold")
    ax.set_ylabel('Flux',fontsize=16,fontweight="bold")
    
    ## save figure
    outimage = fname[0:-2] + 'png'
    print('{} {}'.format('output image : ',outimage ))
    plt.savefig(outimage)
    #plt.show()


