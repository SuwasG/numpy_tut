'''There are 5 General mechanisms for creating numpy arrays
1> conversion from other python structures'''
from matplotlib.pyplot import axis
import numpy as np
list_array=np.array([[[4,7,11,90],[8,16,24],[22,33,44]]])
print(list_array)

print(list_array.dtype)

print(list_array.shape)

print(list_array.ndim)
# 2> Intrinsic numpy array creation objects(eg. arange,ones,zeros etc.)
print('2nd method')
Zeros=np.zeros((3,5)) # array of 0s having size of 3 rows and 5 columns.
print(Zeros)

print("dtype",Zeros.dtype)

print( "Shape",Zeros.shape)

print("Dimension",Zeros.ndim)

print("Itemsize",Zeros.itemsize)

''' Both arange() and linspace() functions evenly space values.However,np.arange ()  returns values up to the end parameters whereas 
np.linspace() returns a specified number of elements only.'''
arange=np.arange(20)
print("arange1",arange)

rng=np.arange(20,100,10)   # start,stop,step
print("arange2",rng)

lspace=np.linspace(1,60,10)  # (start ,stop ,required quantity)
print("linespace",lspace)

emp=np.empty((4,7))
print("emp",emp)

emp_like=np.empty_like(lspace)
print("empty_like",emp_like)

identity=np.identity(10)
print("identity matrix",identity)

arr=np.arange(100)
print("arr",arr)

print("reshaping",arr.reshape(5,20))

print("ravel",arr.ravel())

y=[[1,8,3],[4,0,9],[5,7,2]]
arrY=np.array(y)
print(arrY)

print(arrY.sum(axis=0))

print(arrY.sum(axis=1))

print("Transpose",arrY.T)

print("Flatiter",arrY.flat)

print("nbytes",arrY.nbytes)

one=np.array([7,9,4,5])
print("argmax",one.argmax())

print("argmin",one.argmin())

print("argsort",one.argsort())

print(arrY.argmax(axis=0))

print(arrY.argmax(axis=1))

print(arrY.argsort(axis=0))
print(arrY.argsort(axis=1))
# 3> Reading arrays from disk,either from standard or custom formats.

# 4> Creating arrays from raw bytes through the use of strings  or buffers.

# 5> Use of special library functions(eg: random)