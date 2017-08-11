#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : May 31, 2017

# Imports
import time
import numpy as np


# LSST r band wavelength ranges:
# Reference: https://www.lsst.org/sites/default/files/docs/sciencebook/SB_2.pdf
# 5520 is the blue side wavelength of LSST r band filter
# 6910 is the red  side wavelength of LSST r band filter
# z_g = redshift of original galaxy e.g. 1.5 from config.sh
# lambda are integers with unit Angstrom.
#
# lambda_1 = 5520 / (1 + z_g) = 2208                           
# lambda_2 = 6910 / (1 + z_g) = 2764

z_g = 1.5
lambda_1 = int(5520 / (1 + z_g))                          
lambda_2 = int(6910 / (1 + z_g))
nr = np.linspace(2208,2764,num=21,endpoint=True)
nr = [int(i) for i in nr]
print(nr)


# HST wavelength range:
# Reference:
# From http://www.stsci.edu/hst/acs/documents/handbooks/current/c05_imaging2.html
# Camera: HST WFC camera
# Filter  Central          Width  Description  Camera 
# name    wavelength (Å)   (Å)
# F814W   8333             2511   Broad I      WFC/HRC
#
# This gives lambda_hst values:
# For now we choose z_cutout = 0.2
# lambda_hst1  = ( 8333 - (2511/2) ) / (1 + z_cutout) = 7077.5 / 1.2 = 5897.9 
# lambda_hst2  = ( 8333 + (2511/2) ) / (1 + z_cutout) = 9588.5 / 1.2 = 7990.4 

z_cutout = 0.2
lambda_hst1  = int(( 8333 - (2511/2) ) / (1 + z_cutout))
lambda_hst2  = int(( 8333 + (2511/2) ) / (1 + z_cutout))
a = np.linspace(lambda_hst1,lambda_hst2,num=21,endpoint=True)
a = [int(i) for i in a]
print(a)
print('lambda_hst1 = ', lambda_hst1)
print('lambda_hst2 = ', lambda_hst2)
print('lambda1 = ', lambda_1)
print('lambda2 = ', lambda_2)

print("\n")
nr = np.linspace(2208,2764,num=21,endpoint=True)
dr_b =  0.59163692358
dr_d =  1.09284263486

m  = [ num/dr_b for num in nr]
m1 = [ num/dr_d for num in nr]
print(m)
print(m1)

# RESULT
#[2208, 2235, 2263, 2291, 2319, 2347, 2374, 2402, 2430, 2458, 2486, 2513, 2541, 2569, 2597, 2625, 2652, 2680, 2708, 2736, 2764]
#[5897, 6001, 6106, 6210, 6315, 6420, 6524, 6629, 6734, 6838, 6943, 7048, 7152, 7257, 7362, 7466, 7571, 7676, 7780, 7885, 7990]
#lambda_hst1 =  5897
#lambda_hst2 =  7990
#lambda1 =  2208
#lambda2 =  2764
