import matplotlib.pyplot as plt
import pandas as pd
import numpy as np




df = pd.read_csv('numpy_class/python3/3. MatPlotlib/train.csv')
df.shape
M = df.as_matrix()
im = M[0,1:]
im.shape
im = im.reshape(28,28)
plt.imshow(im)
plt.show()
M[0,0]
plt.imshow(im,cmap="gray")
plt.show()
plt.imshow(255-im,cmap='gray')
plt.show()