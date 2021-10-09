# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 22:19:11 2021

@author: dbtmd
"""


from bs4 import BeautifulSoup as bt
import pandas as pd
import os
import sys
import urllib.request
from urllib import parse
import requests as re



def get_html(url):
    request = urllib.request.Request(url,headers=getagent())
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
            response_body = response.read()
    else:
            print("Error Code:" + rescode)
    return response_body.decode('cp949')

def getagent():
    agent_head = {
      "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
      "accept" :  "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
      }
    return agent_head

    
encText = urllib.parse.quote("전주 여행")
page = 1
body=""
list1 =[]









"""
전주 146
정읍 245
김제 737 
익산 702
군산 140
완주 734
임실 244
부안 243
"""



url = "https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_day?202101310145&0&DAYDB&146&m&M"
html = get_html(url)
#print(html)

soup = bt(html,"lxml")

#날씨 헤더
table = soup.find("tr",class_="name")
td = table.findAll("td")
t_head = []
for item in td:
    #print(item.text)
    t_head.append(item.text)
#print(t_head)
#날씨 헤더 끝_____

#날씨 온도 데이터 가져오는 코드


date_list = ["0930","0831","0731","0630","0531","0430","0331","0228","0131"]
location_code = ["146","245","737","702","140","734","244","243"]

for code in location_code:
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    data9 = []
    for date in date_list:
        data = ""
        datas = []
        print(date)
        url = "https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_day?2021"+date+"0145&0&DAYDB&"+code+"&m&M"
        print(url)
        html = get_html(url)
        soup = bt(html,"lxml")
        table2 = soup.findAll("tr",class_="text")
        #print(soup)
        
        for tr_item in table2:
            #print(tr_item.text)
            
            table2_1 = tr_item.findAll("td")
            for td_item in table2_1:
                #print(td_item.text)
                position = td_item.text.find("(")
                if(position != -1):
                    data = td_item.text[:position]
                else:
                    data = td_item.text
                datas.append(data.strip())
        
        #한페이지에 32개를 출력해줌
        
        #print(len(data))
        #print(datas[0])
        #print(datas[0+9])
        
        for num in range(0,32):
            data1.append(datas[0+(num*9)])
            data2.append(datas[1+(num*9)])
            data3.append(datas[2+(num*9)])
            data4.append(datas[3+(num*9)])
            data5.append(datas[4+(num*9)])
            data6.append(datas[5+(num*9)])
            data7.append(datas[6+(num*9)])
            data8.append(datas[7+(num*9)])
            data9.append(datas[8+(num*9)])
    
    
    table_dict = {
        t_head[0] : data1,
        t_head[1] : data2,
        t_head[2] : data3,
        t_head[3] : data4,
        t_head[4] : data5,
        t_head[5] : data6,
        t_head[6] : data7,
        t_head[7] : data8,
        t_head[8] : data9,
        }
    
    
    df = pd.DataFrame(table_dict)        
    
    df.to_csv(code+"온도.csv",encoding="euc-kr")



