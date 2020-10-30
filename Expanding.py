import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.DataFrame(np.random.randn(1000, 4),
                  index=pd.date_range('1/1/2015', periods=1000),
                  columns=['A', 'B', 'C', 'D'])

df=df.cumsum()

#df.rolling(window=60).sum().plot(subplots=True)
#df.rolling(window=len(df), min_periods=1).mean().plot()
#df.expanding(min_periods=1).mean().plot()
#plt.show()


dfe=pd.DataFrame({'B':[0,1,2,np.nan, 4]})
dfe=dfe.expanding(2).sum().plot()
plt.show()


