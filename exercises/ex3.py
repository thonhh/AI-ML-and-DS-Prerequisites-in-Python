# https://deeplearningcourses.com/c/deep-learning-prerequisites-the-numpy-stack-in-python
# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python

from __future__ import print_function, division
from future.utils import iteritems
from builtins import range, input
# Note: you may need to update your version of future
# sudo pip install -U future

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# load in the data - Tải MINIST dataset
df = pd.read_csv('train.csv')#đọc file train.csv vào dataframe df
data = df.values #trích bảng giá trị vào mảng data (loại bỏ header)
X = data[:, 1:] # images trích lấy tất cả các dòng từ cột một cho đến các cột còn lại
Y = data[:, 0] # labels trích lấy các dòng tại cột 0

# loop through each label
for k in range(10):#Chạy 10 lần-với mỗi lần thực hiện công việc sau
  Xk = X[Y == k]# 1. Lấy tất cả dữ liệu có số hiệu k (= cách Lọc lại, xếp lại các số từ 0,9 các dữ liệu ký tự số từ 0 đến 9

  # mean image
  Mk = Xk.mean(axis=0) # 2. lấy giá trị trung bình của Xk

  # reshape into an image
  im = Mk.reshape(28, 28) # 3. Chuyển mảng 1 chiểu Xk thành mảng 2 chiều im

  # plot the image - hiển thị hình ảnh
  plt.imshow(im, cmap='gray')
  plt.title("Label: %s" % k)
  plt.show()
