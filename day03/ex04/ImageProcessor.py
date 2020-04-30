import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

class ImageProcessor:
	def load(self, path):
		im = Image.open(path)
		print("Loading image of dimesions {} x {}".format(im.size[0], im.size[1]))
		array = plt.imread(path)
		return array
	def display(self, array):
		return plt.imshow(array)