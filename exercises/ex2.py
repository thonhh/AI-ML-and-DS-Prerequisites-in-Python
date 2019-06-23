# https://deeplearningcourses.com/c/deep-learning-prerequisites-the-numpy-stack-in-python
# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python

from __future__ import print_function, division
from future.utils import iteritems
from builtins import range, input
# Note: you may need to update your version of future
# sudo pip install -U future

import numpy as np
import matplotlib.pyplot as plt
'''
In probability theory and statistics, a collection of random variables is independent and identically distributed if each random variable has the same probability distribution as the others and all are mutually independent. This property is usually abbreviated as i.i.d. or iid or IID.
'''
def sampleY(n=1000):
  # draw n samples from uniform dist.
  X = np.random.random(n)#Phát sinh bộ dữ liệu mẫu cho X
  Y = X.sum() # Hàm y làm hàm tổng của các giá trị trong X
  return Y


# now draw N Y's
N = 1000 #N số lượng biến số trong X
Y_samples = np.zeros(N) #Khởi tạo giá trị 0 cho toàn bộ mảng Y_sample
for i in range(N): #Thực hiện lặp N lần
  Y_samples[i] = sampleY() # Với mỗi lần lặp thứ i: Tính giá trị hàm Y (chính là hàm phân phối Gaussian)


# now plot the Y_samples
# Các giá trị của hàm Y (phân phối gaussian sẽ có hình cong như cái chuông
plt.hist(Y_samples, bins=20)
plt.show()