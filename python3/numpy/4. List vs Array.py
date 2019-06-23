#https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/lecture/5853244#overview

import numpy as np
L=[1,2,3]
A = np.array(L)
for e in L:
    print(e)
A = np.array([1,2,3])
for e in L:
    print(e)
for e in A:
    print(A)
L.append(4)
L
A.append(4)
A
L=L+[5]
L
A=A+[4,5]
#------------------------ Giống nhau trong phép cộng
#Cộng 2 Danh sách List (theo kiểu tập hợp)
L2=[]
for e in L:
    L2.append(e+e)
L2
#Cộng 2 mảng array
A+A
#------------------------khác nhau trong phép nhân
# Nhân 2 các phần tử trong mảng array
2*A #
# Nhân đôi danh sách
2*L #->Nhân đôi danh sách
L**2 #lỗi
#-----------------------
#bình phương các giá trị của list
L2=[]
for e in L:
    L2.append(e*e)
L2
A**2 # ko lỗi ->bình phương các phần tử trong mảng
#------------
np.sqrt(A)
np.log(A)
np.exp(A)


