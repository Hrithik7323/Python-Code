# import pandas as pd
#
# #print(pd.__version__)
#
# arr=[0,1,2,3,4]
# s1=pd.Series(arr)
# print(s1)
#
# order=[1,2,3,4,5]
# s2=pd.Series(arr, index=order)
# print(s2)


import pandas as pd
import numpy as np
# # creating a random Ndarray
# n=np.random.randn(5)
# index=['a','b','c','d','e']
# s2=pd.Series(n, index=index)
# print(s2)

# creating series from dictionary
d={'a':1,'b':2,'c':3,'d':4,'e':5}
s3=pd.Series(d)
print(s3)

# you can modify the index of series
arr=[0,1,2,3,4]
s1=pd.Series(arr)
print(s1)
s1.index=['A','B','C','D','E']
print(s1)

slicing
print(s1[:3])
s4=s1.append(s1)
print(s4)

