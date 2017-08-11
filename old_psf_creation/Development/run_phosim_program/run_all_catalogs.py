#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jun 24, 2016
# Last update :

# Inputs      : instance_catalogs/*.icat  (1 broadband and 20 narrowband icats)
#               backgrounds/background1.bkg
# Outputs     : outputs/broadband_out/17_zip_files
#               outputs/narrowband*_out/17_zip_files

# Info:
# 1. This script run the phosim software command:
#       cd ~/phosim;
#       ./phosim instance_catalogs/required_instance_catalog.icat
#       -c Research/twenty_catalogs/backgrounds/background1.bkg
#       -o Research/twenty_catalogs/outputs
#       
#       N.B. phosim is installed at ~/phosim
#            icat is instance_catalog file        
#            -c is physics_command file, background added later
#            -o is output_folder
#
#      To run phosim command we need an instance_catalog, background is optional.
#      All the paths are relative to phosim installation directory.
 

# Imports
import subprocess
import os
import time,datetime
import shutil
import re

# beginning time
program_begin_time = time.time()
print('\nCurrent time: ', time.ctime())

# parent output folder 
output = 'outputs'
shutil.rmtree(output, ignore_errors=True)  
if not os.path.exists(output):
        os.makedirs(output) 




##=============================================================================
nfiles = 20
for i in range(nfiles):
    start_time = time.time()
    subprogram = 'narrowband{:d}'.format(i)
    print('{} {} {}'.format('\nrunning subprogram :',subprogram, ''))

    # commands to run
    instance_catalog  = r'Research/twenty_catalogs/instance_catalogs/' + \
                        'narrowband{:d}.icat'.format(i)
              
    background        = 'Research/twenty_catalogs/backgrounds/background1.bkg'
    
    outputdir         = r'Research/twenty_catalogs/outputs/' + \
                        'narrowband{:d}_out'.format(i)
    
    commands = r'cd ~/phosim;' + \
           r' ./phosim '   + instance_catalog + \
           r' -c '         + background + \
           r' -o '         + outputdir
              

              
    # output dir
    outputdir = output + r'/' + 'narrowband{:d}_out'.format(i)

    # remove output dir if exist and create again
    shutil.rmtree(outputdir, ignore_errors=True)  
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)           

    # run the program
    subprocess.call(commands,shell=True)

    # read object info from instance_catalog
    object = []
    infile = r'instance_catalogs/' + 'narrowband{:d}.icat'.format(i)
    with open (infile,'r') as fin:
        for line in fin.readlines():
            if line.startswith('object'):
                object.append(line)
            
    object   = str(object[0])
    sed_line = re.findall(r'\S+', object)[-10]
    sed      = sed_line.split("/")[-1]


    # output info
    print('{} {} {}'.format('output folder    = ',outputdir, ''))
    print('{} {} {}'.format('instance catalog = ',instance_catalog, ''))
    print('{} {} {}'.format('\nobject_line = \n',object, ''))
    print('{} {} {}'.format('sed_line     = ',sed_line, ''))
    print('{} {} {}'.format('sed          = ',sed, ''))


    # print elapsed time
    end_time = time.time()
    seconds  = end_time - start_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print('\nCurrent time: ', time.ctime())
    print("\nTime taken to run subprogram {}  ==> {:.0f} days, {:.0f} hours, {:.0f} minutes, {:f} seconds.".format(subprogram,d, h, m, s))
    print('*'*50)
    print('*'*50)




##=============================================================================
# run broadband
start_time_broadband = time.time()
outputdir            = r'outputs/broadband_out'
shutil.rmtree(outputdir, ignore_errors=True)  
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

instance_catalog  = r'Research/twenty_catalogs/instance_catalogs/broadband.icat'          
background        = r'Research/twenty_catalogs/backgrounds/background1.bkg'
outputdir         = r'Research/twenty_catalogs/outputs/broadband_out'

commands = r'cd ~/phosim;' + \
       r' ./phosim ' + instance_catalog + \
       r' -c '       + background + \
       r' -o '       + outputdir
       
subprocess.call(commands,shell=True)
##=============================================================================


# time taken by broadband
end_time_broadband = time.time()
seconds = end_time_broadband - start_time_broadband
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print("\nTime taken to run broadband program  ==> {0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))
print('*'*50)
print('*'*50)


##=============================================================================


    

# print the time taken
program_end_time = time.time()
seconds = program_end_time - program_begin_time
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print('\nCurrent time: ', time.ctime())
print("\nTime taken to run whole program ==> {0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

## NOTE: run program in the external terminal


