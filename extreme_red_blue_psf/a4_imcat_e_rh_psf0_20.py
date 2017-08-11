#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Douglas Clowe; Associate Professor, Ohio University
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
#
# Date        : Aug 22, 2016
# Last update : Sep 02, 2016 # changed hfindpeaks
#


# Imports
from __future__ import print_function
import os
import sys
import subprocess
import time



def imcat_parameters_e_rh():
    '''
# Inputs      : extreme_psf/psf0.fits_and_psf20.fits
#
# Outputs     : imcat variables
#
# Info:
# 1. This program takes in an input fitsfile and creates a parameter file
#    for that fitsfile.
#  
#
# 2. psrat is the pixscale ratio
#    from jesisim_config_file:
#    pix_scale=0.03  		# pixel scale to use (arseconds per pixel)
#    final_pix_scale=0.2    # LSST pixscale (arcsecords per pixel)
#
#    psrat = 0.03 / 0.2 = 1.15
#
# Estimated time : 23 seconds  
    '''
    


    ##==============================================================================
    ## for psf0 find imcat variables e00 e10 rh0
    ##==============================================================================
    sfile = ' psf0'
    psrat = ' ' +  str(0.15)   # ratio of pixscales 0.03/0.2 = 0.15
    ffile = ' extreme_psf/psf0.fits'
    
    
    ## do imcat analysis
    commands = " " +\
    "ic -s 100 '%1 grand .001 * +'" + ffile + " > temp.fits"  + " ;" +\
    "hfindpeaks temp.fits -r 5 50 | "                    + \
    "getsky -Z rg 3 | "                                    + \
    "apphot -z 30 | "                                      + \
    "lc -b -i '%flux 0 >' | "                              + \
    "cleancat 100000 | "                                   + \
    "getshapes -s" + psrat + ' ' + "| "                    + \
    "lc -b +all 'x = %x %d vadd' | "                       + \
    "apphot -z 30 | "                                      + \
    "getshapes -s " + ' ' + psrat + "| "                   + \
    "lc -b +all 'x = %x %d vadd' | "                       + \
    "apphot -z 30 | "                                      + \
    "getshapes -s " + psrat + "| "                         + \
    "lc -b +all 'x = %x %d vadd' | "                       + \
    "apphot -z 30 | "                                      + \
    "getshapes -s" + psrat + "| "                          + \
    "lc > temp.cat  "                                      + \
    " ; " +\
    "rm temp.fits"
    
    
    # call the commands
    print('Commands to run psf0 and get imcat variables e00 e10 rh0 \n')
    print(*commands.split('|'), sep='\n')
    print("\n\n")
    subprocess.call(commands,shell=True)
    
    
    e00 = float(subprocess.check_output("lc -o 'e = %e[0]' < temp.cat",shell=True))
    e10 = float(subprocess.check_output("lc -o 'e = %e[1]' < temp.cat",shell=True))
    rh0 = float(subprocess.check_output("lc -o 'rh' < temp.cat",       shell=True))
    
    print('\n{} {} {}'.format('e00 = ',float(e00), ''))
    print('{} {} {}'.format('e10 = ',float(e10), ''))
    print('{} {} {}'.format('rh0 = ',float(rh0), ''))
    
    print('{} {} {}'.format('\n Paramters e00 e10 rh0 for psf0 are found!','', ''))
    
    
    
    
    
    
    
    
    
    
    ##==============================================================================
    ## for psf20 find imcat variables e01 e11 rh1
    ##==============================================================================
    sfile = ' psf20'
    psrat = ' ' +  str(0.15)   # ratio of pixscales 0.03/0.2 = 0.15
    ffile = ' extreme_psf/psf20.fits'
    
    
    ## do imcat analysis
    commands = " " +\
    "ic -s 100 '%1 grand .001 * +'" + ffile + " > temp.fits"  + " ;" +\
    "hfindpeaks temp.fits -r 5 50 | "                    + \
    "getsky -Z rg 3 | "                                    + \
    "apphot -z 30 | "                                      + \
    "lc -b -i '%flux 0 >' | "                              + \
    "cleancat 100000 | "                                   + \
    "getshapes -s" + psrat + ' ' + "| "                    + \
    "lc -b +all 'x = %x %d vadd' | "                       + \
    "apphot -z 30 | "                                      + \
    "getshapes -s " + ' ' + psrat + "| "                   + \
    "lc -b +all 'x = %x %d vadd' | "                       + \
    "apphot -z 30 | "                                      + \
    "getshapes -s " + psrat + "| "                         + \
    "lc -b +all 'x = %x %d vadd' | "                       + \
    "apphot -z 30 | "                                      + \
    "getshapes -s" + psrat + "| "                          + \
    "lc > temp.cat  "                                    + \
    " ; " +\
    "rm temp.fits"
    
    
    # call the commands
    print('Commands to run psf20 and get imcat variables e01 e11 rh1 \n')
    print(*commands.split('|'), sep='\n')
    print("\n\n")
    subprocess.call(commands,shell=True)
    
    
    
    # variables
    e01 = float(subprocess.check_output("lc -o 'e = %e[0]' < temp.cat",shell=True))
    e11 = float(subprocess.check_output("lc -o 'e = %e[1]' < temp.cat",shell=True))
    rh1 = float(subprocess.check_output("lc -o 'rh' < temp.cat",       shell=True))
    
    
    print('{} {} {}'.format('e01 = ',float(e01), ''))
    print('{} {} {}'.format('e11 = ',float(e11), ''))
    print('{} {} {}'.format('rh1 = ',float(rh1), ''))
    
    print('{} {} {}'.format('Paramters e01 e11 rh1 for psf20 are found!\n','', ''))
    
    
    e_rh = [e00,e10,rh0,e01,e11,rh1]
    return e_rh

      
if __name__ == '__main__':
    #imcat_parameters_e_rh()
    pass

