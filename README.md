# MERRA2combinetoCSV.Python
Downloading MERRA-2 data without using wget, after filtering, combining individual netCDF4 files and then converting it into a .csv file with Python


MERRA-2 is up-to-date reanalysis data of NASA regarding earth system science. MERRA stands for "Modern-Era Retrospective analysis for Research and Applications" and despite "retrospective" word might make you think that it is old, one can reach data up-to previous months easily.
You can find detailed information of which observation systems they use for doing this retrospective analysis from the part of "c. Observing system" from https://journals.ametsoc.org/jcli/article/30/14/5419/97087/The-Modern-Era-Retrospective-Analysis-for-Research
Detailed description of the data and datasets related to MERRA-2 can be found in here: https://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich785.pdf

To reach these data and subset/download them, first you need to (freely) register via https://urs.earthdata.nasa.gov/users/new

# Subsetting and downloading

After logging in to your account, for being able to spatially and temporally filter your target dataset with no redundant variables, use https://disc.gsfc.nasa.gov/
In the dataset search space, right next to the search icon you can subset it temporally and spatially very easily. One warning is, if you want to download more than a year data or a data spanning two different years, do it separately for each year. 

After doing these subsets and choose your target variables, click "Get Data" button at the right bottom corner of the popped up window and you will get a list of links for every individual granule of your dataset. For instance for a time series of hourly radiation data set of a single coordination, you will get a different granule for each day. Copy all these links and directly paste it to Microsoft Office Word application including their hyperlink information. You can obtain Free Microsoft Office 365 if you are student currently, via this address: https://www.microsoft.com/en-us/education/products/office

Here with a quick macro in MS Word you may accelerate the downloading process by just clicking "Save" button for automatically opened windows. You need to open "Developer" tab to reach this option from MS Word. How you can do is written here https://support.microsoft.com/en-us/office/show-the-developer-tab-in-word-e356706f-1891-4bb8-8d72-f57a51146792

Hover to Developer Tab and click "Macros", then "Create" one.
The Visual Basic code for this macro is below: 

Dim alink As Hyperlink

For Each alink In Active.Document.Hyperlinks

  alink.Follow
  
Next alink

End Sub

If you want to obtain Microsoft Visual Studio freely as a student to write Visual Basic or many other codes within a strong IDE, you can use this link: https://visualstudio.microsoft.com/tr/dev-essentials/

When you run this macro, normally it would simultaneously open all links, but as downloading something is somewhat slower working, you can safely save all files without crashing your computer with excessive RAM use, and what you need to do is just clicking "Save" button when a pop-up window appears for saving a file. Comparing to automated wget command, it is of course more time-consuming but you can still do this job even while you are telephoning your significant other, or just want to do a chore without using your brain. It takes a few minutes to download 150 files. 

! Warning: You need to be logged in via web browser to the Earth Data of NASA while doing this.
! Warning: If you want to cancel the process for whatever reason, kill the Microsoft Word task through Task Manager.

# Combining all .nc timeseries files into a one file with all variables included, then converting it into a .csv

This part is explained in Python directly, with annotations included in it in "netcdftocsv.py" file I included here. What I conveniently use as a Python writing IDE is Anaconda's Spyder. You can obtain it freely from: https://www.anaconda.com/products/individual
After installing it, running "netcdftocsv.py" file with necessary changes into working directory and file names (explained in the script itself), your job will be done in a minute.

# Interpolating hourly timeseries data to 20 min (or any other equal interval <hour) 

This is done with hourto20min.R file. For various reasons you might want to interpolate MERRA-2 time series data to <hour intervals, and to be blunt, I don't know how to do it in Python, so instead I put an R script for the same purpose. I don't think it will be difficult for anyone as it is far more straightforward to have R than Python or Visual Studio. 

