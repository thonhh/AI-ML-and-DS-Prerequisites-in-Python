# https://deeplearningcourses.com/c/deep-learning-prerequisites-the-numpy-stack-in-python
# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python
# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/lecture/5853248#overview

from __future__ import print_function, division
from builtins import range
# Note: you may need to update your version of future
# sudo pip install -U future


import numpy as np
from datetime import datetime

a = np.random.randn(100) #tạo ra 100 số ngẫu nhiên rồi gán cho a
b = np.random.randn(100) #tạo ra 100 số ngẫu nghiên rồi gán cho mảng b
T = 100000 #lặp lại việc tính toán 100.000 lần

#hàm phép nhân 2 ma trận 1 chiều = mảng (chưa tối ưu)
def slow_dot_product(a, b):
  result = 0
  for e, f in zip(a, b):
    result += e*f
  return result

#t0 là thời gian bắt đầu chạy hàm tính toán
#dt1 là thời gian sau khi chạy hàm tính toán
t0 = datetime.now()
for t in range(T):
  slow_dot_product(a, b)
dt1 = datetime.now() - t0

#t0 là thời gian bắt đầu chạy hàm tính toán
#dt2 là thời gian sau khi chạy hàm tính toán
t0 = datetime.now()
for t in range(T):
  a.dot(b)
dt2 = datetime.now() - t0


#dt1/dt2 >1 thì thời gian của hàm tự làm ở dt1 > lớn hơn hàm của gói numpy tại dt2
print("dt1 / dt2:", dt1.total_seconds() / dt2.total_seconds())