import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class MyPlotLib:
	@staticmethod
    def histogram(data, features):
    	features = [f for f in features if np.issubdtype(data[f].dtype, np.number)]
        data[features].hist()
        plt.show()
	@staticmethod
    def density(data, features):
    	features = [f for f in features if np.issubdtype(data[f].dtype, np.number)]
        data[features].plot.kde(alpha=0.5)
        plt.show()
	@staticmethod
    def pair_plot(data, features):
    	features = [f for f in features if np.issubdtype(data[f].dtype, np.number)]
        pd.plotting.scatter_matrix(data[features], alpha=0.2)
        plt.show()
	@staticmethod
    def box_plot(data, features):
		features = [f for f in features if np.issubdtype(data[f].dtype, np.number)]
        data[features].plot.box()
        plt.show()
