"""
Renata Koontz

SID: 861166139

Due: April 18, 2016 11:00 pm

Exercise 2
Week 5
"""
import numpy as np
from numpy.fft import rfft,irfft
import matplotlib.pyplot as plt
import math
from scipy import signal
from cmath import exp, pi

def dft(y):
    
    
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

time = []
sunSpots = []
data = np.loadtxt('sunspots.txt')
time = data[:,0]
sunSpots = data[:,1]

cycleEstimate = 150
N = len(time)

plt.plot(time, sunSpots)
plt.show() 


coeff = rfft(sunSpots) 
print len(coeff)
print N/2         
nc = len(coeff)
plt.plot(np.arange(nc), np.abs(coeff))
plt.xlim(0,100)
plt.show()

xpoints = np.linspace(0,0.5,N/2+1)

print len(xpoints)
plt.plot(xpoints, np.abs(coeff))
plt.xlim(0,0.01)
plt.show()

print xpoints    
    