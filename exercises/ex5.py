# https://deeplearningcourses.com/c/deep-learning-prerequisites-the-numpy-stack-in-python
# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python

from __future__ import print_function, division
from future.utils import iteritems
from builtins import range, input
# Note: you may need to update your version of future
# sudo pip install -U future

import numpy as np
import matplotlib.pyplot as plt



def is_symmetric1(A):#Hàm từ thư viện numpy
  return np.all(A == A.T)


def is_symmetric2(A):#Hàm kiểm tra đối xứng làm từ đầu
  rows, cols = A.shape
  if rows != cols:
    return False

  for i in range(rows):
    for j in range(cols):
      if A[i,j] != A[j,i]:
        return False

  return True


def check(A, b):
  print("Testing:")
  print(A)
  assert(is_symmetric1(A) == b)
  assert(is_symmetric2(A) == b)


# test the functions
A = np.zeros((3, 3))#Kiểm tra với ma trận 0
check(A, True)

A = np.eye(3) #Tạo ma trận đơn vị 3x3
check(A, True)

A = np.random.randn(3, 2)#Tạo ma trận ngẫu nhiên
A = A.dot(A.T)
check(A, True)

A = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
check(A, True)


# Các trường hợp kiểm tra không đối xứng
A = np.random.randn(3, 2)
check(A, False)

A = np.random.randn(3, 3)
check(A, False)

A = np.arange(9).reshape(3, 3)
check(A, False)

