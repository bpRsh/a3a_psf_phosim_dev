#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date      : Jun 24, 2016
 

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

# delete output folder if exist and create again
output = 'outputs'
shutil.rmtree(output,ignore_errors=True)
if not os.path.exists(output):
    os.makedirs(output)


# commands to run
infile            = r'instance_catalogs/'       + r'broadband.icat'
instance_catalog  = 'Research/twenty_catalogs/' + infile
background        = 'Research/twenty_catalogs/' + r'backgrounds/background1.bkg'
outputdir         = 'Research/twenty_catalogs/' + output
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

