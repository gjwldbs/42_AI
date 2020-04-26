import numpy as np

class ScrapBooker:
	def crop(self, arr, dimensions, pos=(0,0)):
		posx = pos[0]
		posy = pos[1]
		dstx = posx + dimensions[0]
		dsty = posy + dimensions[1]
		if len(arr) < dstx or len(arr[0]) < dsty:
			print("Crop size is bigger than current img size")
			return arr
		return arr[posx:dstx, posy:dsty]
	def thin(self, arr, n, axis):
		if axis == 0:
			for i in range(n-1, len(arr), n-1):
				arr = np.concatenate((arr[:i,:], arr[i+1:,:]), axis=0)
			return arr
		else:
			for i in range(n-1, len(arr[0]), n-1):
				arr = np.concatenate((arr[:,:i], arr[:,i+1:]), axis=1)
			return arr
	def juxtapose(self, arr, n, axis):
		copy = arr
		for i in range(n - 1):
			arr = np.concatenate((arr, copy), axis=axis)
		return arr
	def mosaic(self, arr, height, width):
		arr = ScrapBooker.juxtapose(self, arr, dimensions[0], 0)
		return ScrapBooker.juxtapose(self, arr, dimensions[1], 1)
