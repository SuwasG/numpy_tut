import numpy as np 
'''There are 5 general mechanisms for creating numpy arrays :
1.Conversio from other Python structures(lists,tuples).
2.Intrinsic numpy array creation objects(eg;arange,ones,zeros ,etc.)
3.Reading arrays from disk ,either from standard or custom formats.
4.Creating arrays from raw bytes through the use  of strings or buffers .
5.Use of special library functions.(eg: random)'''

# 1.Conversion from other python structures
np_array_from_tuples=np.array((((('t','u','p','l','e','s')))))
print(np_array_from_tuples)
print(type(np_array_from_tuples))

np_array_from_lists=np.array([['l','i','s','t','s']])
print(np_array_from_lists)

print(np_array_from_tuples.ndim)
print(np_array_from_lists.ndim)

#2. Intrinsic numpy array creation objects(eg;arange,ones,zeros,etc.)
np_zeros=np.zeros((3,5))
print(np_zeros)

np_ones=np.ones((4,6))
print(np_ones)

np_arange=np.arange(3,10,2)    #start,end,step
print(np_arange)

np_linspace=np.linspace(1,5,8)  # equally linearly spaced 1 dekhi 5 sammako 8 ota numbers dinxa
print("Linspace",np_linspace)

emp=np.empty((4,5))     # 4,5 ko random values dinxa
print(emp)

emp_like=np.empty_like(np_linspace)
print(emp_like)

np_identity=np.identity(10)
print(np_identity)
print("Shape of np_identity",np_identity.shape)

reshape=np_identity.reshape(5,20)
print(reshape)
print("dimension of reshape",reshape.ndim)
print("Shape of reshape",reshape.shape)

ravel=reshape.ravel()
print(ravel)
print("Dimension of ravel",ravel.ndim)
print("Shape of ravel",ravel.shape)

y=[[3,4,5,6],[3,7,9,4],[2,7,4,9]]
array=np.array(y)
print(array.sum(axis=0))
print(array.sum(axis=1))

print("Transpose",array.T)

print(array.flat)
for item in array.flat:
    print(item)

print("dimension",array.ndim)

print("Size",array.size)

print("Nbytes",array.nbytes)    #kati bytes consume gareko xa

one_dim=np.array([3,5,8,2])
print("argmax",  one_dim.argmax())    #maximum element ko index dinxa

print(one_dim.argmin())

print(one_dim.argsort())    #sorted index dinxa ascending order of element


two_dim=np.array([[2,3,4,7],[3,7,0,9],[4,1,6,5]])
print(two_dim)
print("argmax-2 \n",two_dim.argmax())
print("argmin-2\n",two_dim.argmin())
print("argsort",two_dim.argsort())

print("two_dim",two_dim ,end=" \n\n")
print(two_dim.argmax(axis=0))     #harek column maa max value ko index dinxa
print(two_dim.argmax(axis=1))

print(two_dim.argsort(axis=0))
print(two_dim.argsort(axis=1))

print("ravel",two_dim.ravel())

print(two_dim.reshape(2,6))