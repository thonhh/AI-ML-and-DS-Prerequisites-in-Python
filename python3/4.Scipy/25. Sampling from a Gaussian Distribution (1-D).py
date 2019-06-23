from scipy.stats import norm
#PDF: Probability density function evaluated at x
#Hàm mật độ xác suất được đánh giá tại x
'''
A normal continuous random variable. = 'norm'
The location (loc) keyword specifies the mean. The scale (scale) keyword specifies the standard deviation.
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html?highlight=norm#scipy.stats.norm
'''
norm.pdf(0)#0.3989422804014327 -> Giá trị của hàm Gaussian PDF tại x=0
norm.pdf(0,loc=5,scale=10)#0.03520653267642995 ->Giá trị của hàm Gaussian PDF tại x=0, mean=5, độ lệch chuẩn = 10

import numpy as np
r = np.random.randn(10)
norm.pdf(r)
norm.logpdf(r)
#Cumulative distribution function evaluated at `x`
norm.cdf(r)
#-------------------------------------------------
r = np.random.randn(10000)
import matplotlib.pyplot as plt
plt.hist(r,bins=100)
plt.show()

r = 10*np.random.randn(10000) + 5
plt.hist(r,bins=100)
plt.show()