import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,10)# Từ 0 đến 10 -> tạo ra 10 số
y = np.sin(x)
plt.plot(x,y)
plt.show()


plt.plot(x,y)
plt.xlabel("Time")
plt.ylabel("Some function of Time")
plt.title("Đồ thị hàm sin của tôi")
plt.show()

#Số lượng giá trị x càng nhiều, đồ thị càng mềm mại
# Từ 0 đến 10 -> tạo ra 100 số
x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y)
plt.show()