import numpy as np
A = np.array([[1,2],[3,4]])
b=np.array([1,2])
x=np.linalg.inv(A).dot(b)
x1=np.linalg.solve(A,b)