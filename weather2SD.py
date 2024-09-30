# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:59:16 2023

@author: Administrator
"""

import pandas as pd
import datetime
import numpy as np

filename = 'xjh_Is_it_sunny_result.csv'


names = ['picname','picnametime','weatherType1']

dfResult=pd.read_csv(filename,names=names,encoding='gbk')


dfResult['months'] = dfResult.picname.apply(lambda x:x[4:6])
dfResult['days'] = dfResult.picname.apply(lambda x:x[6:8])
dfResult['hours'] = dfResult.picname.apply(lambda x:x[8:10])

fromdt = datetime.datetime(2023,1,1)
todt = datetime.datetime(2024,1,1)
deltt = datetime.timedelta(hours=1)

newdf = pd.DataFrame([],columns=['days','picGet'])
picGet = []
days = []

dnow = -1
while fromdt<todt:
    days.append(fromdt.strftime('%Y%m%d%H'))
    tempdf = dfResult[(dfResult.months==('%02d'% fromdt.month)) & (dfResult.days==('%02d'% fromdt.day)) & (dfResult.hours==('%02d'% fromdt.hour))]  
    tempdfsunny = tempdf[(tempdf.weatherType1=='yes')|(tempdf.weatherType1=='sunny')]
    v = len(tempdfsunny)
    picGet.append(v/6.0)    
    mstr = str(fromdt.year)+'-'+str(fromdt.month)+'-1 00:00'    
    fromdt = fromdt + deltt
   
newdf.picGet = picGet
newdf.days = days
newdf['months'] = newdf.days.apply(lambda x:x[4:6])
newdf['hours'] = newdf.days.apply(lambda x:x[8:10])
newdf['d'] = newdf.days.apply(lambda x:x[6:8]) 
newdf.to_csv('xjh_hourly_SD_Is_it_sunny.csv')
newdf111=newdf[(newdf.hours>'05')&(newdf.hours<='18')]

fromdt = datetime.datetime(2023,1,1)
todt = datetime.datetime(2024,1,1)
deltt = datetime.timedelta(days=1)

daypic=[]
while fromdt<todt:
    days.append(fromdt.strftime('%Y%m%d%H'))
    tempdf = newdf[newdf.d==('%02d'% fromdt.day)]
    tempdf = tempdf[tempdf.months==('%02d'% fromdt.month)] 
    v = np.sum(tempdf.picGet)
    daypic.append(v)
    
    fromdt = fromdt + deltt

fromdt = datetime.datetime(2023,1,1)
todt = datetime.datetime(2024,1,1)
deltt = datetime.timedelta(days=1)
dates = []
while fromdt<todt:
    dates.append(fromdt.strftime('%Y%m%d'))   
    fromdt = fromdt + deltt

df=pd.DataFrame([],columns=['Date','SD'])   
df['Date']=dates 
df['SD']=daypic
df.to_csv('xjh_daily_SD_Is_it_sunny.csv')






    

    
    
    