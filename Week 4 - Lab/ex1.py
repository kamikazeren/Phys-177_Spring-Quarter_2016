"""
Renata Koontz

SID: 861166139

Due: April 26, 2016 11:00 pm

Exercise 1
Week 4
"""

x = 0.0
y = 0.0
a = 1.0
b = 2.0
p = 0.0

def f(x):
    y = (b)/(a + x**2)
    x = y*(a + x**2)
    
    return x
    
def q(x):
    
    return (x)/(1.0 + x**2)
##part a
    
for k in range(100):
    p = f(k)
    
print 'Fails to converge.'
x = 2.0
##part b
for k in range(100):
    x = q(x)
    print x


