"""
Renata Koontz

SID: 861166139

Due: April 5, 2016 11:00 pm

Exercise 2 - Students' Final Grades

Week 1
"""
import numpy as np
import matplotlib.pyplot as plt

#Variables

Homework = np.array([10.0,10.0,8.0,9.5,3.0,9.0,0.0,6.0])
Midterm = np.array([10.0,10.0,10.0,10.0,8.0,5.0,10.0,7.0])
FinalProject = np.array([9.0, 10.0, 10.0, 6.0, 10.0, 6.0, 8.0, 9.0])
Averages = []
i = 0
failed = 0
outstanding = 0


#Body

##print Homework
##print Midterm
##print FinalProject

Average = .4*Homework + .2*Midterm + .4*FinalProject
for i in Average:
    print i

for i in Average:
    if i < 6.0:
        failed +=1
    elif i > 9.5:
        outstanding+=1

for i in Average:
    if i < 6.0:
        who = i
        print 'Number of failures: ', failed, ' with a grade of ', who
print 'Fraction of of outstandings', outstanding/8.0
f = open('students.dat','wt')
f.write('this is a test')
f.close()

l = np.array(Average)
plt.hist(Average, bins = 8)
plt.xlabel("grades")
plt.ylabel("# of students")
plt.show()
plt.savefig('plotOfStudents.png', format = 'png')
np.savetxt('StudentGrades.dat', l)


#print 'end program'