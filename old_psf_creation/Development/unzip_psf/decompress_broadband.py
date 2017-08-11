#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jul 18, 2016
# Last update :

# Inputs      : outputs/broadband_out/lsst_e_99999999_f2_R22_S11_E000.fits.gz
# Outputs     : outputs/broadband.fits

# Info:
# 1. This program takes in input fits file from outputs/broabdand_out/something.zip
#       and unzip it into outputs/something
#               
#               

# Imports
import gzip
import glob
import os
import time
import shutil

# start time
start_time = time.time()

# decompress broadband
indir = 'outputs' + r'/' + 'broadband_out'
outdir = 'outputs'
infile = indir + r'/' + r'lsst_e_99999999_f2_R22_S11_E000.fits.gz'
outfile = outdir + r'/' + 'broadband.fits'
print('{} {} {}'.format('\ninfile : ',infile, ''))
print('{} {} {}'.format('outfile: ',outfile, ''))

# read zipdata from input fitsfile
with gzip.open(infile, 'rb') as inzip:
    zipdata = inzip.read()

# write zipdata to output fitsfile
with open(outfile, 'wb') as f:
    f.write(zipdata)

        

# print the time taken
end_time = time.time()
seconds = end_time - start_time
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print("\nTime taken ==> {:2.0f} days, {:2.0f} hours,\
{:2.0f} minutes, {:f} seconds.".format( d, h, m, s))
