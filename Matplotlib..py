from matplotlib import pylab
print(pylab.__version__)



## USe Numpy to generate random date
import numpy as np
# import matplotlib.pylot as plt

x=np.linspace(0,10,25)
y=x*x+2
print(x)
print(y)

## It only takes 1 cammand to drow
pylab.plot(x,y,'r') # 'r' stand for red

pylab.subplot()
