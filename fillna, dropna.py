import pandas as pd
import numpy as np
df=pd.DataFrame([])

print("========================================================================================")
df = pd.DataFrame([[np.nan,2,np.nan,0],
                   [3,4,np.nan,1],
                   [np.nan,np.nan,np.nan,5]],
                  columns=list('ABCD'))
print(df)

print("========================================================================================")
print(df.dropna(axis=1, how='all'))
#axis가 0은 row, 1은 column. all은 전부 null값일때 드랍시킨다.
print("========================================================================================")
print(df.dropna(axis=0, how='any'))
#column에 하나라도 null이 있으면 드랍시킨다.

print("========================================================================================")
print(df.fillna(0))
values= {'A':0, 'B':1, 'C':2, 'D':3}
print(df.fillna(value=values))

print("========================================================================================")
print(df)   #nan값이 도처에 널려있다.
print(df['D'].mean()) #D행의 평균값은 2.0, media, min, max등을 사용가능하다
print(df.fillna(df['D'].mean())) #D행의 평균값으로 도처에 널린 nan값을 채운다.

print("========================================================================================")
print(df.isnull().sum()) #null인값 몇개
print(df.notnull().sum()) #not null인값 몇개
#null값이 많을때 유용하게 사용가능하다.















