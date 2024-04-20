import my_lib as mb
import math
import matplotlib.pyplot as plt
import csv

A = []
B = []
for i in range(14):
        A.append([])
        B.append([])
x=[0.0096,0.125,0.3895,0.731,0.818,0.934,1.05,1.218,1.53,2,3.66,4.23,6.5,9.9]

        
with open('bif.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
      for i in range(len(lines)):
          A[i].append(lines[i])
          B[i].append(x[i])
   
# print(A[0])


# plt.scatter(B[10],A[10],s=0.1)
# plt.show()
for i in range(14):
    plt.scatter(B[i],A[i],s=0.1)
# plt.savefig('bif.png')
plt.show()

