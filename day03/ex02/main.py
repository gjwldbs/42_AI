from ScrapBooker import ScrapBooker

if __name__ == "__main__":
	scb = ScrapBooker()
	arr = np.eye(5)
	print(arr)
	print("\nMosaic (2x3) :\n")
	arr = scb.mosaic(arr, (2,3))
	print(arr)
	print("\nCrop to 3x4 from index [1,1] :\n")
	arr = scb.crop(arr, (3,4), (1,1))
	print(arr)
	print("\nThin every third line vertically (n=3, axis=0)\n")
	arr = scb.thin(arr, 3, 0)
	print(arr)
	print("\nThin every third line horizontally (n=3, axis=1)\n")
	arr = scb.thin(arr, 3, 1)
	print(arr)