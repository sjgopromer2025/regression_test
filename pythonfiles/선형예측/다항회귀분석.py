# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:53:32 2021

@author: 733
"""

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
"""

krfont = {'family':'NanumGothic', 'weight':'bold','size':10}
matplotlib('font',**krfont)
matplotlib.rcParams['axes.unicode_minus'] = False
"""




city = "군산"
df = pd.read_csv("C:\\Users\\733\\Desktop\\날씨\\선형예측\\merge\\"+city+".csv",encoding="euc-kr")
df = df.drop("Unnamed: 0", axis=1)
print(df.dtypes)

def regression(df):
        
    #############################################
    # 단순회귀분석
    maxcount = df["최저기온(시각)"].count()
    baserow = maxcount - int(maxcount * 0.2) #80%
    #print(baserow)
    
    train_data = df.iloc[0:baserow][["최저기온(시각)","최고기온(시각)","방문자수","일강우량","최저습도(시각)","최저기압(시각)","최고기압(시각)","최고습도(시각)"]]    #80%
    test_data  = df.iloc[baserow:][["최저기온(시각)","최고기온(시각)","방문자수","일강우량","최저습도(시각)","최저기압(시각)","최고기압(시각)","최고습도(시각)"]]   #20%
    #print(train_data)
    #print(test_data)
    
    #"일강우량","최저습도(시각)","	최고습도(시각)","최저기압(시각)","최고기압(시각)"

    


    X = np.array( df.iloc[0:baserow][["최저기온(시각)","최고기온(시각)","일강우량","최저습도(시각)","최저기압(시각)","최고기압(시각)","최고습도(시각)"]] )
    Y = np.array(df.iloc[0:baserow][["방문자수"]])

 
    #x = train_data[["최저기온(시각)","최고기온(시각)"]]
    #y = train_data["방문자수"]
    
    lr.fit(X,Y)
    #p = test_data[["최저기온(시각)","최고기온(시각)"]]
    p = np.array(df.iloc[baserow:][["최저기온(시각)","최고기온(시각)","일강우량","최저습도(시각)","최저기압(시각)","최고기압(시각)","최고습도(시각)"]])
    y_predict = lr.predict(p)
    return y_predict
    
    #print(y_predict)
    ##############################################
city = "군산"
df = pd.read_csv("C:\\Users\\733\\Desktop\\날씨\\선형예측\\merge\\"+city+".csv",encoding="euc-kr")
df = df.drop("Unnamed: 0", axis=1)

y_predict = regression(df)
print(y_predict)
maxcount = df["최저기온(시각)"].count()
baserow = maxcount - int(maxcount * 0.2) #80%

test_data  = df.iloc[baserow:][["최저기온(시각)","최고기온(시각)","방문자수","날짜"]]   #20%
print(test_data[['날짜',"방문자수"]])


