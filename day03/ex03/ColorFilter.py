import numpy as np
from PIL import Image, ImageOps
class ColorFilter:
	def invert(self, arr):
		cp_arr = 1 - arr.copy()
		return cp_arr
	def to_blue(self, arr):
		cp_arr = np.zeros(arr.shape)
		cp_arr[:,:,0] = 0 #0: removing red
		cp_arr[:,:,1] = 0 #1: removing green
		cp_arr[:,:,2] = arr[:,:,2]
		return cp_arr
	def to_green(self, arr):
		cp_arr = arr.copy()
		cp_arr *= [0, 1, 0]
		return cp_arr
	def to_red(self, arr):
		cp_arr = arr.copy()
		cp_arr -= (self.to_blue(arr) + self.to_green(arr))
		return cp_arr
	def celluloid(self, arr, tresh = 4):
		cp_arr = np.array(arr)
		hold = np.linspace(0.0, 1.0, num=tresh, endpoint=False)[::-1]
		for i in hold:
			idx = arr >= i
			arr[idx] = -1
			cp_arr[idx] = i
		return cp_arr
	def to_grayscale(self, arr, filter):
		if self.filter is 'm' or 'mean':
			cp_arr = np.zeros(arr.shape)
			i = 0
			while i < 3:
				cp_arr[:,:,i] = (arr[:,:,0] + arr[:,:,1] + arr[:,:,2]) / 3
				i += 1
			return cp_arr
		else:
			cp_arr = np.zeros(arr.shape)
			i = 0
			while i < 3:
				cp_arr[:,:,i] = 0.299 * arr[:,:,0] +  0.587 * arr[:,:,1] + 0.114 *arr[:,:,2]
				i += 1
			return cp_arr