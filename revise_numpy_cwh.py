# import numpy as np
# numpy_array=np.array([3,4,5,6,7,8],np.int32)
# print(numpy_array)
# print(numpy_array[3])
# # print(numpy_array[0,1])    this throws an error.
# numpy_array_2d=np.array([['l','i','s','t'],[4,7,9,10]])
# print(numpy_array_2d[0,1])
# print(numpy_array_2d[1,2])
# print(numpy_array_2d[1,3])

# numpy_array_2d[0,1]='a'
# print(numpy_array_2d)


# print("Shape of numpy_array,",numpy_array.shape)
# print("Shape of numpy_array_2d",numpy_array_2d.shape)

# print("Size of numpy_array,",numpy_array.size)
# print("Size of numpy_array_2d ,",numpy_array_2d.size)

# print("Dtype of numpy_array",numpy_array.dtype)
# print("Dtype of numpy_array_2d",numpy_array_2d.dtype)


import numpy as np 
x=np.arange(2,8,2)
x=np.append(x,x.size)
x=np.sort(x)
print(x)

y=np.arange(10)
print(y)
print(y[y<5])

print(y[(y>5)&(y%2==0)])

print(y.sum())

print(y.min())
print(y.max())

print(y*2)
print(y+1)

print(np.median(y))
print(np.mean(y))
print(np.var(y))
print(np.std(y))