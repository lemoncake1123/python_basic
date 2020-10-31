import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False


df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])  #10개의 행, 5개의 열
print(df.describe())   #r의 summary와 동일
df.plot.box()    #최대 최소 234분위 수를 이용해서 그린게 박스플롯임

color = {'boxes': 'DarkGreen',
         'whiskers': 'DarkOrange',
         'medians': 'DarkBlue',
         'caps': 'Gray'}
df.plot.box(color=color, sym='r+')    #r은 빨강색을 의미, 심볼을 십자가 형태로 표시한다.
df.plot.box(vert=False, positions=[1, 4, 5, 6, 8])  #축 90도 회전

df = pd.DataFrame(np.random.rand(10, 5))

df = pd.DataFrame(np.random.rand(10, 2), columns=['Col1', 'Col2'])
df['X'] = pd.Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
bp = df.boxplot(by='X')
df.boxplot()    #이렇게 그리면 뒤에 격자가 생김




np.random.seed(1234)   #랜덤 시드를 지정해주었기에, 시드가 1234인 사람의 결과는 랜덤할지언정 동일하다.
df_box = pd.DataFrame(np.random.randn(50, 2))    #50개 열, 2개 행
df_box['g'] = np.random.choice(['A', 'B'], size=50)
df_box.loc[df_box['g'] == 'B', 1] += 3
bp = df_box.groupby('g').boxplot()    #격자
bp = df_box.boxplot(by='g')






plt.show()






















