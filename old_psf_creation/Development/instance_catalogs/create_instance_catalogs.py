#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jun 26, 2016
# Last update : Jul 28, 2016

# Inputs      : none
# Outputs     : instance_catalogs/broadband.icat
#               instance_catalogs/barrowband*.icat

# Info:
# 1. This program creates 21 + 1 narrowband and broadband instance_catalogs.
#                These instance catalogs will be used by phosim software.
#                e.g. inside phosim directory:
#                phosim instance_catalog_path -c background_path -o output_path

## Input/output info:
## outfolder = 'instance_catalogs'
## outfile = outfolder + '/' + 'narrowband' + '{:d}.icat'.format(i)
## outfile = outfolder + '/' + 'broadband.icat'

# !!WARNING!! This program will clobber the folder : instance_catalogs


# Imports
import shutil
import os

data = """
Unrefracted_RA_deg 0
Unrefracted_Dec_deg 0
Unrefracted_Azimuth 0
Unrefracted_Altitude 89
Slalib_date 1994/7/19/0.298822999997
Opsim_rotskypos 0
Opsim_rottelpos 0
Opsim_moondec -90
Opsim_moonra 180
Opsim_expmjd 49552.3
Opsim_moonalt -90
Opsim_sunalt -90
Opsim_filter 2
Opsim_dist2moon 180.0
Opsim_moonphase 10.0
Opsim_obshistid 99999999
Opsim_rawseeing 0.65
SIM_SEED     1000
SIM_MINSOURCE 1
SIM_TELCONFIG 0
SIM_CAMCONFIG 1
SIM_VISTIME 15000.0
SIM_NSNAP 1
"""


# clobber outfolder
outfolder = 'instance_catalogs'
if os.path.exists(outfolder):
    shutil.rmtree(outfolder)
os.makedirs(outfolder)


# parameters
magnitude = '24 '

#=======================================================================
for i in range(21):
    outfile = outfolder + '/' + 'narrowband' + '{:d}.icat'.format(i)
    print('{} {} {}'.format('creating: ',outfile, ''))
    with open(outfile,'w') as fout:
        print('{} {} {}'.format('creating: ',outfile, ''))
        fout.write(data.lstrip())
        sed  = '../../Research/psf_creation/seds/' + 'narrowband' + '{:d}.sed'.format(i)
        line = r'object 0 0.0 0.0 '+ magnitude + sed + \
               r' 0 0 0 0 0 0 star none none' + '\n'

        fout.write(line)
#=======================================================================



# create catalog for broadband
outfile = outfolder + '/' + 'broadband.icat'
with open(outfile,'w') as fout:
    print('{} {} {}'.format('\ncreating: ',outfile, ''))
    
    fout.write(data.lstrip())
    sed  = '../../Research/psf_creation/seds/' + 'broadband.sed'
    line = r'object 0 0.0 0.0 ' + magnitude + sed + r' 0 0 0 0 0 0 star none none' + '\n'
    fout.write(line)
    
# WARNING:
print('{} {} {}'.format('\n !!WARNING!! This program will clobber the folder :',outfolder, ''))
