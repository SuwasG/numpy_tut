#Datacamp

import numpy as np
# print("practice-1")
# # extract b and d
# x=[['a','b'],['c','d']]
# # regular list of lists method
# print(x[0][1],x[1][1])      

# #numpy method
# np_array_x=np.array(x)
# print(np_array_x[:,1])

# print(x[1])

#2d np arrays can combine with single numbers ,with vectors and with other matrices.
print("practice-2")
np_matrix=np.array([[1,2],[3,4],[5,6]])
print(np_matrix*20)    
print(np_matrix+ np.array([10,10]))
# print(type(np.array([10,10])))
print(np_matrix+np_matrix)

