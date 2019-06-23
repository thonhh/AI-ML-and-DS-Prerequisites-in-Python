from scipy.stats import norm
#PDF: Probability density function evaluated at x
#Hàm mật độ xác suất được đánh giá tại x
# norm 1: tổng trị tuyệt đối các phần tử của vector
# norm 2: được định nghĩa là căn bậc hai của tổng bình phương các phần tử của nó.
# https://machinelearningcoban.com/2017/10/12/fundaml_vectors/#-norm-
norm.pdf(0)#0.3989422804014327
norm.pdf(0,loc=5,scale=10)#0.03520653267642995

import numpy as np
r = np.random.randn(10)
norm.pdf(r)
norm.logpdf(r)
#Cumulative distribution function evaluated at `x`
norm.cdf(r)
#-------------------------------------------------
r = np.random.randn(10)