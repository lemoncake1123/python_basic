import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False

##Plot kind: str
#‘line’: line plot(default)
#‘bar’: vertical bar plot
#‘barh’: horizontal bar plot
#‘hist’: histogram
#‘box’: boxplot
#‘kde’: Kernel Density Estimation plot
#‘density’: same as ‘kde’
#‘area’: area plot
#‘pie’: pie plot
#‘scatter’: scatter plot
#‘hexbin’: hexbin plot

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()


df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.plot()
plt.show()


df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df3['A']=pd.Series(list(range(len(df))))   #A열 추가, 1000개
#df3 = df3.cumsum()
#df3.plot()
df3.plot(x='A', y='B')
plt.show()


















