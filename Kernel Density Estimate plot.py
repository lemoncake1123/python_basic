import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False

#KDE 히스토그램을 곡선으로 만들어줌
ser = pd.Series(np.random.randn(1000))
ser.plot.kde()
#ser.plot.density()   #kde와 똑같음



















plt.show()


























