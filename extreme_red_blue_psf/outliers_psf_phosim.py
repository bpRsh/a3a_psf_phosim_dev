#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Aug 25, 2016
# Last update : Sep 07, 2016
#

     

# Imports
import subprocess  
import os     
import shutil 
import re
import sys 
import datetime
import time
import numpy as np

from a1b_create_instance_catalogs_seed import create_catalogs
from a2b_phosim_all_narrowbands        import run_phosim
from a3b_unzip_all_psf                 import unzip_psf


def outlier_psf_phosim():
    '''
# Depends     : 1. a1_create_instance_catalogs_0_20_seed.py
#                  argument: the SIM_SEED to run this program
#                            
#               2. a2_phosim_narrow0_and_20.py   # gives zipped psfs
#                  ./instance_catalogs
#                  ./seds
#                  ./backgrounds
#
#               3. a3_unzip_psf_0_20.py
#                  phosim_output_extreme_psf/narrowband_0_and_20/zipped_psf
#
#           
# Outputs     : outlier_psf/outlier_psf_seed/psf0_20.fits
#
# Info:
# 1. This program creates instance catalogs, uses them to create zipped psf using
#    Phosim software, then unzips these psf into the folder
#    extereme_psf/psf0_20.fits .
#
# 2. Then, it copies this folder into output folder with given seed number.
#
#    Note: dest1 = 'outlier_psf'
# 
#
# Estimated time: 6 min 27 sec (i.e. 6.5 min) for one seed
    
    '''


    
    #sim_seed_lst=[103105035,104141804,105111823,102221250,102230033,104184839,104211258]
    nloop = len(sim_seed_lst)
    for i in range(0,nloop):
        
        # seed
        seed = sim_seed_lst[i] 
        
        # time to run the loop
        subprogram_start_time = time.time()
        sub_begin_ctime       = time.ctime()   
        
        # print loop info
        # one loop takes 6 min 30 seconds
        print("\n\n"+'#'*50+"\n# Running loop for seed: ", seed, '\n'+'#'*50+'\n\n')
        
        
        # 1. create instance catalogs  
        #    creates: instance_catalogs/narrowbans0_and_20.icat
        #    time   : 2 seconds
        print("\n\n"+'#'*50+"\n# Running create catalogs loop: ", seed, '\n'+'#'*50+'\n\n')
        create_catalogs(seed)
        
        
        # 2. run phosim  
        ##    creates: phosim_output_extreme_psf/narrowband_0_and_20/zipped_psf
        ##    time   : 6 minutes
        print("\n\n"+'#'*50+"\n# Running phosim loop: ", seed, '\n'+'#'*50+'\n\n')
        run_phosim()
        
        
        ## 3. unzip psf
        ##    creates: extreme_psf/psf0_and_20.fits 
        ##    time   : 1 second
        print("\n\n"+'#'*50+"\n# Running unzip_psf loop: ", seed, '\n'+'#'*50+'\n\n')
        unzip_psf()
        
        

        
        #delete old folders at the end of the loop
        print("\n\n"+'#'*50+"\n# Deleting old outputs loop: ", seed, '\n'+'#'*50+'\n\n')
        
        # delete instance catalogs
        outfolder = 'instance_catalogs'
        if os.path.exists(outfolder): 
            shutil.rmtree(outfolder)
        
        # delete phosim output for zipped psf
        outfolder = 'phosim_output_extreme_psf' 
        if os.path.exists(outfolder): 
            shutil.rmtree(outfolder)
            
        # copy extreme psf with given seed number
        src   = 'extreme_psf'
        dest1 = 'outlier_psf'
        dest2 = dest1 + '/extreme_psf_{:d}'.format(int(seed))
        if os.path.exists(src) :
            if not os.path.exists(dest1): os.makedirs(dest1)
            if not os.path.exists(dest2): shutil.copytree(src,dest2 ) 
            shutil.rmtree(src) 
        
##==============================================================================
## Main program
##==============================================================================
if __name__ == '__main__':
    
    # beginning time
    program_begin_time = time.time()
    begin_ctime        = time.ctime()
    
    # run main program
    outlier_psf_phosim()  
    
    # print the time taken
    program_end_time = time.time()
    end_ctime        = time.ctime()
    seconds          = program_end_time - program_begin_time
    m, s             = divmod(seconds, 60)
    h, m             = divmod(m, 60)
    d, h             = divmod(h, 24)
    print('\nBegin time: ', begin_ctime)
    print('End   time: ', end_ctime,'\n')
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))
    
