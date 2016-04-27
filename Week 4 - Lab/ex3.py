"""
Renata Koontz

SID: 861166139

Due: April 26, 2016 11:00 pm

Exercise 3
Week 4
"""
import math
import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt


def f(x):
    
    return x**2-(4*x*(math.sin(x)))+(2*math.sin(x))**2
    
    
accuracy = 1e-10
x1 = 2.2e10
x2 = 2.5e10
x3 = 0.0

while abs(x2 - x1) > accuracy:
    
    x3 = x2 - f(x2)*((x2-x1)/(f(x2)-f(x1)))
    x1 = x2
    x2 = x3
print 'Root #1: ', x3

x1 = 0.0
x2 = 2.0
x3 = 0.0

while abs(x2 - x1) > accuracy:
    
    x3 = x2 - f(x2)*((x2-x1)/(f(x2)-f(x1)))
    x1 = x2
    x2 = x3
print 'Root #2: ',  x3

    
