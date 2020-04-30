import numpy as np
class AdvancedFilter:
	def mean_blur(self, arr):
		cp_arr = arr.copy()
		imx = arr.shape[0] - 1
		jmx = arr.shape[1] - 1
		for i in range (imx + 1):
			for j in range(jmx + 1):
				if i > 0 and i < imx and j > 0 and j < jmx:
					temp = arr[i-1:i+1,j-1:j+1]
					cp_arr[i][j][0] = np.sum(temp[:,:,0]) / 9
					cp_arr[i][j][1] = np.sum(temp[:,:,1]) / 9
					cp_arr[i][j][2] = np.sum(temp[:,:,2]) / 9
		return cp_arr
	def gaussian_blur(self, arr):
		cp_arr = arr.copy()
		imx = arr.shape[0] - 1
		jmx = arr.shape[1] - 1
		for i in range (imx + 1):
			for j in range(jmx + 1):
				if i > 0 and i < imx and j > 0 and j < jmx:
					cp_arr[i][j] = (4 * arr[i][j] + 2 * arr[i][j+1] + 2 * arr[i][j-1] + 2 * arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j-1] + 2 * arr[i-1][j] + arr[i-1][j+1] + arr[i-1][j-1]) / 16
		return cp_arr