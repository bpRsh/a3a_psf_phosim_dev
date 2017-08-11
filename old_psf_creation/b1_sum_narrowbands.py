#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jul 18, 2016
# Last update : Sep 13, 2016

# Inputs      : phosim_output_zipped/broadband_out/electron_image_zipfile
#               phosim_output_zipped/narrowband*_out/electron_image_zipfile
# Outputs     : phosim_output_zipped/narrowbands_sum.fits

# Info:
# 1. This program takes in two input fits file :
#       phosim_output_zipped/narrowbands_sum.fits, and, 
#       phosim_output_zipped/broadband_out/lsst_e_99999999_f2_R22_S11_E000.fits.gz, then
#       creates the difference of two as :
#       phosim_output_zipped/difference.fits
#
# Estimated time: 25 sec               

 

# Imports
from astropy.io import fits
import numpy as np
import subprocess
import time

# start time
start_time = time.time()

# get data shape from first input file
infile1 = 'phosim_output_zipped/narrowband0_out/lsst_e_99999999_f2_R22_S11_E000.fits.gz'
print('{} {} {}'.format('Reading data from: ',infile1, '\n'))
data1   = fits.getdata(infile1)
shape1   = data1.shape
print('{} {} {}'.format(r'shape[0] = ',shape1[0], ''))
print('{} {} {}'.format(r'shape[1] = ',shape1[1], '\n'))
dout = np.zeros((shape1[0],shape1[1]))


##=============================================================================
# input filenames
infiles = []
nfiles = 20
for i in range(nfiles):
    tmp = 'phosim_output_zipped/' + 'narrowband{:d}_out/'.format(i) + 'lsst_e_99999999_f2_R22_S11_E000.fits.gz'
    infiles.append(tmp)
    #print(tmp)

##=============================================================================
for i in range(nfiles):
    infile   = infiles[i]
    data     = fits.getdata(infile)
    dout     = dout + data
    hdu      = fits.PrimaryHDU()
    hdu.data = dout    
    print('{} {} {}{}'.format('shape of ',infile, ' = ', data.shape))

    # write output if shapes are same
    if (shape1 == data.shape):
        hdu.writeto('phosim_output_zipped/narrowbands_sum.fits', clobber=True)
    else:
        exit

##=============================================================================
#output info
print('{} {} {}'.format('\noutput file: ', 'phosim_output_zipped/narrowbands_sum.fits  ', ''))


# print the time taken
end_time = time.time()
seconds = end_time - start_time
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print("\nTime taken ==> {:2.0f} days, {:2.0f} hours,\
{:2.0f} minutes, {:f} seconds.".format( d, h, m, s))
