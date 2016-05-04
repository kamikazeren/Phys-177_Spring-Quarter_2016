# -*- coding: utf-8 -*-
"""
Renata Koontz
SID: 861166139

Midterm - Exercise 2
Fibonacci Sequence
"""

##Variables
x1 = 1.0
x2 = 1.0
increments = 2
xN = 0.0
##xN = x2 + x1
print 'first term: ', x1
print 'second term: ', x2

##twelth step
for i in range(10):
    
    xN = x1 +  x2
    ##print 'xN: ', xN
    x1 = x2
    x2 = xN
    increments += 1
    print increments, '# term', ' is ', xN
    
##99 and 100
increments = 2
x1 = 1.0
x2 = 1.0
print ' '
print 'first term: ', x1
print 'second term: ', x2
for i in range(98):
    
    xN = x1 +  x2
    ##print 'xN: ', xN
    x1 = x2
    x2 = xN
    increments += 1
    print increments, '# term', ' is ', xN
    
    
    
    

    
    
    
    
    


