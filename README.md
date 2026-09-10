# Spatio-Temporal Analysis of Sea Surface Temperature over the Bay of Bengal

## Overview
This project examines how sea surface temperature (SST) over the Bay of Bengal 
(BoB) varies across seasons, decades, and sub-regions, using gridded ocean 
reanalysis data.

## Objective
- Study the monthly and seasonal climatology of SST over the Bay of Bengal
- Compare SST spatial patterns across two decades (1990s vs 2000s) to check 
  for long-term change
- Compare SST between the Northern and Southern Bay of Bengal for a single year

## Data
- **Source:** ORAS5 (Ocean Reanalysis System 5) SST dataset
- **Time period:** 1990–2008 (with a focused comparison year of 2005)
- **Region:** Bay of Bengal (4°N–24°N, 76°E–100°E)

## Tools & Methods
- **Language:** Python
- **Key libraries:** xarray, numpy, matplotlib, cartopy
- **Method:** Extracted the BoB region from gridded SST data, computed monthly 
  and seasonal (DJF/MAM/JJAS/ON) climatologies, compared spatial SST patterns 
  between the 1990s and 2000s, and compared Northern vs Southern BoB SST time 
  series for 2005

## Results
- SST over the Bay of Bengal shows a clear seasonal cycle, generally warmest 
  during the pre-monsoon (MAM) period
- The decade-wise spatial comparison (1990s vs 2000s) showed a visible shift 
  in SST patterns between the two periods
- Northern and Southern BoB showed different temperature trends across the 
  months of 2005, highlighting sub-regional variation within the Bay

## Skills Demonstrated
- Working with gridded ocean reanalysis data (NetCDF)
- Seasonal and decadal climate comparison
- Regional sub-setting and time series analysis
- Scientific visualization (spatial maps, time series) using Python

## Author
Aaroksh Chauhan — M.Sc. Atmospheric and Oceanic Sciences, IIT Bhubaneswar
