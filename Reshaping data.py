print("========================================================================================")
import pandas as pd
import numpy as np
import seaborn as sns

df=sns.load_dataset("mpg")
print(df.shape)

print("========================================================================================")
print(df.head())

print("========================================================================================")
print(df.sort_values('mpg', ascending=True)) #mpg 오름차순 기준으로 정렬

print("========================================================================================")
df_1=df.rename(columns={'model_year':'year'}) #저장하는 방법
print(df_1)

print("========================================================================================")
print(df.sort_index()) #인덱스별 정렬

print("========================================================================================")
print(df.reset_index()) #인덱스가 없을때 인덱스를 새로 만들고 싶다 할때 쓰인다.

print("========================================================================================")
print(df.drop(columns=['mpg', 'year']))  #특정 열을 생략 드랍 시킴

















