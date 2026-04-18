import numpy as np

dataList = [2,7,3,1,5,4,3,7,8]
print("numpy example with mean :: ",np.mean(dataList))
print("numpy example with median :: ",np.median(dataList))
print("numpy example with sum :: ",np.sum(dataList))
print("NumPy is used to work with arrays. The array object in NumPy is called ndarray.")
print("numpy example with  :: ",np.array(dataList) )
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
print(arr.ndim)
