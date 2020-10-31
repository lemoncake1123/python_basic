import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False


df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area(stacked=False, grid=True)   #면적, stacked기본값이 True임
df.plot(grid=True)    #선으로 그려짐, 격자
plt.show()























