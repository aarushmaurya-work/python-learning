import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)


def info(arr: np.ndarray):
    print(arr.size)  # Total no of elements in the array
    print(arr.shape)  # Shape of the array
    print(arr.ndim)  # Dimension of the array
    print(arr.nbytes)  # No of bytes of the array elements
    print(arr.dtype) #The data type


