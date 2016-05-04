"""
Renata Koontz
SID: 861166139

Midterm - Exercise 3
Height
"""

##functions

import math
import numpy as np
import array
import  matplotlib.pyplot as plt


##function
def f(x):
    
    y = -3*x**5-24*x**4+3*x+10
    return y
    
def g(x):
    
    y = -15*x**4 - 96*x**3+3
    return y
    
    
    
    
##body
    
height = []
time = []
y = 0.0
b = 1.0
a = 0.0
increment = 0
bins = 20
h = (b - a)/bins




for i in [float(j)/100 for j in range(0, 105, 5)]:
    y = f(i)
    height.append(y)
    time.append(i)

    increment += 1
    
plt.plot(time, height)
plt.xlabel("time in Gr")
plt.ylabel("height of sun")
plt.show()

##Newton's method

accuracy = 1.e-10

x1 = 0.0
x2 = 1.0
xN = 0.0
pos = 0.0
N = 0


while abs(x2 - x1) > accuracy:
    
    x2 = x1
    xN = x1 - f(x1)/g(x1) 
    x1 = xN
    
    N+=1
    pos = abs(xN)
    
print 'Position of root is: ', pos
print 'It took ',N,' number of steps' 

























