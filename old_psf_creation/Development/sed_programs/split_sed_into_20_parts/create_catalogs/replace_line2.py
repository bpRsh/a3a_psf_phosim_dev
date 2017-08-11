#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 26, 2016


# Imports
from __future__ import print_function

#==============================================================================
infile = 'input'
outfile = 'output'
with open(infile) as fin, open(outfile,'w') as fout:
    for line in fin:
	if line.startswith('#'):
	    line = 'replaced line' + '\n'
            fout.write(line)
	else:
	    fout.write(line)
#==============================================================================


