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

import pandas as pd
X1=pd.read_csv("data_2d.csv",header=None)
type(X1)#<class 'pandas.core.frame.DataFrame'>
X1.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 3 columns):
0    100 non-null float64
1    100 non-null float64
2    100 non-null float64
dtypes: float64(3)
memory usage: 2.4 KB
'''
X1.head()
X1.head(10)
