#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 25, 2016
# Last update : Sep 02, 2016
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

from a1_create_instance_catalogs_0_20_seed import create_catalogs
from a2_phosim_narrow0_and_20              import run_phosim
from a3_unzip_psf_0_20                     import unzip_psf
from a4_imcat_e_rh_psf0_20                 import imcat_parameters_e_rh


def extreme_psf_phosim_imcat():
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
#               4. a4_imcat_e_rh_psf0_20.py
#                  extreme_psf/psf0_and_20.fits
#           
# Outputs     : extreme_psf_phosim_imcat_seed_e_rh.dat
#
# Info:
# 1. This program creates instance catalogs, uses them to create zipped psf using
#    Phosim, unzips these psf into the folder extereme_psf/psf0_20.fits .
#
# 2. Then, it finds imcat variables e and rh (e00 e10 rh0 e01 e11 rh1) for given seed.
#
# 3. Then, it copies the seed and the imcat variables into a big datafile called
#    extreme_psf_phosim_imcat_seed_e_rh.dat
#
# N.B.:  SIM_SEED should not start with zero, and it better not be very long digit.
#        suitable value is: sim_seed =  datetime.datetime.now().strftime("%d%H%M%S") 
#
# Estimated time: 6 min 27 sec (i.e. 6.5 min)
    
    '''


    nloop = 580
    for i in range(0,nloop): 
        
        # time to run the loop
        subprogram_start_time = time.time()
        sub_begin_ctime       = time.ctime()   
        
        # print loop info
        # one loop takes 6 min 30 seconds
        print("\n\n"+'#'*50+"\n# Running loop: ", i, '\n'+'#'*50+'\n\n')
        
        
        # 1. create instance catalogs  
        #    creates: instance_catalogs/narrowbans0_and_20.icat
        #    time   : 2 seconds
        print("\n\n"+'#'*50+"\n# Running create catalogs loop: ", i, '\n'+'#'*50+'\n\n')
        sim_seed1 = '1' # do not start sim_seed with 0
        sim_seed2 = datetime.datetime.now().strftime("%d%H%M%S") 
        sim_seed = sim_seed1 + sim_seed2 # 1,day_num of month, hour, min, sec
        create_catalogs(sim_seed)
        
        
        # 2. run phosim  
        ##    creates: phosim_output_extreme_psf/narrowband_0_and_20/zipped_psf
        ##    time   : 6 minutes
        print("\n\n"+'#'*50+"\n# Running phosim loop: ", i, '\n'+'#'*50+'\n\n')
        run_phosim()
        
        
        ## 3. unzip psf
        ##    creates: extreme_psf/psf0_and_20.fits 
        ##    time   : 1 second
        print("\n\n"+'#'*50+"\n# Running unzip_psf loop: ", i, '\n'+'#'*50+'\n\n')
        unzip_psf()
        
        
        ## 4. finds imcat variables e and rh
        ##    creates: imcat_variables.dat
        ##    time   : 23 seconds
        print("\n\n"+'#'*50+"\n# Running imcat variables loop: ", i, '\n'+'#'*50+'\n\n')
        erh = imcat_parameters_e_rh()
        
        # 5. write sim_seed and imcat variables into a file
        print("\n\n"+'#'*50+"\n# Writing imcat variables to a file loop: ", i, '\n'+'#'*50+'\n\n')
        outfile = 'extreme_psf_phosim_imcat_seed_e_rh.dat'
        line = str(sim_seed) + '  '       +\
               str(erh[0]) + '  ' + str(erh[1]) + '  ' + str(erh[2]) + '  ' +\
               str(erh[3]) + '  ' + str(erh[4]) + '  ' + str(erh[5]) + '\n'
               
               
        with open(outfile, 'a') as fout:
            fout.write(line)    
        
        #delete old folders at the end of the loop
        print("\n\n"+'#'*50+"\n# Deleting old outputs loop: ", i, '\n'+'#'*50+'\n\n')
        if os.path.exists('instance_catalogs')        : shutil.rmtree('instance_catalogs') 
        if os.path.exists('phosim_output_extreme_psf'): shutil.rmtree('phosim_output_extreme_psf')
        
        
        src   = 'extreme_psf'
        dest1 = 'outlier_psf'
        dest2 = dest1 + '/extreme_psf_{:d}'.format(int(sim_seed))
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
    extreme_psf_phosim_imcat()    
    
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
    
