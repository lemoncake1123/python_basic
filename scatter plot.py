import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False


df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])


ax = df.plot.scatter(x='a', y='b', color='DarkRed', label='Group 1')
df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ax)  #ax를 스캐터에 한번 더 넣어줌


df.plot.scatter(x='a', y='b', c='c', s=50, grid=True)   #scatter에서는 x, y를 꼭 지정해줘야함, s는 사이즈, c는 세번째 점


df.plot.scatter(x='a', y='b', s=df['c'] * 200)   #c만 점 크기를 키움







plt.show()









