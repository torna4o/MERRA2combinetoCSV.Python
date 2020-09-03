##################################################
##     ##     ##    ## ### ##     ##    ###     ##
#### #### ### ## ## ##  ## ## ### ## ### ## ### ##
#### #### ### ##   ### # # ## ### ## ### ## ### ##
#### #### ### ## ## ## ##  ##     ## ### ## ### ##
#### ####     ## ## ## ### ## ### ##    ###     ##
##################################################

# Script to make MERRA-2 hourly data to 20 min (or some other <1 hour equal interval) period data

# Part 0: Loading the data and required package

library(xts)
winddata <- read.csv(file="####", header=TRUE, sep=",")

# Part 1: The magic! xts object solution

# We create an xts object with a datetime inex and relevant variable columns to be interpolated
# orber.by part is where you specify the type of indexing date you have in your data
# if it is to be only date, as.Date is sufficient, if like here Date Time, as.POSIXct is required, etc.

x <- xts(winddata[, c("ULML","VLML")], order.by=as.POSIXct(winddata$time))

# Creating empty xts later to fill it with our data and then interpolate the empty places

x20min <- xts(, order.by = seq(start(x), end(x), by = "20 min")) # You can ignore if there is a warning here in RStudio

# Here fill part do the interpolation

y <- merge(x, x20min, fill = na.approx)

# Part 2: Creating the relevant csv with newly interpolated one

# write.zoo is the proper way to print the xts object to a csv

write.zoo(y, file="####", sep=",")
