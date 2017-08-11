#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 20, 2016
# Last update : Aug 25, 2016
#



# Imports
import subprocess  
import os     
import shutil 
import re
import sys
import time






def run_phosim():
    '''
# Depends     : instance_catalogs/narrowband0.icat
#               instance_catalogs/narrowband20.icat
#               seds/narrowband0.sed
#               seds/narrowband20.sed
#               backgrounds/background1.bkg
#
# Outputs     : phosim_output_extreme_psf/narrowband0/17_zipped_psf_fitsfiles
#               phosim_output_extreme_psf/narrowband20/17_zipped_psf_fitsfiles
#               
#               
# Info:
# 1. This program runs narrowband0 and narrowband20 instance catalogs.
#    It creates zipped psf for them in the output directory.
#
# 2. This will clobber the previous output folder.
#
# 3. The program unzip_psf_0_20.py will extract psf0 and psf20.fits from this.
#
# 4. The program create_instance_catalogs_0_20_seed.py will 
#    create the instance catalogs needed by this program. 
#
#  Estimated time : 6 minutes    
    '''
    
    # clobber output folder 
    output = 'phosim_output_extreme_psf'
    if os.path.exists(output):
        shutil.rmtree(output)
    os.makedirs(output)

    # catalogs
    icatlist= [0,20]
    for i in range(len(icatlist)):
        num = icatlist[i]
        
        subprogram = 'narrowband{:d}'.format(num)
        print('{} {} {}'.format('\n\n Begin running Phosim for catalog :',subprogram, '\n\n'))
    
    
        # create output dir
        outputdir1 = output + '/narrowband{:d}_out'.format(num)
        os.makedirs(outputdir1)
    
        # commands to run relative to phosim installation folder
        # in my case ~/phosim
        instance_catalog  = '../Research/extreme_red_blue_psf/' + \
                            'instance_catalogs/' + \
                            'narrowband{:d}.icat'.format(num)
                  
        background        = '../Research/extreme_red_blue_psf/' +\
                            'backgrounds/background1.bkg'
        
        outputdir2        = '../Research/extreme_red_blue_psf/' + outputdir1
        
        commands = 'cd ~/phosim;' + \
                   ' ./phosim '   + instance_catalog + \
                   ' -c '         + background + \
                   ' -o '         + outputdir2
              
    
        # run the program
        subprocess.call(commands,shell=True)
        
        print('{} {} {}'.format('\n\n End running Phosim for catalog :',subprogram, '\n\n'))
        
 
if __name__ == '__main__':
    #run_phosim()
    pass
