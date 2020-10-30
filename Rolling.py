import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print("==================================================================")

s = pd.Series(np.random.randn(1000),
              index=pd.date_range('1/1/2015', periods=1000))  #2000년 1월 1일부터 랜덤하게 1000일까지 생성하는 함수
#print(s)

print("==================================================================")

#plt.plot(s)
#plt.show()

print("==================================================================")
s = s.cumsum()   #누적해서 더해줬다
#plt.plot(s)
#plt.show()

print("==================================================================")
s.rolling(window=30).mean().plot()   #윈도우의 사이즈만큼 값을 이동을 시켜준다.
plt.show() #롤링은 moving average를 구할때 쓴다. 추세선을 그릴때 쓴다






























