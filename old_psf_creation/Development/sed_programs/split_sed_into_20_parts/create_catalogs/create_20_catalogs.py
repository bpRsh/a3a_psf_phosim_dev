#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 26, 2016


# Imports
from __future__ import print_function
import os


# create output dir
dirname = 'catalogs'
if not os.path.exists(dirname):
    os.makedirs(dirname)

line1 = 'Opsim_filter 2\n'
line2 = 'SIM_SEED     1000\n'



#==============================================================================
for i in range(20):
    outfile = dirname + '/' + 'catalog' + '{:d}.icat'.format(i)
    with open(outfile,'w') as fout:
        fout.write(line1)
        fout.write(line2)

        sed  = '../../Research/twenty_catalogs/seds/' + 'catalog' + '{:d}.sed'.format(i)

        line = r'object 0 0.0 0.0 15 ' + sed + r' 0 0 0 0 0 0 star none none'
                               
        fout.write(line)
	        
#==============================================================================



