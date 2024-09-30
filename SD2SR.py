# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:09:32 2024

@author: ldw
"""

import aquacropeto as pyeto
import pandas as pd
import datetime


def computeRs(n,date):
    cdt = datetime.datetime.strptime(date,'%Y-%m-%d').date()
    J = cdt.toordinal()        #get Julian day
    solar_dec=pyeto.sol_dec(J) #Calculate the solar declination
    latitude = pyeto.deg2rad(Local_Lat) 
    sunset_hour_angle=pyeto.sunset_hour_angle(latitude,solar_dec)  #Calculate the angle at sunset
    inv_rel_dist_earth_sun = pyeto.inv_rel_dist_earth_sun(J) #Calculate the inverse relative distance between the Earth's sun
    Ra = pyeto.et_rad(latitude,solar_dec,sunset_hour_angle,inv_rel_dist_earth_sun) #Calculation of astronomical radiation
    N= pyeto.daylight_hours(sunset_hour_angle) #Enter the sunset hour angle to calculate the day length
    Rs = (0.25+(0.5*n/N))*Ra   #as, bs take the FAO default value
    return Rs
    

filename = 'xjh_daily_SD_Is_it_sunny.csv'
df =  pd.read_csv(filename)


Local_Lat = 31.2


rss = []

for i in range(len(df)):
    dtstr = str(df.Date.values[i])
    dt = '-'.join([dtstr[0:4],dtstr[4:6],dtstr[6:8]])
    rz = df.SD.values[i]
    rs = computeRs(rz,dt)
    rss.append(rs)

df['SR']=rss
df.to_csv('xjh_daily_SR_Is_it_sunny.csv')