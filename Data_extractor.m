clc
close all

lon = ncread("SODA_Temp.nc","LON173_180");
lat = ncread("SODA_Temp.nc",'LAT176_183');
depth = ncread('SODA_Temp.nc','LEV1_19');
Time = ncread("SODA_Temp.nc",'TIME');
temp = ncread("SODA_Temp.nc",'TEMP');