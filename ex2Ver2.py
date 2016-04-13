"""
Renata Koontz

SID: 861166139

Due: April 11, 2016 11:00 pm

Exercise 2 - Velocities
Week 2
"""
import numpy as np
import matplotlib.pyplot as plt

## functions ----------------------------------------------------------------
def trap(time1, vel1):
    xValues = time1
    yValues = vel1
    Trap = []

    bins = len(xValues)
    
    a = xValues[0]
    b = xValues[bins-1]
    
    h = (b-a)/bins
    for k in range (bins-1):
        Area = ((yValues[k]+yValues[k+1])/2)*h
        Trap.append(Area)

    print 'Area using Trapezoids: ', np.sum(Trap)
    
    
    ##Distance = np.sum(Trap)
    return Trap
    
##Simpson function
def simp(time1, vel1):
    xValues = time1
    yValues = vel1
    SimpArea=[]
    
    bins = len(xValues)

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
        
    
    
    print 'Area using Simpsons Rule: ', np.sum(SimpArea)  
    ##Distance = np.sum(SimpArea)
    return SimpArea
    
       
    

## main body ----------------------------------------------------------------
data = np.loadtxt('velocities.txt')
time = data[:,0]
vel = data[:,1]
distanceTrap = []
distanceSimp = []

print 'This program will read velocities and print '

##print 'time: ', time

##print 'velocities: ', vel

distanceTrap = trap(time, vel)
distanceSimp = simp(time, vel)

##Saving files ---------------------------------------------------------------
'''
textTrap = np.savetxt('DistanceTrap.txt', np.array(distanceTrap))
textSimp = np.savetxt('DistanceTrap.txt', np.array(distanceSimp))
'''

plt.subplot(2,1,1)
plt.plot(time, vel,)
time = time[0:100]
plt.subplot(2,1,2)
plt.plot(time, distanceTrap)
plt.show()

'''
ax1.plot(time, vel)
plt.ylabel("Velocity, v_in")
plt.xlabel("Time, t")
plot2 = plt.plot(time, distanceTrap)
plt.ylabel("Distance, v_in")
plt.xlabel("Time, t")
plt.show()
'''

