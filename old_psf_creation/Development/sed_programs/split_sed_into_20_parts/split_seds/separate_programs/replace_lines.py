#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 26, 2016


# Imports
from __future__ import print_function


infile = 'catalog.icat'
with open(infile) as fin, open('output','w') as fout:
    line = fin.readlines()
    print(line)
