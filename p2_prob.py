#Introduction to Bioinformatics Assignment 4
#Purpose:Probability of Hamming Distance
#Your Name: Michael Thomas
#Date: 10/10/15

import math
import matplotlib.pyplot as plt

a = int(input("Enter length of sequences: "))
hamms=[]
probs = []
for i in xrange(0,int(a)):
    hamms.append(i)

for j in hamms:
    bicoef = (math.factorial(a))/(math.factorial(j)*(math.factorial(a-j)))
    perms = 4.0**a
    prob = bicoef/perms
    probs.append(prob)

pmn = min(probs)
pmx = max(probs)

plt.scatter(hamms,probs)
plt.axis([0,a,0,pmx + pmx*.25])
plt.xlabel('hamming distance')
plt.ylabel('probability')
plt.show()
