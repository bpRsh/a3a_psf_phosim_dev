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
# Depends     : instance_catalogs/narrowband*.icat
#               seds/narrowband*.sed
#               backgrounds/background1.bkg
#
# Outputs     : phosim_output_zipped/narrowband*/17_zipped_psf_fitsfiles
#               
#               
# Info:
# 1. This program a1_create_background.py will create background/background.bkg
#    for this prog.
#
# 2. This program a2_create_seds.py will create seds/narrowband*.sed and
#    seds/broadband.sed for this prog.
#
# 3. This program a3_create_instance_catalogs.py will create instance_catalogs/narrowband*.icat and
#    seds/broadband.icat for this prog.
#
# 4. We can change seed, magnitude , sed etc while creating instance catalogs.
#
# 5. For 21 input instance catalogs this program will create 21 unzipped psfs.
#
# 6. We need only electron image and next script a5_unzip_all_psf
#
#  Estimated time :  minutes    
    '''
    
    # clobber output folder 
    output = 'phosim_output_zipped'
    if os.path.exists(output):
        shutil.rmtree(output)
    os.makedirs(output)

    # catalogs
    for i in range(21):
        
        subprogram = 'narrowband{:d}'.format(i)
        print('{} {} {}'.format('\n\n Begin running Phosim for catalog :',subprogram, '\n\n'))
    
    
        # create output dir
        outputdir1 = output + '/narrowband{:d}_out'.format(i)
        os.makedirs(outputdir1)
    
        # commands to run relative to phosim installation folder
        instance_catalog  = '../Research/psf_creation/' + \
                            'instance_catalogs/' + \
                            'narrowband{:d}.icat'.format(i)
                  
        background        = '../Research/psf_creation/' +\
                            'backgrounds/background1.bkg'
        
        outputdir2        = '../Research/psf_creation/' + outputdir1
        
        commands = 'cd ~/phosim;' + \
                   ' ./phosim '   + instance_catalog + \
                   ' -c '         + background + \
                   ' -o '         + outputdir2
              
    
        # run the program
        subprocess.call(commands,shell=True)
        
        print('{} {} {}'.format('\n\n End running Phosim for catalog :',subprogram, '\n\n'))
        
 



def run_phosim_broadband():

    # print
    print('{} {} {}'.format('\n\n Begin running Phosim for catalog :','broadband', '\n\n'))

    # output dir
    outputdir1         = 'phosim_output_zipped/broadband_out'
    if os.path.exists(outputdir1):
        shutil.rmtree(outputdir1)
    os.makedirs(outputdir1)
    
    # phosim command arguments relative to phosim installtion directory
    instance_catalog  = '../Research/psf_creation/instance_catalogs/broadband.icat'          
    background        = '../Research/psf_creation/backgrounds/background1.bkg'
    outputdir2        = '../Research/psf_creation/phosim_output_zipped/broadband_out'
    
    commands = r'cd ~/phosim;' + \
           r' ./phosim ' + instance_catalog + \
           r' -c '       + background + \
           r' -o '       + outputdir2
           
    subprocess.call(commands,shell=True)
    print('{} {} {}'.format('\n\n End running Phosim for catalog :','broadband', '\n\n'))


if __name__ == '__main__':


    # beginning time
    program_begin_time = time.time()
    begin_ctime        = time.ctime()
    
    run_phosim()
    run_phosim_broadband()


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
    
