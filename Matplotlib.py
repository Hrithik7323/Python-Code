from matplotlib import pyplot as plt

# #========== Bar Graph =============================

# plt.plot([1,2,3],[4,5,1])
# plt.show()

#### Getting Started
## Lets add tiltle and labels to our graph
# x = [4, 6, 8]
# y = [12, 16, 6]
#
# plt.plot(x,y)
# plt.title('info')
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# plt.show()

# ### Adding Style To Our Graph.
# from matplotlib import pyplot as plt
# from matpoltlib import style
# x=[4,6,9]
# y=[12,15,8]
#
# x1=[4,9,11]
# y1=[5,15,7]
#
# plt.plot(x,y,'r',label='LineOne',linewidth=5)
# plt.plot(x1,y1,'g',label="LineTwo",linewidth=5)
#
# plt.title('info')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
#
# plt.legend()
# plt.grid(True,color='k')
# plt.show()


# ### Bar Graph
# import matplotlib.pyplot as plt
#
# plt.bar([1,3,5,7,9],[5,7,9,4,6], label='Example One', color='b')
# plt.bar([2,4,6,8,10],[4,6,5,11,9], label="Example Two", color='g')
#
# plt.legend()
# plt.xlabel("Bar Number")
# plt.ylabel("Hight Number")
# plt.title("Bar Graph")
# plt.show()


# #============ Histogram ==================================
#
# import matplotlib.pyplot as plt
#
# population_age=[22,55,27,59,78,11,53,89,14,85,95,23,130,140,89,69,120,74,15,39,73,82,91]
# bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140]
#
# plt.hist(population_age,bins,histtype='bar', rwidth=0.8, label="Age Distribution")
#
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.title("Histogram of Population Age")
#
# plt.legend()
# #plt.grid(True, color='k')
# plt.show()


# #============ Scatter Plot ====================================
#
# import matplotlib.pyplot as plt
#
# x=[1,2,3,4,5,6,7,8]
# y=[5,2,6,4,3,8,2,1]
#
# plt.scatter(x,y, label="Skitscat", color="k")
#
# plt.xlabel("X-axis")
# plt.ylabel("Y-axix")
# plt.title("Scatter Plot")
# plt.legend()
# plt.show()

# #============== Stack Plot ===================================
#
# import matplotlib.pyplot as plt
#
# days=[1,2,3,4,5]
#
# sleeping=[7,8,6,11,7]
# eating=[2,3,4,3,2]
# working=[7,8,7,2,2]
# playing=[8,5,7,8,13]
#
# plt.plot([],[],color="m", label="Sleeping", linewidth=5)
# plt.plot([],[], color="c", label="Eating", linewidth=5)
# plt.plot([],[], color="r", label="Working", linewidth=5)
# plt.plot([],[], color="k", label="Playing", linewidth=5)
#
# plt.stackplot(days, sleeping, eating, working, playing, colors=["m","c","r","k"])
#
# plt.xlabel("X-axis")
# plt.ylabel("y-axis")
# plt.title("Stack Plot")
# plt.legend()
# plt.show()

# #============= Pie Chart ============================================
#
#
# import matplotlib.pyplot as plt
#
# slices=[7,2,3,13]
# activities=["Sleeping","Eating","Working","Playing"]
# cols=['c','m','r','b']
#
# plt.pie(slices,
#         labels=activities,
#         colors=cols,
#         startangle=90,
#         shadow=True,
#         explode=(0,0.1,0,0),
#         autopct='%1.1f%%'
#         )
# plt.title("Pie Chart")
# plt.show()

#============ Working With Multiple Plots ===================================
#Example 1
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()

#Example 2
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.subplot(222)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()
