"""
Renata Koontz
SID: 861166139

Midterm - Exercise 4
Potential
"""

import numpy as np
import matplotlib.pyplot as plt

     
    

q = -1.0 ##coulombs?
k = 9.e9 ##Nm^2/c^2
V = 0

sides = 100 ##in cm
x1 = sides/2.0
y1 = sides/2.0
delta = 1.0
xDistance = []
yDistance = []
Potential = np.zeros((100,100))


for i in range(100):
    y = i*delta
    for j in range(100):
        x = i*delta
        r = math.sqrt((x - x1)**2 + (y - y1)**2 + 0.00000001)
        V = (k*q)/r
        
        Potential[i,j] = V
        

plt.imshow(Potential)
plt.savefig('problem4.png')
plt.close()
    
    








