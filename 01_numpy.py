import numpy as np
'''The Numpy Library(Numpy=Numerical Python ) is the package of high-level mathematical and numerical functions and tools that are designed to work with the nympy array 
objects.
A numpy array is a high performance multi dimensional data structure and is all around more efficient and convenient than a Python List.
A one dimensional array can be directly compared to the Python list because they both store a list of numbers.
A two dimensional array has a grid structure with rows and colulmns.
A three dimensional array can be thought of as a stack of two-dimensional arrays.

NOTE: Numpy arrays are of Fixed size ,Indexed starting at 0 and contain elements of all the same type.
      They are ndarry objects and created using the np.array() function.
      Numpy arrays refer to dimension as axes and the number of axes is rank. '''

nd_array=np.array([[4,7,10,9]])
numpy_array=np.array([4,7,10,9])
print(nd_array)
print(numpy_array)
# print(nd_array[0,3])

print('shape ',nd_array.shape)
print('shape of numpy_array',numpy_array.shape)
# print('dtype',nd_array.dtype)

# nd_array[0,3]=55
# print(nd_array)

print('dimension',nd_array.ndim,'D')
print('dimension of numpy_array',numpy_array.ndim ,'D')

print('size',nd_array.size)
print('size of numpy_array',numpy_array.size)

my_array=np.array([[2,3,6,7],[9,8,1,4]])
print("Dimension or Rank of my_array",my_array.ndim)
print("Shape of my_array",my_array.shape)
print("Size of my_array",my_array.size)
print(my_array[1,3])


