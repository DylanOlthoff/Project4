#Dylan Olthoff
#CST-305
#Topic 4 Project 4: Degredation of Data Integrity
#Dr. Ricardo Citro

#Implementation

#solve the problem by hand in part 2
#develop functions based on the answers in part 2
#graph functions



# Packages used matplotlib numpy
import numpy as np
import matplotlib.pyplot as plt

# functions made from part two x1t x2t
def function(t):
    return np.exp((-1 / 20) * t)    # returns the value

def function2(t):
    return np.exp((-1 / 20) * t-1)    # returns the value

# creates the arrays for the values
ts = []         # tspace for x axis
xs = []         # tspace for y axis
ts2 = []         # tspace for x axis
xs2 = []         # xspace for y axis

ts = np.linspace(0, 150, 1000)
for i in ts :                   # create x values for all ts
    xs.append(function(i))          # add to x space
ts2 = np.linspace(0, 150, 1000)  # create a t space
for i in ts2 :                   # create x values for every value of t
    xs2.append(function2(i))          # append all the values of x into the xspace

plt.title("Function Analysis 1")          # set the title of the graph
plt.xlabel("t")                         # set the x label on the graph
plt.ylabel("x")                         # set the y label on the graph
plt.plot(ts, xs, 'r-', linewidth = 2)
plt.show()

plt.title("Function Analysis 2")          # set the title of the graph
plt.xlabel("t")                         # set the x label on the graph
plt.ylabel("x")                         # set the y label on the graph
plt.plot(ts2, xs2, 'r-', linewidth = 2)
plt.show()