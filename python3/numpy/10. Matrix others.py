#https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/lecture/5853256#overview

import numpy as np
A = np.array([[1,2],[3,4]])
#Compute the (multiplicative=nhân) inverse=nghịch đảo of a matrix
#linale = Linear algebra basics
Ainv = np.linalg.inv(A)
Nghich_dao_nhan_A = Ainv.dot(A)
A_nhan_nghich_dao = A.dot(Ainv)
Det_A = np.linalg.det(A)#Định thức (Determinant) là giá trị số thực có thể được tính ra từ mỗi ma trận vuông. Định thức của một ma trận vuông A được kí hiệu là det A hay |A|
duongcheo = np.diag(A)#diag(a1, a2,…, an) để chỉ một ma trận đường chéo cấp n có các phần tử trên đường chéo lần lượt là a1, a2, …, an
duongcheo1 = np.diag([1,2])

#----------------- outer product - inner product

a=np.array([1,2])
b=np.array([3,4])
outer_product = np.outer(a,b)
#---------
inner_product = np.inner(a,b)#11
a_dot_b = a.dot(b)#11
#---------
tong_duong_cheo = np.diag(A).sum()#5
tong_duong_cheo_voi_trace = np.trace(A)#5  Trong đại số tuyến tính, vết (tiếng Anh: trace) của một ma trận vuông A bậc nxn được xác định bằng tổng các phần tử trên đường chéo chính (đường nối từ góc trên bên trái xuống góc dưới bên phải) của A


#--------
X= np.random.randn(100,3)
cov1=np.cov(X)# Covariance (Hiệp phương sai) thể hiện mối quan hệ giữa hai biến với nhau, có thể là đồng biến (positive covariance) hoặc nghịch biến (negative covariance).
kich_co_mang_hai_chieu_cua_cov = cov1.shape
#Correlation  (Hệ số tương quan) là gì? Để thể hiện mối quan hệ giữa 2 biến là “mạnh” hay “yếu”, chúng ta sử dụng correlation thay cho covariance
cov_T = np.cov(X.T)
#trị riêng, vectơ riêng của ma trận (eigenvalues and eigenvectors)
'''
Số \lambda \in K  được gọi là giá trị riêng (gọi tắt là trị riêng – kí hiệu GTR) của ma trận A, nếu tồn tại một vectơ 0 \ne u \in K^n  sao cho: Au = {\lambda}u 
Khi đó vectơ u được gọi là vectơ riêng (VTR) của ma trận A ứng với giá trị riêng \lambda 
'''
vecto_rieng=np.linalg.eigh(cov1)