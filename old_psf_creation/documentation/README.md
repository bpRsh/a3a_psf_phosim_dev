### Programs Description:

#### 1. Create catalogs

Program:  create_20_catalogs.py 
Inputs   : none  
Outputs : instance_catalogs/broadband.icat    and instance_catalogs/barrowband*.icat

This program creates 20 narrowband instance catalogs and one broadband catalog inside the folder instance_catalogs.
These instance catalogs are required by Phosim software.

#### 2. Create seds 

Program: create_seds.py  
Inputs    : sed_flat.txt  
Outputs   : seds/broadband.sed and narrowband*.sed
    
This program creates 21 sed_files from the given input_sed_file. It also normalizes the flux at wavelength 500 nm (after rescaling down by the factor of  100). The broadband wavelength range is 531-696 nm, which was chosen from LSST r-band filter such that transmission is NOT <= 5%. For each output sed_file, the non_zero fluxes are in their order and all the other fluxes are zero EXCEPT flux for 500 nm.

#### 3.  Choose your background   

The physics_command for the phosim software is chosen with following modifications:  
pixelsize 1.5  
saturation 0  
blooming 0  
chargesharing 0

The location of this background file is:  
backgrounds/background1.bkg
We get the saturation effect and the resulting psf looks like comet shape, if we take saturation to be 1.

#### 4. Run the phosim software to create psfs  
Program :  _run_all_catalogs.py_  
Inputs      : instance_catalogs/*.icat  &  backgrounds/background1.bkg    
Outputs     : outputs/broadband_out/17_zipped_psf_fitsfiles  AND  narrow bands.

This script run the phosim software command:  
cd ~/phosim;  
 ./phosim instance_catalogs/required_instance_catalog.icat  
  -c Research/twenty_catalogs/backgrounds/background1.bkg  
   -o Research/twenty_catalogs/outputs
   
    N.B. phosim is installed at ~/phosim
     icat is instance_catalog file        
      -c is physics_command file, background added later
      -o is output_folder

      To run phosim command we need an instance_catalog, background is optional.
      All the paths are relative to phosim installation directory.
      
      For the each input instance catalog, the phosim software gives 
      16 output amplifier zipped psf file and   
      ONE zipped electron image (fits file). 
      We need this electron image and do not need amplifier images. 

#### 5. Check the difference between sum_of_narrobands_psf and broadband_psf
+ The program _sum_narrowbands.py_ sums up all the psf images and create _narrowbands_sum.fits_ .  
+ The program _decompress_broadband.py_ will extract the broadband psf and put it inside outputs folder.  
+ The program _difference.fits_ will create a fitsfile which is the difference of above two psf images. This difference fitsfile should have small values and should have NO STRUCTURE.
+ The program _decompress_all_psfs.py_ will extract all the psf files into the directory output_psfs. This will give 20 narrowband psf and one broadband psf.

 
