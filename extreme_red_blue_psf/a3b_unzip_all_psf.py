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
# Depends     : phosim_output_extreme_psf/narrowband*_out/zipped_psf
#
# Outputs     : extreme_psf/psf*.fits
#
# Info:
# 1. This program will unzip zipped psf output from phosim software into 
#    extreme_psf folder.
#
#  Estimated time: 1 seconds    
    '''
    
    print('{} {} {}'.format('\nRunning a3b_unzip_all_psf','', ''))

    # clobber outdir
    outdir = 'extreme_psf'
    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    
    os.makedirs(outdir)
    
    
    ##==============================================================================
    for i in range(21):
        
        # input/output info
        indir = 'phosim_output_extreme_psf' + r'/' + 'narrowband{:d}_out'.format(i)
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
        
    
    print('{} {} {}'.format('\nEnd of a3b_unzip_all_psf','', ''))


if __name__ == '__main__':
    #unzip_psf()
    pass
