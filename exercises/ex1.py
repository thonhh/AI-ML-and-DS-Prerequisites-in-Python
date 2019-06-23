# https://deeplearningcourses.com/c/deep-learning-prerequisites-the-numpy-stack-in-python
# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python

from __future__ import print_function, division
from future.utils import iteritems
from builtins import range, input
# Note: you may need to update your version of future
# sudo pip install -U future

import numpy as np
import matplotlib.pyplot as plt

A = np.array([
  [0.3, 0.6, 0.1],
  [0.5, 0.2, 0.3],
  [0.4, 0.1, 0.5]])

v = np.ones(3) / 3

num_iters = 25 #Tạo biến số để: Thực hiện 25 lần lặp
distances = np.zeros(num_iters) # Khởi tạo mảng rỗng
for i in range(num_iters):# Chạy vòng lặp
  v2 = v.dot(A) # Thực hiện nhân vecto với ma trận
  d = np.linalg.norm(v2 - v) #Tính khoản cách 2 vector bằng hàm norm
  distances[i] = d # Lưu khoảng cách vào mảng distance
  v = v2

plt.plot(distances)
plt.show()