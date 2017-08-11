#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 11, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : psf_flux.txt
#               column0: psfname
#               column1: weight
#
# Info:
# 1. This program creates a textfile- psf_flux.txt
#    with psf weights from 1.0 to 1.2
#
#    Note: These weights are the average flux ratio of 100 f606 and f814
#          galaxies. (refer: ~/phosim/simdatabase/average_flux_ratio.py)
#
#

# Imports
import numpy as np

nfiles = 21
flux = np.linspace(1.0,1.2,num=nfiles,endpoint=True)
print(flux)

outfile = 'psf_flux.txt'
with open(outfile,'w') as fout:
    for i in range(nfiles):
        line = 'output_psfs/psf{}.fits'.format(i) + '\t' + str(flux[i]) + '\n'
        fout.writelines(line)

# output info
print('{} {} {}'.format('\noutput file = ',outfile, ''))
