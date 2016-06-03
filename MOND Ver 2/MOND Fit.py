# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:18:20 2016

@author: RenTh
"""

import numpy as np
import math
import scipy
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d 
import random

data = np.loadtxt('UGC 128 - Obs Vel.txt')
data1 = np.loadtxt('UGC 128 - Star Vel.txt')
data2 = np.loadtxt('UGC 128 - Gas Vel.txt')
errorBars = np.loadtxt('UGC 128 - Error Bars.txt')

##FUNCTIONS-------------------------------------------------------------------

##Evaluating Fit---------------------------------------------------
def f(starVel,gasVel,aConstant, radius):
    
    gN = ((gasVel)**2/(radius + 0.0000001)) + ((starVel)**2/(radius + 0.0000001))
    
    discri = gN**4 + 4*(aConstant*gN)**2
    
    discrim = math.sqrt(discri)
    
    y = (.5)*(gN**2 + discrim)
    
    g = math.sqrt(y)
    
    vFit = radius*g
    
    velFit = math.sqrt(vFit)
    
    return velFit
    
##density dark matter---------------------------------------
def rho1DM(rs, rho1, r):

    density = rho1/(((r + 0.0001)/rs)*(1+((r + 0.0001)/rs))**2)
    return density
##VelocityNFW-----------------------------------------------
def vNFW(rs, rho1,gg, r):
    
    vel = 4*math.pi*gg*rho1*rs**2*(rs/r)*(math.log(r/rs+1)-((r/rs)/(r/rs + 1)))
    return vel
    
    
    
    
    
##MAIN BODY-------------------------------------------------------------------- 

##radius and vel of observed points-------------------------------
radiusObs = data[:,0]
ObsVel = data[:,1]
ErrorBar = errorBars[:,1]
error = []

radiusObsKM = [x * (3.086e16) for x in radiusObs]


##radius and vel of gas points-----------------------------------
radiusGas = data1[:,0]
GasVel = data1[:,1]

##radius and vel of star points----------------------------------
radiusStar = data2[:,0]
StarVel = data2[:,1]

##Declaring constants-------------------------------------
##1000 points
N = 1000
##constant
ao = 1.2e-13
G = 6.67408e-20 ##km^3/(kg*s^2)
GG = 4.301*10**(-6)

chai = []

radiusDM = []
DMdensity = []

Q = 10

xPts = np.linspace(radiusObs[0], radiusObs[-1], N)
Rhosx = np.linspace(2.59612*10**6, 6.6*10**6, N)

InterPolateGas = interp1d(radiusGas, GasVel)
yNew = InterPolateGas(xPts)


InterPolateStar = interp1d(radiusStar, StarVel)

GasVelNew = []
StarVelNew = []

for i in range(len(radiusObs)):
    
    radGas = InterPolateGas(radiusObs[i])
    GasVelNew.append(radGas)
    
    radStar = InterPolateStar(radiusObs[i])
    StarVelNew.append(radStar)
##Fitting the velocities ----------------------------------------------- 
velFit = []

   
for i in range(len(radiusObs)):
    y = f(StarVelNew[i], GasVelNew[i], ao, radiusObsKM[i])
    velFit.append(y)
 
InterPolateFit = interp1d(radiusObs, velFit)
yNew = InterPolateFit(radiusObs)

error = [x * (1.0) for x in ErrorBar]
#print 'Error: ', error

##creating chai - squared distribution----------------------------CHI MODEL
#print len(radiusObs)
#print 'velFit: ', velFit
#print 'ObsVel:', ObsVel
for i in range(len(radiusObs)):

    y = (ObsVel[i] - velFit[i])**2/(error[i])**2
    chai.append(y)

#print 'chai: ', chai
chaiSort = []
for i in sorted(chai):
    chaiSort.append(i)
q = np.sum(chai)
#print q
#print chaiSort
#print 'sort: chaiSort: ', chaiSort
#print 'chai: ', np.sum(chai)
##dark matter density profile-------------------------------------DARK MATTER
k = 0.5

#rs1 = 5.7
#rs1 = 45.4
rs1 = 13.9
#rs1 = 9.0
rhos1 = 4.4*10**6

radDM2 = []
DMden = []
density2 = 0

for i in range(len(radiusObs)):
    radiusDM.append(radiusObs[i])
    density = rho1DM(rs1,rhos1,radiusObs[i])
    d = density
    DMdensity.append(d)
    
i = 0  
for i in range(50):
    
    radDM2.append(i)
    density2 = rho1DM(rs1,rhos1,i)
    DMden.append(density2)
    
    
    
DMdensity2 = np.array(DMdensity)
radiusDM2 = np.array(radiusDM)

DMdensity3 = np.array(DMden)
radiusDM3 = np.array(radDM2)

#print 'density #1: ', DMdensity3
#print 'radius#1: ; ', radiusDM3

#print 'density: ', DMdensity2
#print 'radius: ', radiusDM2

#InterpolateDMdensity = interp1d(radiusDM2, DMdensity2)
logDM = []
for i in range(len(radiusObs)):
    y = math.log(math.log(DMdensity2[i]))
    logDM.append(y)
InterpolateChai = interp1d(logDM, chai)
InterpolateChai2 = interp1d(logDM, chai, kind = 'cubic')
xnew = np.linspace(logDM[0], logDM[-1], num = 100)
InterpolateDMdensity = interp1d(radiusDM2, DMdensity2)

##Integrating density & Monte Carlo-------------------------------------------
'''
GG = 4.301*10**(-6)

count = 0
N = 10000
for i in range(N):
    x = random.uniform(logDM[0],logDM[-1])
    #print 'x: ', x
    y = random.uniform(chaiSort[0], chaiSort[-1])
    #print 'y: ', y
    if y < InterpolateChai(x):
        count += 1.0
I = 4* math.pi*(count/N)
#print 'Integral: ', I
#print 'Count: ', count

print 'True area: ', scipy.integrate.trapz(logDM, chaiSort, 0.5)

count = 0
N = 1000
##print DMdensity2
for i in range(N):
    
    x = random.uniform(radiusDM2[0],radiusDM2[-1])
    #print 'x: ', x
    y = random.uniform(DMdensity2[0], DMdensity2[-1])
    #print 'y: ', y
    if y < InterpolateDMdensity(x):
        count += 1
Q = (2*138**2)/(8*math.pi*GG*(2.1)**2)*(4*math.pi*count/N)
print 'Integral 2 : ', Q
print 'Count 2 : ', count

MassHalo = scipy.integrate.trapz(DMdensity2, radiusDM2)
MassHalo = MassHalo*(2*138**2)/(8*math.pi*GG*(2.1)**2)*(4*math.pi)

MassHalo2 = scipy.integrate.trapz(DMdensity3, radiusDM3)
MassHalo2 = (4*math.pi)*MassHalo2
#MassHalo2 = MassHalo2*(2*138**2)/(8*math.pi*GG*(2.1)**2)*(4*math.pi)
    
print 'True area: ', MassHalo
print 'Other area: ', MassHalo2
'''
##Calcuting the velocityNFW for testing purposes-------------------------------
count = 0
chiKeep = []
for k in range(N):
    
    velNFW = []
    for i in range(len(radiusObs)):
        vel = vNFW(rs1,Rhosx[k],GG,radiusObs[i])
        velNFW.append(vel)
#print 'velNFW: ', velNFW



##Calculating the velocity fit of CDM -----------------------------------------

##V_total**2 = V_b**2 + V_Halo**2
##V_b**2 = V_star**2 + V_gas**2
##V_halo**2 = 

    V_halo = []
    V_b = []
    V_total = []
    v_temp = []
    MassSolar = 1.98892*10**30 ##kg
    MassHalo = 6.69463*10**10
#MassHalo = 2.21026*10**11
#MassHalo = scipy.integrate.trapz(DMdensity2, radiusDM2)
#MassHalo1 = MassHalo*(2*(138**2))/(8*math.pi*GG*(2.1)**2)*(4*math.pi)

    for i in range(len(radiusObs)):
        Vhalo = (G*MassHalo)/(radiusObs[i]) ##V_Halo^2 = GM_halo/r
        V_halo.append(Vhalo)
   
    
    StarVelNew2 = np.array(StarVelNew)
    GasVelNew2 = np.array(GasVelNew)   
    for i in range(len(radiusObs)):
        Vbaryon = InterPolateGas(radiusObs[i])**2 + InterPolateStar(radiusObs[i])**2
    #Vbaryon = StarVelNew2[i]**2 + GasVelNew2[i]**2
        V_b.append(Vbaryon)
 
    for i in range(len(radiusObs)):
       Vtotal = velNFW[i] + V_b[i]
       Vtotal2 = math.sqrt(Vtotal)
       V_total.append(Vtotal2)
    
    
    StarVelNew2 = np.array(StarVelNew)
    GasVelNew2 = np.array(GasVelNew)  

##chi distribution DARK MATTER----------------------------------------------
    chi2 = []
    for i in range(len(radiusObs)):

        y = (ObsVel[i] - V_total[i])**2/(error[i])**2
        chi2.append(y)

    #print 'chai: ', chi2
    chaiSort = []
    for j in sorted(chi2):
        chaiSort.append(j)

#print 'sort: chaiSort: ', chaiSort
    #print 'chai: ', np.sum(chi2)
    
    q = np.sum(chaiSort)
    chiKeep.append(q)
    count += 1

#print q 
#print chaiSort   
#print count
#print chiKeep


#print len(chiKeep)
#print len(Rhosx)



  
#print 'StarVel: ', StarVelNew2
#print 'GasVel: ', GasVelNew2
#print 'V_total: ', V_total
#print 'vFit: ', velFit
#print 'V_b: ', V_b
#print 'V_halo: ', V_halo
#print 'vNFW: ', velNFW
    



##print ObsVel
##print logDM

##finding the minima using the golden ratio--------------------------------

accuracy = 1e-6
z = (1+math.sqrt(5))/2
x1 = Rhosx[0]
x4 = Rhosx[-1]

x2 = x4 - (x4 - x1)/z
x3 = x1 + (x4 - x1)/z

#initial values of the functions at the four points
InterpolateChi = interp1d(Rhosx, chiKeep)
InterpolateChi2 = interp1d(Rhosx, chiKeep, kind = 'cubic')

f1 = InterpolateChi(x1)
f2 = InterpolateChi(x2)
f3 = InterpolateChi(x3)
f4 = InterpolateChi(x4)

while x4 - x1 > accuracy:
    if f2 < f3:
        x4,f4 = x3,f3
        x3,f3 = x2,f2
        x2 = x4 - (x4 - x1)/z
        f2 = InterpolateChi(x2)
    else:
        x1,f1 = x2,f2
        x2,f2 = x3,f3
        x3 = x1 + (x4 - x1)/z
        f3 = InterpolateChi(x3)

bestDensity = 0.5*(x1 + x4)        
print 'The minimum falls at ', 0.5*(x1 + x4)
##print 'LogDM: ', logDM
##print chai
##Using best fit compute CDM--------------------------------------------------
velNFW = []
for i in range(len(radiusObs)):
    vel = vNFW(rs1,bestDensity,GG,radiusObs[i])
    velNFW.append(vel)


V_halo = []
V_b = []
V_total = []
v_temp = []
MassSolar = 1.98892*10**30 ##kg
##MassHalo = 6.69463*10**10
#MassHalo = 2.21026*10**11
#MassHalo = scipy.integrate.trapz(DMdensity2, radiusDM2)
#MassHalo1 = MassHalo*(2*(138**2))/(8*math.pi*GG*(2.1)**2)*(4*math.pi)


for i in range(len(radiusObs)):
    Vhalo = (G*MassHalo)/(radiusObs[i]) ##V_Halo^2 = GM_halo/r
    V_halo.append(Vhalo)

StarVelNew2 = np.array(StarVelNew)
GasVelNew2 = np.array(GasVelNew)   
for i in range(len(radiusObs)):
    Vbaryon = InterPolateGas(radiusObs[i])**2 + InterPolateStar(radiusObs[i])**2
    #Vbaryon = StarVelNew2[i]**2 + GasVelNew2[i]**2
    V_b.append(Vbaryon)
 
for i in range(len(radiusObs)):
    Vtotal = velNFW[i] + V_b[i]
    Vtotal2 = math.sqrt(Vtotal)
    V_total.append(Vtotal2)
    
    
StarVelNew2 = np.array(StarVelNew)
GasVelNew2 = np.array(GasVelNew)



plt.scatter(radiusGas,GasVel)
plt.scatter(radiusStar,StarVel)
plt.scatter(radiusObs,ObsVel)
plt.plot(radiusObs, V_total)
plt.plot(radiusObs, yNew, '--')
plt.xlim(0,radiusObs[-1]+.5)
plt.ylim(0,ObsVel[-1]+50.0)
plt.show()
#plt.loglog(radiusDM2, DMdensity2)
#plt.xlim(0.5,50)
#plt.show()
#plt.loglog(radiusDM3, DMdensity3)
#plt.show()

plt.scatter(Rhosx, chiKeep)
plt.plot(Rhosx, InterpolateChi(Rhosx))
plt.show()
