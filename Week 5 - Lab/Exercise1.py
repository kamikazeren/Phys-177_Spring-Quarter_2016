"""
Renata Koontz

SID: 861166139

Due: April 18, 2016 11:00 pm

Exercise 1
Week 5
"""
import numpy as np
from numpy.fft import rfft,irfft
import matplotlib.pyplot as plt
import math
from scipy import signal
from cmath import exp, pi

##Square Well function

def SineFunction(n, bins):
    
    y = math.sin((math.pi*n)/bins)*math.sin((20*math.pi*n)/bins)
    return y
        
def dft(y):
    
    
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

N = 1000
t = np.linspace(0, 1, N)
squareWell = signal.square(2*np.pi*t*1)
plt.plot(t, squareWell)
plt.ylim(-1.5,1.5)
plt.show()


c = []
coeff = rfft(squareWell)
z = irfft(coeff)
c = dft(squareWell)
nc = len(coeff)


plt.plot(np.arange(nc), np.abs(coeff))
plt.xlim(0,100)
plt.show()



t = np.linspace(-1,1,N)
sawtoothFunc = []
sineFunc = []

sawtoothFunc = signal.sawtooth(2*t*np.pi)
    
plt.plot(t, sawtoothFunc)
plt.show()
c = []
coeff = rfft(sawtoothFunc)
z = irfft(coeff)
c = dft(sawtoothFunc)
lc = len(coeff)
plt.plot(np.arange(lc), np.abs(coeff))
plt.show()


uPoints = np.linspace(0,1000,N)
for i in uPoints:
    sineFunc.append(SineFunction(i, N))
    
plt.plot(uPoints, sineFunc)
plt.show()
c = []
coeff = rfft(sineFunc)
z = irfft(coeff)
c = dft(sineFunc)

uPoints = np.linspace(0, 1000, 501)
plt.plot(uPoints, np.abs(c))
plt.xlim(0,100)
plt.show()


    
        
    

