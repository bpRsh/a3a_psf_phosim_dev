#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author     : Bhishan Poudel; Physics PhD Student, Ohio University
# Date       : Sep 07, 2016
# Last update:

# Inputs     : sed_flat.txt
# Outputs    : seds/narrowband*.sed

# Info:
# 1. This program takes in  input_sed_file (sed_flat.txt)
#    and creates twenty-one   output_sed files.
#
# 2. The input sed file has two columns:
#        wavelength (nm) and flux (ergs/cm^2/s/nm)
#        wavelength varies from 300 nm to 1200 nm.
#
# 3. To create output_seds from this input_sed_file, we first decrease the
#    flux at 500 nm wavelength by a factor of 100 so that when phosim software
#    uses this flux to normalize all the values, it will have lesser impact.
#    i.e. sed_flat.txt    : 500.000  3.97290e-12
#         narrowband*.sed : 500.000  3.9728999999999995e-14
#
# 4. Now, from the LSST_RED_BAND_FILTER_FILE we looked for the values of wavelength
#    where transmission is NOT <= 5%.
#        We found that the wavelength range to be 531-696 nm.
#
# 5. So, we will take the wavelength range only between this range and set all
#    the other wavelength fluxes to zero EXCEPT for 500 nm case.
#
#
#
# sed_info:
# source_input_sed_file: phosim/data/SEDs/flatSED/sed_flat.txt
# column0              : wavelength (300-1200 nm)
# column1              : flux (ergs/cm^2/s/nm)
# e.g.                 : phosim/data/SEDs/kurucz/km01_7000.fits_g40_7120

# filter_info:
# source_red_band_filter_lsst : phosim/data/lsst/filter_2.txt
# We take wavelength range such that transmission <= 5%,
# and we get 531 nm - 696 nm.
#
#
# Estimated time:  sec


# Imports
import numpy as np
import os
import shutil
import time




##==============================================================================
## replace_outfolder
##==============================================================================
def replace_outfolder(outfolder):
    '''
Depends: outfolder

Returns: outfolder
    '''

    #outfolder = 'seds'
    if os.path.exists(outfolder):
        print('Replacing folder: ', outfolder,'\n')
        shutil.rmtree(outfolder)
    os.makedirs(outfolder)






##==============================================================================
## read_data
##==============================================================================
def read_data(infile):
    '''
Depends: infile e.g. infile = 'sed_flat.txt'

Returns: data
    '''
    #infile = 'sed_flat.txt'
    # read input sed file
    # if we change infile, we may need to change varialbe "lookup"
    # also, change normalize variable
    with open(infile, 'r') as f:
        data = f.readlines()
    return data




##==============================================================================
## get_number_of_comments_line
##==============================================================================
def get_number_of_comments_line(comments_lines,data):
    '''
Depends: data (obtained from function read_data)

Returns: comments_lines
    '''

    comments_lines = 0
    for line in data:
        if line.strip().startswith('#'):
            comments_lines += 1
        else:
            break

    # print final value of comments_line
    print('{} {} {}'.format('comment_lines = ',comments_lines, '\n'))

    return comments_lines








##==============================================================================
## get_normalize_line_and_num
##==============================================================================
def get_normalize_line_and_num(lookup,infile):

    #lookup = '500.000'
    #infile = 'sed_flat.txt'
    normalize_line = ''
    normalize_line_num = 0
    with open(infile) as f:
        for num, line in enumerate(f, 1):
            if lookup in line:
                normalize_line = line
                normalize_line_num = num - 1
                print ('normalize line = ', line)
                print ('normalize line num = ', num)

    return normalize_line, normalize_line_num









##==============================================================================
## rescale_normalize_line
##==============================================================================
def rescale_normalize_line(normalize_line):

    # decrease the flux of normalize line by a factor of 100
    wave,flux = normalize_line.split()
    flux = float(flux) / 100.0  # for flat_sed.txt
    #flux = float(flux) / 1.0     # for kurucz star
    normalize_line = str(wave) + '  ' + str(flux) + '\n'

    # prints
    #print('{} {} {}'.format('wave = ',wave, ''))
    #print('{} {} {}'.format('flux = ',flux, ''))
    #print('{} {} {}'.format('normalize_line = ',normalize_line, ''))

    return normalize_line




##==============================================================================
## r_band_breakpoints
##==============================================================================
def r_band_breakpoints(lambda_start,lambda_end,nbreaks):
    '''
# from red band filter of lsst : phosim/data/lsst/filter_2.txt
# we take wavelength range such that transmission <= 5%,
# and we get 531 nm - 696 nm wavelength range

    '''
    #lambda_start = 531.0
    #lambda_end = 696.0
    #nbreaks = 21.0

    # step between sed0 and sed1
    step = (lambda_end-lambda_start) / float(nbreaks) # 7.9 nm


    # sed file has decimal precision 1, so round off step to one precision
    step = float(str(round(step, 1)))
    breakpoints = np.arange(lambda_start,lambda_end,step)
    breakpoints = np.append(breakpoints, lambda_end)

    # prints
    #print('{} {} {}'.format('\nlambda_start = ',lambda_start, 'nm'))
    #print('{} {} {}'.format('lambda_end = ',lambda_end, 'nm'))
    #print('{} {} {}'.format('lambda range = ',lambda_end - lambda_start, 'nm'))
    #print('{} {} {}'.format('step = ',step, ' nm\n'))
    #print('{} {}{}'.format('breakpoints = \n', breakpoints,'' ))
    #print('{} {}{}'.format('\nlen breakpoints = ', len(breakpoints),'' ))

    return breakpoints







