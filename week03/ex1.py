"""
Renata Koontz

SID: 861166139

Due: April 18, 2016 11:00 pm

Exercise 1
Week 3
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import pdb
import numpy.linalg as lin



##Variables
distance = 10.0 ##in cm
Epsilon = 8.854187817 ##C2/(N m2) constant
pi = 3.14159 ##pi
k = 1/(4*pi*Epsilon) ##constant k
separation = 10.0

q1 = 1.0 ##Coulombs
q2 = -1.0 ##Coulombs
side = 100.0
points = 100 
spacing = side/points #cm

x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2



#storing potentials
#Body
PotEn = np.empty([points, points], float)
#
##x = np.linspace(-50,50,100)
##y = np.linspace(-50,50,100)

for i in range(points):
    y=spacing*i
    for j in range(points):
        x = spacing*j
        r1 = math.sqrt((x - x1)**2 + (y - y1)**2)
        r2 = math.sqrt((x - x2)**2 + (y - y2)**2)
        PotEn[i,j] = ((k*q1)/(r1 + 1.**-4)) + ((k*q2)/(r2 + 1.**-4))


plt.imshow(PotEn, origin = "lower" ,extent = [0, side, 0, side])
plt.show()


##Derivative part

h = 1

bins = len(PotEn)
deriv_y = 0.0
deriv_x = 0.0

deriv = np.zeros([bins, bins])

#d/dy
for j in range(bins):
    for i in range(bins):

        if i < 99:
            deriv_y = (PotEn[j, i + 1] - PotEn [j, i])/(h)
            
        else:
            deriv_y = (PotEn[j, i] - PotEn[j, i-1])/(h)

        if j < 99:
            deriv_x = (PotEn[j + 1, i] - PotEn[j, i])/(h)
            
        else:
            deriv_x = (PotEn [j, i] - PotEn[j - 1, i])/(h)
        deriv[i,j] = math.sqrt(deriv_x**2 + deriv_y**2)
            
            
##Comparison
       
plt.imshow(deriv.T, origin = "lower" ,extent = [0, side, 0, side]) 
plt.show()      
DerivNump = np.gradient(PotEn)


##print 'Gradient: ', DerivNump
##print 'Derivative: ', deriv




##So far it looks right
