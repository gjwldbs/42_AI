import numpy as np
import string
array = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],[1, 2, 3, 4, 5]]
n = 2
i = 0
#for i in range(n-1, len(array), n-1):
array = np.concatenate((array[:i,:], array[i+1:,:]), axis=0)

print(array)
