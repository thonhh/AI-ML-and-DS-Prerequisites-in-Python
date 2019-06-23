# https://deeplearningcourses.com/c/deep-learning-prerequisites-the-numpy-stack-in-python
# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python

# NOTE: in class, we assumed the current working directory
#       was linear_regression_class
#       in this file, we assume you are running the script
#       from the directory this file is in

import numpy as np

X = []
#1 mở file csv ->lấy ra từng dòng 1 gán cho biến line
for line in open('data_2d.csv'):
  # 1. dòng dữ liệu là số liệu từ biến line đã bỏ đi dấu phẩy
  row = line.split(',')
  # 1. gán kiểu float cho các giá trị ở biến row -> 2. chuyển các giá trị text đó thành list = hàm map() -> 3. gán list đó cho biến sample
  sample = list(map(float, row))
  # bổ sung sample = mỗi dòng vào danh sách X
  X.append(sample)

X = np.array(X)
X.shape# (100,3)
print(X)
