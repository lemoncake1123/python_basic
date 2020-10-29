print("========================================================================================")
#같은 카테고리의 데이터끼리 모아서 연산한다.
import pandas as pd
import seaborn as sns
import numpy as np

df=sns.load_dataset("mpg")

k=df.groupby(by="origin")['cylinders'].mean()    #size, min, max, mean, median등 사용가능
print(k)

print("========================================================================================")

kk=df["origin"].value_counts()
print(kk)

print("========================================================================================")

kkk=pd.DataFrame(df.groupby(['model_year', 'origin'])['cylinders'].mean())
print(kkk)

print("========================================================================================")

df2= pd.DataFrame([[4, 7, 10],[5, 8, 11],[6, 9, 12]], index=[1, 2, 3], columns=['a', 'b', 'c'])
print(df2['b'].shift(1))   #행이 하나씩 쉬프트 된것, -1은 하나 위로, b행만 나타냄

print("========================================================================================")

print(df["model_year"].rank(method='dense').value_counts())  #ranking by dense, 순위값을 보여줌
print("========================================================================================")

print(df["model_year"].rank(pct=True))   #percent
print("========================================================================================")

print(df["model_year"].rank(method='first'))   #첫번째값 순위가 1위가 됨.

print("========================================================================================")
print(df2.cumsum())  #누적해서 더하기, 위의 값이 더해져서 내려옴.
print(df2.cummax())  #최댓값 출력, 만약 2열이 값이 13이고 3열의 값이 11이면, 최댓값인 13을 3열에도 적음
print(df2.cummin())  #위와 정반대
print(df2.cumprod()) #누적하여 값을 곱해줌















































