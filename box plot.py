import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))


df.iloc[5].plot(kind='bar')    # --same plot.bar()
plt.axhline(0, color='k')    # middle line
plt.show()


df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot.bar(stacked=True)   #누적해서 나옴
plt.show()

df2.plot.barh(stacked=True)   #x y 축 90도 회전
plt.show()



















