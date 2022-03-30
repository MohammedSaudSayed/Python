import numpy as np

x = np.array(10)

oneDim = np.array([1, 2, 3])
twoDim = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
threeDim = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

print(x.ndim)
print(oneDim.ndim)
print(twoDim.ndim)
print(threeDim.ndim)
