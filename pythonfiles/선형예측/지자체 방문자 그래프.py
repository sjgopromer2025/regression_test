# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:47:11 2021

@author: 733
"""

import pandas as pd
import requests as re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

def changestrtemp(date):
    date = str(date).replace(".","-")
    if(len(date) == 3):
        date = date+"0"
    return "0"+date
    


def changestr(date):
    date1 = str(date)[0:4]
    date2 = str(date)[4:6]
    date3 = str(date)[6:]
    full = date1 + "-" + date2 +"-" + date3
    return full
    


city ="전주"

df = pd.read_csv("C:\\Users\\733\\Desktop\\날씨\\선형예측\\지역방문자\\1_9월"+city+"덕진구방문자.csv",encoding="euc-kr")

#df.drop("Unnamed: 0", axis=1,inplace=True)
#print(df)
df['날짜'] = df["날짜"].apply(changestr)

df['날짜'] = pd.to_datetime(df['날짜'], infer_datetime_format=True)
df['날짜'] = df["날짜"].dt.strftime("%m-%d")
print(df.dtypes)
print(df)

"""
df2 = pd.read_csv("C:\\Users\\733\\Desktop\\날씨\\선형예측\\온도\\"+city+"온도.csv",encoding="euc-kr")

#print(df2)
df2["날짜"] = df2["날짜"].apply(changestrtemp)
#df2['날짜'] = pd.to_datetime(df2['날짜'], infer_datetime_format=True)
#df2['날짜'] = df2["날짜"].dt.strftime("%m-%d")
print(df2.head(15))
print(df)

data1 = []
data2 = []
for item in df['날짜']:
    data1.append(item)
    
    
for item in df2['날짜']:
    data2.append(item)
    
    
    
merge_inner = pd.merge(df, df2)

print(merge_inner)
    
merge_inner.to_csv(city+".csv",encoding="euc-kr")
print(len(data1))
print(len(data2))
for item in data2:
    if(item not in data1):
        print(item)
"""
