#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 11, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. This program finds the average flux of all the f606 and f814
#    fitsfiles inside "color" folder. 
#
#
#
# Imports
from astropy.io import fits
from astropy.io.fits import getheader
from astropy.io.fits import getval
from astropy.io.fits import getdata

sum_flux1 = 0.0
sum_flux2 = 0.0
for i in range(100):
    infile1 = 'colors/f606w_gal'+str(i)+'.fits'
    infile2 = 'colors/f814w_gal'+str(i)+'.fits'
    
    flux1 = getval(infile1, 'FLUX')
    flux2 = getval(infile2, 'FLUX')
    
    sum_flux1 += flux1
    sum_flux2 += flux2
    
 
 
# print info
avg_flux_606 = sum_flux1/100.0    
avg_flux_814 = sum_flux2/100.0 
   
print('{} {:.3f} {}'.format('avg_flux_606 = ',avg_flux_606, '')) # 62.395
print('{} {:.3f} {}'.format('avg_flux_814 = ',avg_flux_814, '')) # 72.279


