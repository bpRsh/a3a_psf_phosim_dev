#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 29, 2016
 

# Imports
import numpy as np


# data
lambda_end = 696.0
lambda_start = 531.0


# step between sed0 and sed1
step = (lambda_end-lambda_start) / 20.0


# sed file has decimal precision 1 so round off step to one precision
step = float(str(round(step, 1)))
print('{} {} {}'.format('lambda_start = ',lambda_start, 'nm'))
print('{} {} {}'.format('lambda_end = ',lambda_end, 'nm'))
print('{} {} {}'.format('step = ',step, ' nm\n'))

waverangeBorders = np.arange(lambda_start,lambda_end,step)
for i in range(len(waverangeBorders)):
    waverangeBorders[i] = float(str(round(waverangeBorders[i], 1)))
    print('{} {} {}{}'.format('waverangeBorder',i, ' = ', waverangeBorders[i]))



# add last wavelength lambda_end to the numpy ndarray
print('{} {} {}'.format('\ntype waverangeBorders = ',type(waverangeBorders), ''))
waverangeBorders = np.append(waverangeBorders, [lambda_end])

for i in range(len(waverangeBorders)):
    print('{} {} {}{}'.format('waverangeBorder',i, ' = ', waverangeBorders[i]))


print(waverangeBorders)
