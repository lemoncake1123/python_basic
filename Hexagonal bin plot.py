import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False

#Hexbin plot은 데이터가 클 때 각각의 점을 산점도로 표현할때의 단점을 보완할 수 있습니다.  Histogram + Scatter plot 합쳐둔것


df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])    #천개의 행, 두개의 열
df['b'] = df['b'] + np.arange(1000)    #b열에 각각의 내림차순 1~1000 인덱스 값을 추가함
df.plot.hexbin(x='a', y='b', gridsize=10)

df['z'] = np.random.uniform(0, 3, 1000)   #0~3까지의 범위를 1000개 만듬
df.plot.hexbin(x='a', y='b', C='z', reduce_C_function=np.max, gridsize=15)   #max, min, median등 가능
#기본적으로 각 (x,y)점 주변의 개수에 대한 히스토그램이 계산됩니다. C및 reduce_C_function 인수에 값을 전달하여 대체 집계를 지정할 수 있습니다.








plt.show()

























