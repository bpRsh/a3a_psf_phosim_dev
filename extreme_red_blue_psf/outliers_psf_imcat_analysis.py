#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Douglas Clowe; Associate Professor, Ohio University
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
#
# Date        : Aug 22, 2016
# Last update : Sep 08, 2016
#


# Imports
from __future__ import print_function
import os
import sys
import subprocess
import time



def outlier_imcat_catalog_seed(seed,outfile):
    '''
# Depends     : seed
#               outlier_psf/extreme_psf_seed/psf*.fits
#
#               infits = ' ' + 'outlier_psf/extreme_psf_' + str(seed) + '/psf'+ str(fnum)+ '.fits' 
#
# Outputs     : outfile # e.g. 'narrowbands_seed.cat'
#
#               outfile = 'outlier_psf/extreme_psf_' + str(seed) + '/narrowbands_' + str(seed) + '.cat'
#
# Info:
# 1. This function takes in a seed number to get the input fitsfiles to be used
#    in the program. For example if we have 21 psf files inside
#    outlier_psf/extreme_psf_103105035/psf*.fits  (21 psf files)
#    then the seed number is 103105035.
#
# 2. The folder outlier_psf/extreme_psf_seed is created by outliers_psf_phosim.py
#  
#
# 3. psrat is the pixscale ratio
#    from jesisim_config_file:
#    pix_scale=0.03  		# pixel scale to use (arseconds per pixel)
#    final_pix_scale=0.2    # LSST pixscale (arcsecords per pixel)
#
#    psrat = 0.03 / 0.2 = 1.15
#
# Estimated time : 2 minute 3 seconds for 21 psf 
    '''
    


    ##==============================================================================
    ## for psf0 
    ##==============================================================================
    fnum = str(0)
    psrat = ' ' +  str(0.15)   # ratio of pixscales 0.03/0.2 = 0.15
    infits = ' ' + 'outlier_psf/extreme_psf_' + str(seed) + '/psf'+ str(fnum)+ '.fits'
    #               outlier_psf/extreme_psf_103105035/psf0.fits    
    
    
    ## do imcat analysis
    commands = " " +\
    "ic -s 100 '%1 grand .001 * +'" + infits + " > temp.fits"  + " ;" +\
    "hfindpeaks temp.fits -r 5 50 | "                      + \
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
    "lc +all 'n = " + fnum + "'>  "  + outfile             + \
    " ; " +\
    "rm temp.fits"
    
    
    # call the commands
    print('\n\nCreating imcat catalog for seed ' + str(seed) + ' and loop ' + str(fnum) + '\n')    
    subprocess.call(commands,shell=True)

    
    # get value of rg
    string = "lc -o 'rg' < " + outfile
    rg = float(subprocess.check_output(string ,shell=True))
    string2 = "lc -b +all 'rg = " + str(rg) + "' | "
    print('{} {} {}'.format('\n\nrg = ',rg, ''))
    print('{} {} {}'.format('string = ',string, ''))
    print('{} {} {}'.format('string2 = ',string2, ''))
    
    for i in range(1,21):
        
        fnum = str(i)
        infits = ' ' + 'outlier_psf/extreme_psf_' + str(seed) + '/psf'+ str(fnum)+ '.fits'

        
        
        ## do imcat analysis
        commands = " " +\
        "ic -s 100 '%1 grand .001 * +'" + infits + " > temp.fits"  + " ;" +\
        "hfindpeaks temp.fits -r 5 50 | "                      +\
        "getsky -Z rg 3 | "                                    +\
        "apphot -z 30 | "                                      +\
        "lc -b -i '%flux 0 >' | "                              +\
        "cleancat 100000 | " + string2                         +\
        "getshapes -s" + psrat + ' ' + "| "                    +\
        "lc -b +all 'x = %x %d vadd' | "                       +\
        "apphot -z 30 | "                                      +\
        "getshapes -s " + ' ' + psrat + "| "                   +\
        "lc -b +all 'x = %x %d vadd' | "                       +\
        "apphot -z 30 | "                                      +\
        "getshapes -s " + psrat + "| "                         +\
        "lc -b +all 'x = %x %d vadd' | "                       +\
        "apphot -z 30 | "                                      +\
        "getshapes -s" + psrat + "| "                          +\
        "lc +all 'n = " + fnum + "'>  "  + 'temp.cat'          +\
        " ; "                                                  +\
        "rm temp.fits ; "                                      +\
        "catcats " + outfile + " temp.cat > temp2.cat ; "      +\
        "mv temp2.cat " + outfile
        
        # print commands
        #print(commands)

        
        # call the commands
        print('\n\nCreating imcat catalog for seed ' + str(seed) + ' and loop ' + str(fnum) + '\n')
        subprocess.call(commands,shell=True)    
        
    

      
if __name__ == '__main__':

    #seed = 103105035
    #sim_seed_lst=[103105035,104141804,105111823,102221250,102230033,104184839,104211258]
    sim_seed_lst=[104141804,105111823,102221250,102230033,104184839,104211258]

    for i in range(len(sim_seed_lst)):
        
        seed = sim_seed_lst[i]
        outfile = 'outlier_psf/extreme_psf_' + str(seed) + '/narrowbands_' + str(seed) + '.cat'

        # run main program
        outlier_imcat_catalog_seed(seed,outfile)

    

    

