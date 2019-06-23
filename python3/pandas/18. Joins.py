import pandas as pd
t1 = pd.read_csv('numpy_class/python3/pandas/table1.csv')
t2 = pd.read_csv('numpy_class/python3/pandas/table2.csv')
m=pd.merge(t1,t2, on="user_id")
t1.merge(t2, on="user_id")