# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/lecture/5853246#overview

import numpy as np

a = np.array([1,2])
b = np.array([2,1])

dot=0
for e,f in zip(a,b):#trả về một đối tượng zip, là một iterator dạng danh sách
    dot+=e*f
print(dot)#4
#a*b #array[2,2]
#np.sum(a*b) #4
#(a*b).sum #4

#np.dot(a,b)#4
#a.dot(b)#4
#b.dot(a)#4
mag = np.sqrt((a*a.sum()))#array([1.73205081, 2.44948974])
amag = np.sqrt((a*a).sum()) #magnitude: độ lớn
amag1 = np.linalg.norm(a) #'Lin'ear 'alg'ebra basics
cosangle = a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b))
angle =  np.arccos(cosangle)
