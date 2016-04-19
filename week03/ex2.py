"""
Renata Koontz

SID: 861166139

Due: April 18, 2016 11:00 pm

Exercise 2 - Circuit and Matrices
Week 3
"""
import math
import numpy as np
import numpy.linalg as lin
import array
import matplotlib.pyplot as plt
import pdb

##Variables------------------------------------------------------------------

V1 = 0.0
V2 = 0.0
V3 = 0.0
V4 = 0.0
VPlus = 5.0
R = 0.0 ##Resistance probably not needed

##Equations------------------------------------------------------------------

A = np.array ([[4, -1, -1, -1],
            [-1, 4, -1, -1],
            [-1, -1, 4, -1],
            [-1, -1, -1, 4]], float)
v = np.array ([5, 0, 5, 0], float)
N = len(v)


# Guassian Elimination
for m in range(N):
    
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div
    
    for i in range(m+1, N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]
    

x = np.empty(N, float)
for m in range(N-1, -1, -1):
    x[m] = v[m]
    for i in range (m+1, N):
        x[m] -= A[m,i]*x[i]

print x

print lin.solve(A, v)

##Body-----------------------------------------------------------------------
