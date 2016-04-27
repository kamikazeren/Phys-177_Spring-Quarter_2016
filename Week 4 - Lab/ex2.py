"""
Renata Koontz

SID: 861166139

Due: April 26, 2016 11:00 pm

Exercise 2
Week 4
"""
import math
import numpy as np
import numpy.linalg as lin
import array
import matplotlib.pyplot as plt
import pdb


accuracy = 1e-10

initial = 0.0
final = 1.0


def p(x):
   
    y=(924.0*x**6)-(2772.0*x**5)+(3150.0*x**4)-(1680.0*x**3)+(420.0*x**2)-(42.0*x) + 1.0
    return y

def q(y):      
        x=(5544.0*y**5)-(13860.0*y**4)+(12600.0*y**3)-(5040.0*y**2)+(840.0*y)-42.0
        return x
         

##Plotting polynomial

upoints = np.linspace(0,1,100)
xpoints = []
roots = []

for k in upoints:
    xpoints.append(p(k))

plt.plot(upoints, xpoints)
plt.show()
plt.savefig("Polynomial.png")

xpoints = []

for k in upoints:
    xpoints.append(q(k))

plt.plot(upoints, xpoints)
plt.show()

'''
while abs(final - initial)> accuracy:
    initial = final
    final = initial - (p(initial)/q(initial))

##print final
roots.append(final)

final = 0.3

while abs(final - initial)> accuracy:
    initial = final
    final = initial - (p(initial)/q(initial))

##print final
roots.append(final)
##print ' '

'''
for k in [float(j)/100 for j in range(5,100, 10)]:
    final = k
    while abs(final - initial) > accuracy:
        initial = final
        final = initial - (p(initial)/q(initial))

  ##  print ' '    
    ##print final
    roots.append(final)

roots = [float(round(n, 12)) for n in roots]
##print roots

##print ' '
newroots = []
for i in roots:
    if i not in newroots:
        newroots.append(i)
        
##print newroots
newroots.sort()        
##print newroots
for i in range(len(newroots)):
    print 'Root # ',i+1,' at ',newroots[i]


print 'End program'

