#!/bin/sh
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 19, 2016

file="c.txt"
line3="# column 2 is the wavelength (nm)"
line6="# column 5 is the flux (ergs/cm^s/s/nm)"
line7="# angle wave    trans   refl    flux"
sed -i '3d' $file
sed -i "3i $line3" $file
sed -i "6i $line6" $file
sed -i "7i $line7" $file
