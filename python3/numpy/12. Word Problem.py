'''
Phí vào cổng tại một triển lãm nhỏ là:
 $1.5 cho trẻ
 $4.0 cho người lớn
 -> 1 ngày đẹp trời, tự nhiên có 22000 người vào triển lãm và tổng thu là $5050
 Thống kê xem có bao nhiêu người lớn và trẻ nhỏ
 --------------
 X1 = số trẻ
 X2 = số người lớn
 X1+X2=2200 người
 1.5X1+4X2=5050
'''

import numpy as np
A=np.array([[1,1],[1.5,4]])
b=np.array([2200,5050])
loi_giai = np.linalg.solve(A,b)
