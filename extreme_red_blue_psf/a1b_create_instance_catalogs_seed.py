#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 25, 2016
# Last update : Sep 07, 2016


# Imports
import shutil
import os
import sys


def replace_outfolder(outfolder):
    if os.path.exists(outfolder):
        print('Replacing folder: ', outfolder)
        shutil.rmtree(outfolder)
    os.makedirs(outfolder)

def create_catalogs(seed):

    '''
# Inputs      : 1. argument: a number for SIM_SEED
#
# Outputs     : instance_catalogs/narrowband*.icat
#
# Info:
# 1. This program creates instance catalogs with different SIM_SEED variables.
#
#
    '''

    sim_seed = str(seed)

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
SIM_SEED     """ + sim_seed +\
"""
SIM_MINSOURCE 1
SIM_TELCONFIG 0
SIM_CAMCONFIG 1
SIM_VISTIME 15000.0
SIM_NSNAP 1
"""


    # function begin
    print("Beginning: create instance catalogs\n")


    # clobber outfolder
    outfolder = 'instance_catalogs'
    replace_outfolder(outfolder)


    for i in range(21):
        outfile = outfolder + '/' + 'narrowband' + '{:d}.icat'.format(i)
        print('{} {} {}'.format('creating: ',outfile, ''))
        with open(outfile,'w') as fout:
            print('{} {} {}'.format('creating: ',outfile, ''))
            fout.write(data.lstrip())
            sed  = '../../../Research/extreme_red_blue_psf/seds/' + 'narrowband' + '{:d}.sed'.format(i)
            line = 'object 0 0.0 0.0 24 ' + sed + \
                   ' 0 0 0 0 0 0 star none none' + '\n'

            fout.write(line)


    # end function
    print("Ending: create instance catalogs\n")

if __name__ == '__main__':
    create_catalogs(1000)
    pass


