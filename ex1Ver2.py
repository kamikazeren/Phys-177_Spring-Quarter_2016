"""
Renata Koontz

SID: 861166139

Due: April 12, 2016 11:00 pm

Exercise 1 - Simpson's Functions
Week 2
"""
import math
import numpy as np
import sys as s

##Function Defintions---------------------------------------------------------
def trap():
    xValues = []
    yValues = []
    Trap = []
    elements = float(input("Enter number of values: "))

    for i in range(0, int(elements)):
        xValues.append(float(input("Enter element: ")))
    print 'xValues: ', xValues
    
    for i in range(0, int(elements)):
        yValues.append(float(input("Enter element: ")))
    print 'yValues: ', yValues
    
    bins = int(elements)
    
    a = xValues[0]
    b = xValues[bins-1]
    
    h = (b-a)/bins
    for k in range (bins-1):
        Area = ((yValues[k]+yValues[k+1])/2)*h
        Trap.append(Area)

    print 'Trapezoid list: ', Trap
    print 'Area: ', np.sum(Trap)

def simp():
    
    xValues = []
    yValues = []
    SimpArea = []
    
    elements = float(input("Enter number of values: "))

    for i in range(0, int(elements)):
        xValues.append(float(input("Enter element: ")))
    print 'xValues: ', xValues
    
    for i in range(0, int(elements)):
        yValues.append(float(input("Enter element: ")))
    print 'yValues: ', yValues
    
    bins = int(elements)
    
    a = xValues[0]
    b = xValues[bins-1]
    h = (b-a)/bins

    SimpArea.append(((yValues[0])/3.0)*h)
    SimpArea.append(((yValues[-1])/3.0)*h)
    
##evens
    for k in range(1,bins,2):
        Area = ((4.0/3)*h)*(yValues[k])
    
        SimpArea.append(Area)
##odds
    for k in range(2,bins,2):
        Area = ((2.0*yValues[k])/3.0)*h
        
        SimpArea.append(Area)
        
    
    print 'Simp list: ', SimpArea
    print 'Area: ', np.sum(SimpArea)     
    
##Local Variables-------------------------------------------------------------


trap()
simp()
