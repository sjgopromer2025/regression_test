# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 02:20:10 2021

@author: dbtmd
"""


from bs4 import BeautifulSoup as bt
import pandas as pd
import os
import sys
import urllib.request
from urllib import parse
import requests as re



df = pd.read_csv("전주한달온도.csv",encoding="euc-kr")

print(df)