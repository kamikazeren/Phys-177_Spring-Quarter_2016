"""
Renata Koontz

SID: 861166139

Due: April 12, 2016 11:00 pm

Exercise 3 - Velocities
Week 2
"""
import numpy as np
import math

## Functions ----------------------------------------------------------------

##Polynomial function
def f(x):
    
    y = x**4 - 2*x + 1
    return y

## trapezoid function
def trap(N, initial, final, distance):
    xValues = []
    yValues = []
    Trap = []
    
    bins = N
    a = initial
    b = final
    h = distance
    q = 1
    ##get x values
    for i in range(bins+1):
        increment = a + i*h
        xValues.append(increment)
        
  ##get y Values  
    yValues.append(f(a))    
    for q in range(1, bins):
        increment = f(a + xValues[q])
        yValues.append(increment)
    yValues.append(f(b))
    
    for k in range (bins):
        Area = ((yValues[k]+yValues[k+1])/2)*h
        Trap.append(Area)

    
    Area = np.sum(Trap)
    
    return Area
##Simpson's rule function

def simp(N, initial, final, distance):
    
    xValues = []
    yValues = []
    Simp = []    
    
    bins = N
    a = initial
    b = final 
    h = distance
    
    ##get x values for xValues list
    for i in range(bins+1):
        increment = a + i*h
        xValues.append(increment)

    
    ##get y values for yValues list
    yValues.append(f(a))    
    for q in range(1, bins):
        increment = f(a + xValues[q])
        yValues.append(increment)
    yValues.append(f(b))

    
    ##Simpson's calculation
    Simp.append(((yValues[0])/3.0)*h)
    Simp.append(((yValues[-1])/3.0)*h)

    ##evens
    for k in range(1,bins,2):
        Area = ((4.0/3)*h)*(yValues[k])
        Simp.append(Area)
        
    ##odds
    for k in range(2,bins,2):
        Area = ((2.0*yValues[k])/3.0)*h
        Simp.append(Area)
        
    
    SimpArea = np.sum(Simp)
    return SimpArea

## Error analysis function for trapazoid  
def ErrorAnalysisTrap(Area20, Area10):
    I2 = Area20
    I1 = Area10    
    Error = (1.0/3.0)*math.fabs((I2 - I1))
    return Error

##Error analysis function for Simpson
def ErrorAnalysisSimp(Area20, Area10):
    I2 = Area20
    I1 = Area10    
    Error = (1.0/15.0)*math.fabs((I2 - I1))
    return Error

## Body ---------------------------------------------------------------------

bins = 20
a = 0
b = 2.0
h = (b-a)/bins

ActualResult = 4.4000 ##true result of area under polynomial


I2 = trap(bins, a, b, h) ##area of 20 bins
print 'Area of bins for trapazoid = 20: ', I2
bins = 10
h = (b-a)/bins
I1 = trap(bins, a, b, h)
print 'Area of bins for trapazoid = 10: ', I1

AnalysisTrap = ErrorAnalysisTrap(I2, I1)
print 'Error is: ', AnalysisTrap, ' for a trapezoid'

bins = 20
h = (b-a)/bins
A2 = simp(bins, a, b, h) ##area of 20 bins
print 'Area of bins for simpson = 20: ', A2
bins = 10
h = (b-a)/bins
A1 = simp(bins, a, b, h)
print 'Area of bins for simpson = 10: ', A1

print 'Error is: ', AnalysisSimp, ' for simpson'

print 'True result: ', ActualResult



