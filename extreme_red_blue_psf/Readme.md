#### Extreme PSF   Analysis (Most Blue and Most Red PSF)

#### Author    : Bhishan Poudel
#### Date      : Aug 25, 2016



# 1. Create Background for Phosim.      

Program   : aa_create_background.py  
   
Depends   : none  
  
Output    : backgrounds/background1.bkg       
            
This program creates a background file for Phosim. In this background  
file we choose pixelsize 1.5 and saturation,blooming,chargesharing to be zero.    

    
It will clobber the output folder backgrounds.  






# 2. Create Seds for Phosim    

Program   : aa_create_sed_all.py  
   
Depends   : sed_flat.txt  
  
Output    : seds/narrowband*.sed        
            
This program creates seds for all narrowbands.    
We break the wavelength range 531-696 nm into 21 parts and decrease the    
normalizing wavelength at 500 nm by a factor of 100.  
    
It will clobber the output folder seds.




# 3. Create Instance Catalogs for Phosim  

Program   : a1_create_instance_catalogs_0_20_seed.py    
Depends   : none    
Output    :

+ instance_catalogs/narrowband0.icat  
  instance_catalogs/narrowband20.icat   
            
This program creates instance catalogs for narrowband0 and narrowband20.    
It will clobber the output folder each time this program runs.  






# 4. Create zipped psf files using Phosim  

Program   : a2_phosim_narrow0_and_20.py  

Depends   :

+ instance_catalogs/narrowband0.icat  
            instance_catalogs/narrowband20.icat  
            seds/narrowband0.sed  
            seds/narrowband20.sed  
            backgrounds/background1.bkg  
               
Outputs   :

+ phosim_output_extreme_psf/narrowband0/17_zipped_psf_fitsfiles
  phosim_output_extreme_psf/narrowband20/17_zipped_psf_fitsfiles  
               
               

This program creates zipped psffiles for narrowband0 and narrowband20.  
It will clobber the output folder each time this program runs.  





# 5. Unzip psffiles created from Phosim  

Program   : a3_unzip_psf_0_20.py  
 
Depends   : phosim_output_extreme_psf/narrowband0_out/zipped_psf  

Outputs   : extreme_psf/psf0.fits_and_20  

This program unzips zipped psffiles created from Phosim into *extreme_psf* folder.





# 6. Get imcat parameters e and rh for psf0 and psf20

Program   : a4_imcat_e_rh_psf0_20.py  

Inputs    : extreme_psf/psf0.fits_and_psf20.fits   

Outputs   : gives 6 values of e and rh ( i.e. e00 e10 rh0 e01 e11 rh1 )


This program returns imcat variables e and rh for given input psf.








# 7. Create imcat variables datafile for different seed

Program   : extreme_psf_phosim_imcat.py 

Depends    :

+ a1_create_instance_catalogs_0_20_seed.py  
                 argument: the SIM_SEED to run this program  

+ a2_phosim_narrow0_and_20.py    # gives zipped psfs  
    ./instance_catalogs  
    ./seds  
    ./backgrounds  

+ a3_unzip_psf_0_20.py
    phosim_output_extreme_psf/narrowband_0_and_20/zipped_psf  

+ a4_imcat_e_rh_psf0_20.py   
    returns e00 e10 rh0 e01 e11 rh1
           
Outputs     : extreme_psf_phosim_imcat_seed_e_rh.dat 

This program runs the above FOUR programs and creates 
imcat variables datafile for different seed.






# 8. Create psf using Phosim for outlier imcat values

Program   : outlier_psf_phosim.py 

Depends   :

+ a1_create_instance_catalogs_0_20_seed.py  
    argument: the SIM_SEED to run this program
                            
+ a2_phosim_narrow0_and_20.py    # gives zipped psfs
    ./instance_catalogs  
    ./seds  
    ./backgrounds  

+ a3_unzip_psf_0_20.py
    phosim_output_extreme_psf/narrowband_0_and_20/zipped_psf  

Outputs     : outlier_psf/extreme_psf_seed/psf0_20.fits

This program runs above programs a1,a2,a3 and it copies final output folder of
_a3_unzip_psf_0_20.py_  (i.e, extreme_psf) into the folder **outlier_psf** with
different seed number.
  
