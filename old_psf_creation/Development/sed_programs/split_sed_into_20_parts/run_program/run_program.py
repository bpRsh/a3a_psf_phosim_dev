#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 26, 2016


# Imports
from __future__ import print_function
import subprocess


commands = '''
./a
echo "b"
echo "c"
echo "d"
'''

subprocess.call(commands, shell=True)
