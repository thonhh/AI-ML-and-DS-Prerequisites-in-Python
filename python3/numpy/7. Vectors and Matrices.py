import numpy as np

M = np.array([[1,2],[3,4]])
L = [ [1,2],[3,4] ]
L[0]#[1, 2]
L[0][0]#1
M[0][0]#1
M2=np.matrix([ [1,2],[3,4]  ])
'''matrix([[1, 2],
           [3, 4]])'''
A=np.array(M2)
'''matrix([[1, 2],
           [3, 4]])'''
A.T
'''
array([[1, 3],
       [2, 4]])
'''
#Matrix chỉ là vector 2 chiều, hay là mảng 2 chiều mà thôi
