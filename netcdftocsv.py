# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:01:19 2020

@author: GÜRAY
"""
##################################################
##     ##     ##    ## ### ##     ##    ###     ##
#### #### ### ## ## ##  ## ## ### ## ### ## ### ##
#### #### ### ##   ### # # ## ### ## ### ## ### ##
#### #### ### ## ## ## ##  ##     ## ### ## ### ##
#### ####     ## ## ## ### ## ### ##    ###     ##
##################################################

# Aim: Converting .nc files automatically to .csv

"""
Content: 
I already downloaded a hell amount of .nc files of MERRA-2. I will first
combine all of them to a single netCDF file then I will convert that guy to
a .csv file which will be easier to work with in Microsoft Excel later.
"""         

# Part 0: Importing relevant packages

import os
import xarray

# Part 1: NetCDF merging part

# Here set your working directory accordingly!!!! Be careful
# This is the file all of your .nc are present.

os.chdir("####")

"""
'MERRA2_400 is present in all the files of .nc I want to integrate, so
change this MERRA2_400 to whatever your target files collectively includes

concat_dim is what you want to concatenate accordingly. Since this is 
expected to be a time-series integration, and the time is specified with
"time" in this .nc files, it can remain like that.

combine="by_coords" is related to coordinates, but here we have only one
coordinate so for this purpose it is relatively ineffective.
"""


ds = xarray.open_mfdataset('MERRA2_400*.nc', combine='by_coords',
                           concat_dim="time") 

ds.to_netcdf('merrarad.nc')  # This creates the '' file in your current wd

# Part 2: NetCDF to csv or xlsx format

import xarray as xr

# In the following ("") specify the place of your time-series combined .nc
nc = xr.open_dataset("####")

# Now 'rad.csv' is actually name of the about to be generated .csv file
nc.to_dataframe().to_csv('rad.csv')

# Happy Birthday to your combined time-series .csv file!
