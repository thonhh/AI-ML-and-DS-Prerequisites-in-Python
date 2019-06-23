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
#------------------------------------------------------------------
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
X1.head()
'''
           0          1           2
0  17.930201  94.520592  320.259530
1  97.144697  69.593282  404.634472
2  81.775901   5.737648  181.485108
3  55.854342  70.325902  321.773638
4  49.366550  75.114040  322.465486
'''

#------------------------lấy giá trị tại 1 tọa độ dòng cột
X[0,0]#17.9302012052
M = X1.as_matrix()
type(M)#<class 'numpy.ndarray'>

#------------------------tại cột 0: tất cả các dòng rows (100 dòng) ->...Name: 0, Length: 100, dtype: float64
X1[0]

type(X1[0])#<class 'pandas.core.series.Series'>

#------------------------tại dòng 0: lấy các giá trị của các cột
X1.iloc[0]
X1.ix[0]##tại dòng 0: lấy các giá trị của các cột
'''
loc gets rows (or columns) with particular labels from the index.
iloc gets rows (or columns) at particular positions in the index (so it only takes integers).
ix usually tries to behave like loc but falls back to behaving like iloc if a label is not present in the index.
'''

type(X1.ix[0])#4<class 'pandas.core.series.Series'>
#------------------------tại cột 0 và cột 2: lấy hết dữ liệu của chúng
X1[[0,2]]
#------------------------tại cột 0 lọc ra các giá trị có giá trị < 5 -> liệt kê hết dữ liệu còn lại của Frame theo các giá trị ở cột 0 có giá trị < 5
X1[ X1[0] < 5 ]
'''
           0          1           2
5   3.192702  29.256299   94.618811
44  3.593966  96.252217  293.237183
54  4.593463  46.335932  145.818745
90  1.382983  84.944087  252.905653
99  4.142669  52.254726  168.034401
'''
X1[0]<5
'''
0     False
.........
99     True
Name: 0, Length: 100, dtype: bool

'''
type(X1[0]<5)#<class 'pandas.core.series.Series'>