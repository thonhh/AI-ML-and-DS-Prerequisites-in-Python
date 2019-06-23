import numpy as np

Z = np.zeros(10)
Z1 = np.zeros((10,10))
O = np.ones((10,10))
R = np.random.random((10,10))

#G = np.random.randn((10,10)) ->ko thể truyền tham số là một tuple (..)
'''
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "mtrand.pyx", line 1425, in mtrand.RandomState.randn
  File "mtrand.pyx", line 1555, in mtrand.RandomState.standard_normal
  File "mtrand.pyx", line 167, in mtrand.cont0_array
TypeError: 'tuple' object cannot be interpreted as an integer
'''
G=np.random.randn(10,10)
Gmean = G.mean()
Gvar = G.var()