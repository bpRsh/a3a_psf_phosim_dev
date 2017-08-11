#### Imcat Analysis of All Outliers and All PSFs of those outliers


#### Author    : Bhishan Poudel
#### Date      : Sep 08, 2016





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







# 3. Create Instance Catalogs for Phosim with given seed. 

Program   : a1b_create_instance_catalogs_seed.py    
   
Depends   : seed  
    
Output    : instance_catalogs/narrowband*.icat        
            
This program creates instance catalogs for all narrowbands.      
It will clobber the output folder each time this program runs.    









# 4. Create zipped psf files using Phosim    

Program   : a2b_phosim_all_narrowbands.py
       
Depends   :
 
> * instance_catalogs/narrowband*.icat  
> * seds/narrowband*.sed
> * backgrounds/background1.bkg

    
               
Outputs   :   

> * phosim_output_extreme_psf/narrowband0/17_zipped_psf_fitsfiles  
> * phosim_output_extreme_psf/narrowband20/17_zipped_psf_fitsfiles 
               

This program creates zipped psffiles for all narrowbands inside the output folder.    
It will clobber the output folder.    

        




# 5. Unzip psffiles created from Phosim.      

Program   : a3b_unzip_all_psf.py    
 
Depends   : phosim_output_extreme_psf/narrowband*_out/zipped_psf    

Outputs   : extreme_psf/psf*.fits     

This program unzips zipped psffiles created from Phosim into the folder extreme_psf.  







# 6. Create psf for outliers using Phosim for given seed of outlier.    

Program   : outliers_psf_phosim.py   

Depends   :

+ a1b_create_instance_catalogs_seed.py  function create_catalogs (seed)
  argument: the SIM_SEED to run this program
                            
+ a2b_phosim_all_narrowbands.py function run_phosim    # gives zipped psfs   
  instance_catalogs/narrowband*.icat  
  seds/narrowbands*.sed  
  backgrounds/background1.bkg  

+ a3b_unzip_all_psf.py function unzip_psf
  phosim_output_extreme_psf/narrowband*/zipped_psf

Outputs     : outlier_psf/extreme_psf_seed/psf*.fits  

This program runs above programs a1b,a2b,a3b and it copies final output folder of  
a3b (i.e, extreme_psf) into the folder outlier_psf with given seed number.






# 7. Create imcat catalog file for given outlier of given seed.  

Program   : outliers_psf_imcat_analysis.py    

Depends     :

+ seed
+ outlier_psf/extreme_psf_seed/psf*.fits    


Outputs     : outlier_psf/extreme_psf_seed/narrowbands_seed.cat

This program creates catalog file for the given outlier of given seed.  
  