##==============================================================================
## get_indices_of_breakpoints
##==============================================================================
def get_indices_of_breakpoints(infile,breakpoints):
    infile = infile
    idx = 0
    line_num = []
    tmpidx = 0
    with open(infile,'r') as fi:
        data = fi.readlines()
        for line in data:
            idx += 1
            for value in list(breakpoints):
                if (str(round(value,1))) in line:
                    tmpidx = idx
                    line_num.append(tmpidx)

    # prints
    #print('{} {} {}'.format('\nlin_num = \n',line_num, ''))
    #print('{} {} {}'.format('\nlen lin_num = \n',len(line_num), '\n'))


    ## debugging line numbers
    #print('{} {}{}'.format('data[0]   = \n', data[0],'' ))
    #print('{} {}{}'.format('len data  = ', len(data),'' ))
    #print('{} {}{}'.format('last data = ', data[(len(data)-1)],'' ))


    #print('{} {}{}'.format('breakpoints[0] = ', breakpoints[0],'' ))
    #print('{} {}{}'.format('line_num[0]     = ', line_num[0],'\n' ))

    #print('{} {}{}'.format('breakpoints[1] = ', breakpoints[1],'' ))
    #print('{} {}{}'.format('line_num[1]     = ', line_num[1],'\n' ))

    #print('{} {}{}'.format('breakpoints[19] = ', breakpoints[19],'' ))
    #print('{} {}{}'.format('line_num[19]     = ', line_num[19],'\n' ))

    #print('{} {}{}'.format('breakpoints[20] = ', breakpoints[20],'' ))
    #print('{} {}{}'.format('line_num[20]     = ', line_num[20],'\n' ))

    #print('{} {}{}'.format('breakpoints[21] = ', breakpoints[21],'' ))
    #print('{} {}{}'.format('line_num[21]     = ', line_num[21],'\n' ))

    return line_num








##==============================================================================
## create_narrow_sed_from_sed
##==============================================================================


def create_narrow_sed_from_sed(outfile,data,comments_lines,line_num,normalize_line,normalize_line_num,lower,upper):

    # create narrow sed file from given sed file
    print('{} {} {}'.format('writing to the file ',outfile, '...'))
    with open (outfile, 'a') as f:

        # write comments
        f.write( ''.join (  data[:comments_lines] ))

        # change column two to zeros
        for line in data:
           if not line.startswith('#'):
            row=line.split()
            tmp = str(row[0]) + '  ' + '0.0\n'
            f.write(''.join(tmp))

        for j in range(lower,upper ,1):
            replace_line(outfile, j-1, data[j-1] )

        # replace 500 nm line (scale down by 100)
        #replace_line(outfile, normalize_line_num, normalize_line + '\n')
        replace_line(outfile, normalize_line_num, normalize_line)










##==============================================================================
## replace_line
##==============================================================================
def replace_line(infile, line_num, text):
    ''' This function replaces a given line number
        Usage: replace_line(infile, line_num, text)
    '''

    lines = open(infile, 'r').readlines()
    lines[line_num] = text
    lines[line_num] = lines[line_num].lstrip() # lstrip removes leading spaces
    out = open(infile, 'w')
    out.writelines(lines)
    out.close()






##==============================================================================
## Main Function
##==============================================================================
def main():

    # read data
    infile = 'sed_flat.txt'
    data = read_data(infile)

    # comments lines
    comments_lines = 0
    comments_lines = get_number_of_comments_line(comments_lines,data)


    # get normalize line of 500 nm
    lookup = '500.000'
    normalize_line, normalize_line_num = get_normalize_line_and_num(lookup,infile)


    # decrease the flux of normalize line by a factor of 100
    normalize_line = rescale_normalize_line(normalize_line)


    # get breakpoints
    breakpoints = r_band_breakpoints(lambda_start=531.0,lambda_end=696.0,nbreaks=21.0)




    # get indices of these breakpoints from input file
    line_num = get_indices_of_breakpoints(infile,breakpoints)


    # replace outfolder
    outfolder = 'seds'
    replace_outfolder(outfolder)

    # create sed file for narrowband0 to 19
    for i in range(21):
        outfile = outfolder + '/' + 'narrowband{:d}.sed'.format(i)
        lower = line_num[i]
        upper = line_num[i+1]

        # create seds for narrownbands
        create_narrow_sed_from_sed(outfile,data,comments_lines,line_num,normalize_line,normalize_line_num,lower,upper)

        # for last narrowband20
        if i==20:
            outfile = outfolder + '/' + 'narrowband{:d}.sed'.format(i)
            lower = line_num[i]
            upper = line_num[i+1] + 1

            # create seds for narrownbands
            create_narrow_sed_from_sed(outfile,data,comments_lines,line_num,normalize_line,normalize_line_num,lower,upper)



    # output info
    print('{} {} {}'.format('\ninput sed            : ',infile, ''))
    print('{} {} {}'.format('output folder        : ',outfolder, ''))





##==============================================================================
## Main Program
##==============================================================================


if __name__ == '__main__':

    # beginning time
    program_begin_time = time.time()
    begin_ctime        = time.ctime()

    # main program
    main()


    # print the time taken
    program_end_time = time.time()
    end_ctime        = time.ctime()
    seconds          = program_end_time - program_begin_time
    m, s             = divmod(seconds, 60)
    h, m             = divmod(m, 60)
    d, h             = divmod(h, 24)
    print('\nBegin time: ', begin_ctime)
    print('End   time: ', end_ctime,'\n')
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))
