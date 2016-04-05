"""
Renata Koontz

SID: 861166139

Due: April 5, 2016 11:00 pm

Exercise 3a - A Ball Drops from a Very Tall Tower part a
Week 1
"""
import numpy as np
import math


##initializing variables
vInitial = 0 ##in meters per second
vFinal = 0 ##final velocity
height = 800 ##fixed height of building in meters
g = 9.81 ##gravity constant in meters per second squared
time = 0

discr = 0 ##discriminant 

##(1/2)g*t^2 + vInitial*t + height
##a*t^2 + b*t + c


vInitial = float(input("What is the initial velocity? "))

discr = vInitial**2 + (4*.5*g*height)

if discr < 0:
    print 'No real solution'
    
elif discr == 0:
    time = (-vInitial + math.sqrt(discr))/(2*.5*g)
    print time

elif discr > 0:
    time = (-vInitial + math.sqrt(discr))/(2*.5*g)
    print 'Time: ', time
    


