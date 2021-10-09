# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:21:00 2021

@author: 733
"""


"""
def regression(df):
        
    #############################################
    # 단순회귀분석
    maxcount = df["최저기온(시각)"].count()
    baserow = maxcount - int(maxcount * 0.2) #80%
    #print(baserow)
    
    train_data = df.iloc[0:baserow][["최저기온(시각)","최고기온(시각)","방문자수"]]    #80%
    test_data  = df.iloc[baserow:][["최저기온(시각)","최고기온(시각)","방문자수"]]   #20%
    #print(train_data)
    #print(test_data)
    
 
    x = train_data[["최저기온(시각)","최고기온(시각)"]]
    y = train_data["방문자수"]
    
    lr.fit(x,y)
    p = test_data[["최저기온(시각)","최고기온(시각)"]]
    y_predict = lr.predict(p)
    return y_predict
    
    #print(y_predict)
    ##############################################
city = "군산"
df = pd.read_csv("C:\\Users\\733\\Desktop\\날씨\\선형예측\\merge\\"+city+".csv",encoding="euc-kr")
df = df.drop("Unnamed: 0", axis=1)
print(df.dtypes)

y_predict = regression(df)
print(y_predict)


maxcount = df["최저기온(시각)"].count()
baserow = maxcount - int(maxcount * 0.2) #80%

test_data  = df.iloc[baserow:][["최저기온(시각)","최고기온(시각)","방문자수"]]   #20%
print(test_data['방문자수'])

"""





X = np.array(df[["최저기온(시각)","최고기온(시각)"]])
y = np.array(df[["방문자수"]])

