# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 16:05:34 2026

@author: user
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

data = "C:/Users/user/Desktop/25CL05014-NMD/lab2_12jan/ORAS5_1deg_SST_1990_2008.nc"
ds =  xr.open_dataset(data)
print(ds)


SST = ds['SOSSTSST']
lon = ds['LONN179_181']
lat = ds['LAT']
time = ds['TIME']

'''
Q1
'''

bob_sst = SST.sel(LAT = slice(4,24),LONN179_181 = slice(76,100)).mean(dim = ('LAT','LONN179_181'))

bob_sst_monthly = bob_sst.groupby('TIME.month').mean(dim='TIME')

bob_sst_monthly.plot()
plt.xlabel("Months")
plt.ylabel("Temperature [in $^\circ$C]")
plt.title("Time series of Sea surface Temperature [in $^\circ$C]")
plt.xlim(1,12)
plt.ylim(26,31)
xs = np.arange(1,13,1)
xs2 = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
plt.xticks(xs,xs2)
plt.grid(True)
plt.tigh_layout()
plt.show()

'''
Q2
'''
import cartopy.crs as cc
import cartopy.feature as cf 

djf = [12,1,2]
mam = [3,4,5]
jjas = [6,7,8,9]
on = [10,11]

sst_djf = SST.sel(TIME = SST['TIME.month'].isin(djf),LAT = slice(4,24),LONN179_181 = slice(76,100)).mean(dim='TIME')
sst_mam = SST.sel(TIME = SST['TIME.month'].isin(mam),LAT = slice(4,24),LONN179_181 = slice(76,100)).mean(dim='TIME')
sst_jjas = SST.sel(TIME = SST['TIME.month'].isin(jjas),LAT = slice(4,24),LONN179_181 = slice(76,100)).mean(dim='TIME')
sst_on = SST.sel(TIME = SST['TIME.month'].isin(on),LAT = slice(4,24),LONN179_181 = slice(76,100)).mean(dim='TIME')


plt.figure(figsize = (22,12))
plt.suptitle("Seasonal Variation over Bay of Bengal")

ax = plt.subplot(2,2,1,projection = cc.Mercator())

cp1 = sst_djf.plot.contourf(transform=cc.PlateCarree(),cmap ='jet',vmin = 27,vmax = 29,levels = 80,add_colorbar = False)
ax.add_feature(cf.LAND,color = 'gray')
ax.gridlines(draw_labels = True)
ax.add_feature(cf.COASTLINE)
plt.title("Spatial plot over BOB in Winters")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(cp1,label = "$^\circ$C")

ax = plt.subplot(2,2,2,projection = cc.Mercator())

cp2 = sst_mam.plot.contourf(transform=cc.PlateCarree(),cmap ='jet',vmin = 27,vmax = 29,levels = 80,add_colorbar = False)
ax.add_feature(cf.LAND,color = 'gray')
ax.gridlines(draw_labels = True)
ax.add_feature(cf.COASTLINE)
plt.title("Spatial plot over BOB in Pre Monsoon")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(cp2,label = "$^\circ$C")

ax = plt.subplot(2,2,3,projection = cc.Mercator())

cp3 = sst_jjas.plot.contourf(transform=cc.PlateCarree(),cmap ='jet',vmin = 27,vmax = 29,levels = 80,add_colorbar = False)
ax.add_feature(cf.LAND,color = 'gray')
ax.gridlines(draw_labels = True)
ax.add_feature(cf.COASTLINE)
plt.title("Spatial plot over BOB in Monsoon")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(cp3,label = "$^\circ$C")

ax = plt.subplot(2,2,4,projection = cc.Mercator())

cp4 = sst_on.plot.contourf(transform=cc.PlateCarree(),cmap ='jet',vmin = 27,vmax = 29,levels = 80,add_colorbar = False)
ax.add_feature(cf.LAND,color = 'gray')
ax.gridlines(draw_labels = True)
ax.add_feature(cf.COASTLINE)
plt.title("Spatial plot over BOB in Post Monsoon")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(cp4,label = "$^\circ$C")

'''
Q3
'''

sst_dec1 = SST.sel(TIME = slice('1990-01-15','1999-12-15'),LAT = slice(4,24),LONN179_181 = slice(76,100)).mean(dim="TIME")
sst_dec2 = SST.sel(TIME = slice('2000-01-15','2008-12-15'),LAT = slice(4,24),LONN179_181 = slice(76,100)).mean(dim="TIME")


plt.figure(figsize = (28,10))
plt.suptitle("SST variation over Bay of Bengal in two different decades")

ax = plt.subplot(1,2,1,projection = cc.Mercator())
ax.gridlines(draw_labels=True)
ax.add_feature(cf.COASTLINE)
dec_cp1 = sst_dec1.plot.contourf(transform=cc.PlateCarree(),cmap = 'jet',vmin = 28,vmax = 29,levels = 100,add_colorbar = False)
ax.add_feature(cf.LAND,color = 'gray')
plt.title("Spatial plot over BOB in 1990-1999")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(dec_cp1,label = "$^\circ$C")

ax = plt.subplot(1,2,2,projection = cc.Mercator())
dec_cp2 = sst_dec2.plot.contourf(transform=cc.PlateCarree(),cmap = 'jet',vmin = 28,vmax = 29,levels = 100,add_colorbar = False)
ax.gridlines(draw_labels=True)
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.LAND,color = 'gray')
plt.title("Spatial plot over BOB in 2000-2008")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(dec_cp2,label = "$^\circ$C")

'''
Q4 
'''

N_bob = SST.sel(TIME = slice('2005-01-15','2006-01-15'),LAT = slice(14,24),LONN179_181 = slice(76,100)).mean(dim = ('LAT','LONN179_181'))
S_bob = SST.sel(TIME = slice('2005-01-15','2006-01-15'),LAT = slice(4,14),LONN179_181 = slice(76,100)).mean(dim = ('LAT','LONN179_181'))



plt.plot(N_bob, label="Northern Bay of Bengal")
plt.plot(S_bob, label="Southern Bay of Bengal")
plt.title("Time Series of Sea Surface Temperature [in $^\circ$C]")
plt.ylabel('Temperature in $^\circ$C')
plt.xlabel("Months")
plt.xlim(1, 12) 
plt.ylim(26, 31)

xs = np.arange(1, 13, 1)
xs2 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]    
plt.xticks(xs, xs2)
plt.grid(True)
plt.legend() 
plt.tight_layout()
plt.show()

# b) 

sp_bob = SST.sel(TIME = slice('2005-01-15','2005-12-15'),LAT = slice(4,24),LONN179_181 = slice(76,100)).mean(dim = 'TIME')
plt.figure(figsize = (12,8))
ax = plt.axes(projection = cc.Mercator())
ax.gridlines(draw_labels=True)
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.BORDERS)
cp_2005 = sp_bob.plot.contourf(transform = cc.PlateCarree(),cmap= 'jet',vmin = 28,vmax = 29,levels = 80,extend = 'both',add_colorbar = False)
ax.add_feature(cf.LAND,color = "gray")
plt.title("Temperature in $^\circ$C for year 2005")
plt.colorbar(cp_2005,label = "$^\circ$C")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
