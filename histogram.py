import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False


df4 = pd.DataFrame({'a': np.random.randn(1000) + 1,
                    'b': np.random.randn(1000),
                    'c': np.random.randn(1000) - 1},
                   columns=['a', 'b', 'c'])


#df4.plot.hist(alpha=0.5)
#df4.plot.hist(stacked=True, bins=20)   #누적, bin은 막대기를 의미, 여기서 막대기 20개
#df4['a'].plot.hist(orientation='horizontal', cumulative=True)   #축바꿈, 누적
#df4['a'].diff().hist()   #diff는 차분 을 의미함. 앞의 값에서 뒤의 값을 빼는 함수.
#df4[['a', 'b', 'c']].diff().hist(color='k', alpha=0.5, bins=50)    #알파는 투명도, 막대기 50개
plt.show()

data = pd.Series(np.random.randn(1000))    #이거나
data = pd.DataFrame({'a':np.random.randn(1000),    #이걸로 데이터 생성
                     'b':np.random.randint(0,4,1000)})

data.hist(by=np.random.randint(0, 4, 1000), figsize=(6, 4))
data['a'].hist(by=data['b'], figsize=(6, 4))

plt.show()






















