import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

A = pd.read_csv('numpy_class/python3/3. MatPlotlib/data_1d.csv', header=None).as_matrix()
x = A[:,0]#lấy tất cả các giá trị tại cột 0 cho biến x
y = A[:,1]#lấy tất cả các giá trị tại cột 1 cho biến y
plt.scatter(x,y)
plt.show()


#kẻ đường thẳng giữa các điểm
x_line = np.linspace(0,100,100)
y_line = 2*x_line+1
plt.scatter(x,y)
plt.plot(x_line,y_line)
plt.show()
# đồ thị tần suất
plt.hist(x)
plt.show()
# Biểu đồ his to gram
R = np.random.randn(10000)
plt.hist(x)
plt.show(
    R = np.random.random(10000)
)

R = np.random.randn(10000)
plt.hist(R,bins=20)
plt.show()

#Biểu đồ
y_actual = 2*x + 1
residual =y - y_actual
plt.hist(residual)
plt.show()

