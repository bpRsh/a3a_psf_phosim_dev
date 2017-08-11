#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jun 24, 2016
# Last update : Aug 10, 2016
#
# Inputs      : instance_catalogs/catalog0.icat_and_catalog19.icat
#               backgrounds/background1.bkg
#
# Outputs     : out_psf_test/narrowband0/17_zipped_psf_fitsfiles
#               out_psf_test/narrowband19/17_zipped_psf_fitsfiles
#               
# Info:
# This program is for testing total number of pixels in all psfs.
# The psfs psf0,psf1,psf19, should have similar count of pixels.
#
## WARNING: This program deletes old OUTPUT_FOLDER and CREATES_NEW.
#
#  Estimated time : 7 minutes for magnitude = 24, and flat_sed.txt


# Imports
import subprocess  # subprocess.call(commands,shell=True)
import os          # os.makedirs(outputdir2)
import time        # start_time = time.time()
import shutil      # shutil.rmtree(output)

# beginning time
program_begin_time = time.time()
print('Current time: ', time.ctime())


# clobber output folder 
output = 'out_psf_test'
if os.path.exists(output):
    shutil.rmtree(output)
os.makedirs(output)


##=============================================================================
lst = [0,19]
for i in range(len(lst)):

    # narrowband number
    number = lst[i]
    
    # create output dir
    outputdir2 = output + '/narrowband'+ str(number)
    os.makedirs(outputdir2)

    # commands to run
    instance_catalog  = r'Research/psf_creation/instance_catalogs/' + \
                        'narrowband'+ str(number) + '.icat'
              
    background        = 'Research/psf_creation/backgrounds/background1.bkg'
    
    outputdir         = r'Research/psf_creation/' + outputdir2
    
    commands = r'cd ~/phosim;' + \
           r' ./phosim '   + instance_catalog + \
           r' -c '         + background + \
           r' -o '         + outputdir

    # input/output info
    print('{} {} {}'.format('outputdir2 = ',outputdir2, ''))       
    print('{} {} {}'.format('outputdir  = ',outputdir, ''))       
    print('{} {} {}'.format('instance_catalog = ',instance_catalog, ''))       
          

    # run the program
    subprocess.call(commands,shell=True)


##=============================================================================
# WARNING:
print('{} {} {}'.format('\n !!WARNING!! This program will clobber the folder :',output, ''))


    

# print the time taken
program_end_time = time.time()
seconds          = program_end_time - program_begin_time
m, s             = divmod(seconds, 60)
h, m             = divmod(m, 60)
d, h             = divmod(h, 24)
print('\nCurrent time: ', time.ctime())
print("\nTime taken to run whole program ==> {0:.0f} days, {1:.0f} hours, \
     {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

## NOTE: run program in the external terminal


