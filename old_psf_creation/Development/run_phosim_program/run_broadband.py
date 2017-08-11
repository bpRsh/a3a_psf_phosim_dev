#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jun 24, 2016
# Last update :

# Inputs      : instance_catalogs/broadband.icat
#               backgrounds/background1.bkg
# Outputs     : outputs/ 16 amplifier images zip files and 1 electron-image zip file

# Info:
# 1. This script run the phosim software command:
#       cd ~/phosim;
#       ./phosim instance_catalogs/broadband.icat
#       -c Research/psf_creation/backgrounds/background1.bkg
#       -o Research/psf_creation/outputs
#       
#       N.B. phosim is installed at ~/phosim
#            icat is instance_catalog file        
#            -c is physics_command file, background added later
#            -o is output_folder
#
#      To run phosim command we need an instance_catalog, background is optional.
#      All the paths are relative to phosim installation directory.
#
#
#  Estimated time: 30 minutes





# Imports
import subprocess
import os
import shutil
import time,datetime
import re
import sys

# time of run
start_time = time.time()
print('Current time: ', time.ctime())


# output dir
outputdir2         = r'outputs/broadband_out'
if os.path.exists(outputdir2):
    shutil.rmtree(outputdir2)
os.makedirs(outputdir2)

# commands to run
infile            = r'instance_catalogs/'    + r'broadband.icat'
instance_catalog  = 'Research/psf_creation/' + infile
background        = 'Research/psf_creation/' + r'backgrounds/background1.bkg'
outputdir         = 'Research/psf_creation/' + outputdir2
commands = r'cd ~/phosim;' + \
           r' ./phosim '   + instance_catalog + \
           r' -c '         + background + \
           r' -o '         + outputdir 



# run the commands
subprocess.call(commands,shell=True)

# read object info from instance_catalog
object = []
infile = infile
with open (infile,'r') as fin:
    for line in fin.readlines():
        if line.startswith('object'):
            object.append(line)
            
object   = str(object[0])
sed_line = re.findall(r'\S+', object)[-10]
sed      = sed_line.split("/")[-1]


# output info
print('{} {} {}'.format('input instance catalog = ',instance_catalog, ''))
print('{} {} {}'.format('input background =  ',background, ''))
print('{} {} {}'.format('\nobject_line = \n',object, ''))
print('{} {} {}'.format('sed_line     = ',sed_line, ''))
print('{} {} {}'.format('sed          = ',sed, ''))
print('{} {} {}'.format('\noutput folder = ',outputdir, ''))

# print the time taken
end_time = time.time()
seconds = end_time - start_time
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print('Current time: ', time.ctime())
print("Time taken to run this program ==> {0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

