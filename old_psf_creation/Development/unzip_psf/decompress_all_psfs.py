#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jul 18, 2016
# Last update :

# Inputs      : outputs/all_folders/zipfiles_of_electron_images
# Outputs     : output_psfs/unzipped_files_of_all_electron_images

# Info:
# 1. This program takes in input fits file from outputs/all_folders/zipfiles_of_electron_images
#       and unzip it into output_psfs/unzipped_files_of_all_electron_images.
#
              
# !!WARNING!! This program will clobber the folder : output_psfs

# Imports
import gzip
import glob
import os
import time
import shutil

# start time
start_time = time.time()

outdir = r'output_psfs'

# clobber outdir
if os.path.exists(outdir):
    shutil.rmtree(outdir)

os.makedirs(outdir)


##=============================================================================
nfiles = 20
for i in range(nfiles):
    
    # input/output info
    indir = 'outputs' + r'/' + 'narrowband{:d}_out'.format(i)
    infile = indir + r'/' + r'lsst_e_99999999_f2_R22_S11_E000.fits.gz'
    outfile = outdir + r'/' + 'psf{:d}.fits'.format(i)
    print('{} {:d} {}'.format('\ncount  : ', i, ''))
    print('{} {} {}'.format('infile : ',infile, ''))
    print('{} {} {}'.format('outfile: ',outfile, ''))

    # read zipdata
    with gzip.open(infile, 'rb') as inzip:
        zipdata = inzip.read()

    # write zipdata to files
    with open(outfile, 'wb') as f:
        f.write(zipdata)


# decompress broadband
indir = 'outputs' + r'/' + 'broadband_out'
infile = indir + r'/' + r'lsst_e_99999999_f2_R22_S11_E000.fits.gz'
outfile = outdir + r'/' + 'broadband.fits'
print('{} {} {}'.format('\ninfile : ',infile, ''))
print('{} {} {}'.format('outfile: ',outfile, ''))

# read zipdata
with gzip.open(infile, 'rb') as inzip:
    zipdata = inzip.read()

# write zipdata to files
with open(outfile, 'wb') as f:
    f.write(zipdata)


# WARNING:
print('{} {} {}'.format('\n!!WARNING!! This program will clobber the folder :',outdir, ''))
        

# print the time taken
end_time = time.time()
seconds = end_time - start_time
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print("\nTime taken ==> {:2.0f} days, {:2.0f} hours,\
{:2.0f} minutes, {:f} seconds.".format( d, h, m, s))
