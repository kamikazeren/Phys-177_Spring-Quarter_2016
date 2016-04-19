"""
Renata Koontz

SID: 861166139

Due: April 18, 2016 11:00 pm

Exercise 4
Week 3
"""
import math
import numpy as np

##Functions-----------------------------------------------------------------


def f(x):
    y = math.sin(math.sqrt(100*x))**2
    return y


##Body

a = 0.0
b = 1.0
bins = 2**14

h = (b-a)/bins

AbsoluteArea = 0.455833 ##wolfram alpha calculation

s = 0.5*f(a)+0.5*f(b)
I0 = h*s
I_N = 0.0
I = 0.0
 
for i in range(1,15):
    h = (b-a)/2**i
    s = 0.5*f(a)+0.5*f(b)
    for k in range(1,2**i):
        s += f(a+k*h)
        I0 = h*s
        I = round(I0, 6)
    E = abs((1.0/3.0)*(I0 - I_N))
    
    I_N = I0
    print 'Error: ',E, ', Bins: ', 2**i, ', Area: ', I0
print 'Real Area: ', AbsoluteArea

