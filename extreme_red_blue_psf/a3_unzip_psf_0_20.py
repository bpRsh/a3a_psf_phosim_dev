#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 25, 2016
# Last update : 
#


# Imports
import gzip
import glob
import os
import time
import shutil

def unzip_psf():
    '''
# Depends     : phosim_output_extreme_psf/narrowband0_out/zipped_psf
#
# Outputs     : extreme_psf/psf0.fits_and_20
#
# Info:
# 1. This program will unzip zipped psf output from phosim software into 
#    extreme_psf folder.
#
#  Estimated time: 0.7 seconds    
    '''
    
    print('{} {} {}'.format('\nRunning unzip_psf_0_20','', ''))

    # clobber outdir
    outdir = 'extreme_psf'
    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    
    os.makedirs(outdir)
    
    
    ##==============================================================================
    icatlist= [0,20]
    for i in range(len(icatlist)):
        num = icatlist[i]
        
        # input/output info
        indir = 'phosim_output_extreme_psf' + r'/' + 'narrowband{:d}_out'.format(num)
        infile = indir + r'/' + r'lsst_e_99999999_f2_R22_S11_E000.fits.gz'
        outfile = outdir + r'/' + 'psf{:d}.fits'.format(num)
        print('{} {:d} {}'.format('\ncount  : ', num, ''))
        print('{} {} {}'.format('infile : ',infile, ''))
        print('{} {} {}'.format('outfile: ',outfile, ''))
    
        # read zipdata
        with gzip.open(infile, 'rb') as inzip:
            zipdata = inzip.read()
    
        # write zipdata to files
        with open(outfile, 'wb') as f:
            f.write(zipdata)
        
    
    print('{} {} {}'.format('\nEnd of unzip_psf_0_20','', ''))


if __name__ == '__main__':
    #unzip_psf()
    pass
