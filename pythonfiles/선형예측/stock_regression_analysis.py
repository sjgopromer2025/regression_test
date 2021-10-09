import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import rc
from sklearn.linear_model import LinearRegression
import pymysql
from datetime import datetime
from dateutil.relativedelta import relativedelta

#DB연결 MySQL Connection 연결
conn = pymysql.connect(host = '192.168.0.165', user = 'root' , db='ezenstock' , password = 'ezen', charset='utf8')

#cursor = 가리키다
# Connection 으로부터 Cursor 생성
curs = conn.cursor() 

# 검색할 주식이름    나중에 input으로 받아서 자바에서 검색 input값 넘어오면 그걸 파이썬으로 넘겨서 돌림
code_name = "경방"

# 검색한 주식이름 데이터 뽑아옴
select_sql = "select * from stock where name='" + code_name + "' order by day desc"
df = pd.read_sql_query(select_sql, conn)
#print(df)
lr = LinearRegression()

def regression(df):
        
    #############################################
    # 단순회귀분석
    maxcount = df["start"].count()
    baserow = maxcount - int(maxcount * 0.8)
    #print(baserow)
    
    train_data = df.iloc[baserow:][["start","final","day"]]
    test_data  = df.iloc[0:baserow][["start","final","day"]]
    #print(train_data)
    #print(test_data)
 
    x = train_data[["start"]]
    y = train_data["final"]
    
    lr.fit(x,y)
    p = test_data[["start"]]
    y_predict = lr.predict(p)
    return y_predict
    
    #print(y_predict)
    ##############################################


regression(df)


# SQL문 실행
sql = "select start from stock where name='" + code_name +"' order by day desc limit 0,1"
curs.execute(sql)
conn.commit()

# sql에서 시가를 뽑아와서 추출함
datas = curs.fetchall()
for data in datas:
	data

data_0 = 0
# 학습한 데이터로 시가를 넣고 예측
prdata = data
y_predict = lr.predict([prdata])
print(int(y_predict))
data_1 = int(y_predict)
print("-------------------------------")

# 이상하게도 두번째 값예측할때는 2차원배열로 해야 돌아감 아니면 오류남
prdata = data_1
y_predict = lr.predict([[prdata]])
print(int(y_predict))
data_2 = int(y_predict)
print("-------------------------------")

prdata = data_2
y_predict = lr.predict([[prdata]])
print(int(y_predict))
data_3 = int(y_predict)

# 데이터셋을 리스트로 만들어서 합치는데 함수에서 1부터 돌기위해 첫번째 dataset[0]은 날라가기에 아무값이나 넣음 
dataset = [data_0, data_1, data_2, data_3]
#print(dataset)

# 오늘 날짜를 얻음
today = datetime.today()

'''
insert_sql  = "insert into prstock "
insert_sql += "(pr_code,pr_code_name,pr_code_wdate,pr_code_final) "
insert_sql += "values "
insert_sql += "('" + df["code"][0] + "','" + code_name + "','" + str(tomorrow_1.date()) + "','" + str(data_1) + "') "
#curs.execute(insert_sql)
#conn.commit()
#conn.close()
'''
# DB에서 prstock에 저장된 
# 코드네임 받는거 바로 밑에거 고쳐야함
wdate_sql = "select pr_code_wdate,pr_code_name from prstock where pr_code_name='" + code_name + "' order by pr_code_wdate desc limit 0,3"
df_wdate = pd.read_sql_query(wdate_sql, conn)
df_wdate = df_wdate.sort_values(by=['pr_code_wdate'], axis=0, ascending=True)   # 날짜 기준 반대로 정렬
df_wdate = df_wdate.sort_values("pr_code_wdate",ignore_index=True)              # 날짜 반대로 됬으나 인덱스도 뒤집혀서 인덱스값 초기화
print(df_wdate)
# 날짜 번호 저거 암튼 정리하고 data저것도 받는거 i로 돌아가면서 증가하게 만들어놓아라
def insertsql(df_wdate, df,code_name,dataset):
    for i in range(1,4):
        tomorrow = today + relativedelta(days=i)
        # 3일후 날짜까지 얻기 위하여 i 번 돌면서 날짜를 얻음
        if(tomorrow.date() == df_wdate["pr_code_wdate"][i-1] and df_wdate["pr_code_name"][0] == code_name):
            break

        insert_sql  = "insert into prstock "
        insert_sql += "(pr_code,pr_code_name,pr_code_wdate,pr_code_final) "
        insert_sql += "values "
        insert_sql += "('" + df["code"][i] + "','" + code_name + "','" + str(tomorrow.date()) + "','" + str(dataset[i]) + "') "
        curs.execute(insert_sql)
    conn.commit()
    conn.close()


insertsql(df_wdate, df,code_name,dataset)












