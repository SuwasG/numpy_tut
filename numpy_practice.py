import numpy as np 
pr=np.array([True,1,2])+ np.array([3,4,False])     # True is converted to 1 and False is converted to 0
print(pr)

x=["a",'b','c']
print(x)
print(type (x))
print(x[1])

np_array_of_x=np.array(x)
print(np_array_of_x)
print(type(np_array_of_x))
print(np_array_of_x[1])