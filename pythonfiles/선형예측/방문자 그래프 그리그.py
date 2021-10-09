# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 00:11:37 2021

@author: dbtmd
"""

import pandas as pd
import requests as re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


def changestr(date):
    date1 = str(date)[0:4]
    date2 = str(date)[4:6]
    date3 = str(date)[6:]
    full = date1 + "-" + date2 +"-" + date3
    return full
    

df = pd.read_csv("C:\\Users\\733\\Desktop\\날씨\\선형예측\\전북방문자\\1_9월전라북도방문자.csv",encoding="euc-kr")
#df.drop("Unnamed: 0", axis=1,inplace=True)
df['날짜'] = df["날짜"].apply(changestr)

df['날짜'] = pd.to_datetime(df['날짜'], infer_datetime_format=True)
df['날짜수정'] = df["날짜"].dt.strftime("%m-%d")

print(df.dtypes)

print(df["날짜수정"])

"""
plt.figure(figsize=(30,20))
plt.plot(df["날짜수정"],df["방문자수"], label="외지인방문")
plt.xlim("08-01", "08-30")
plt.legend()
plt.title("단어별 좋아요수")
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig("1.png",dpi=600)
plt.show()
plt.close()
"""