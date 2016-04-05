"""
Renata Koontz

SID: 861166139

Due: April 5, 2016 11:00 pm

Exercise 3a - A Ball Drops from a Very Tall Tower part b
Week 1
"""
import numpy as np
import math
import matplotlib.pyplot as plt

##variables
vMax = 0 ##maximun velocity
vMin = 0 ##minimum velocity
g = 9.81 ##gravity constant
time = 0
bins = 10
i = 0
incrementsTime = 0
incrementsVelocity = 0
timeArray = []
velocityArray = []

height = 800 ##height of building


##input
vMax = float(input("Enter the maximum velocity: "))
vMin = float(input("Enter the minimum velocity: "))

##calculations

bins = (vMax - vMin)/10.0

for i in range(int(bins)):
    increment = vMin + bins*i
    velocityArray.append(increment)
print velocityArray

for i in range(int(bins)):
    increment = (velocityArray[i] - vMin)/(g)
    timeArray.append(increment)
print timeArray

plt.plot(velocityArray, timeArray)
plt.xlabel("Velocity, v_in")
plt.ylabel("Time, t")
file = open('timeVsvelocity.dat','w')
for i in range(int(bins)):
    txt = str(timeArray[i]) + '\t' + str(velocityArray[i]) + '\n'
    file.write(txt)
    
file.close()

plt.show()



    










