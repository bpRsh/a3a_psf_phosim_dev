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

##==============================================================================
#infile = 'catalog.icat'
#outfile = dirname + '/' + 'output1.icat'
#with open(infile) as fin, open(outfile,'w') as fout:
    #for line in fin:
	#if line.startswith('object'):
	    #sed = r'catalog1.sed'
	    #line = r'object 0 0.0 0.0 15 ' + sed + \
		   #r' 0 0 0 0 0 0 star none none' + '\n'
	    #fout.write(line)
	#else:
	    #fout.write(line)
##==============================================================================



#==============================================================================
for i in range(1,21,1):
    infile = 'catalog.icat'
    outfile = dirname + '/' + 'catalog' + '{:d}.icat'.format(i)
    with open(infile) as fin, open(outfile,'w') as fout:
        for line in fin:
	    if line.startswith('object'):
	        sed = '../../research/catalogs/' + 'catalog' + '{:d}.sed'.format(i)
	        line = r'object 0 0.0 0.0 15 ' + sed + \
		   r' 0 0 0 0 0 0 star none none' + '\n'
	        fout.write(line)
	    else:
	        fout.write(line)
#==============================================================================



