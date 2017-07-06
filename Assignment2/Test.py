import sys
import math
import os
xes = []
ys = []
i=0
j=0
c= []
d= []
with open('point_sets1.txt') as f:
     for line in f:
         x, y = line.split()
         xes.append(x)
         ys.append(y)

for i in range(len(xes)):
    print(xes[i],ys[i])

#for i in range(len(xes)):
 #   d[i] = math.sqrt(math.pow( float(xes[i]) - float(xes[i+1]), 2) + math.pow( float(ys[i]) - float(ys[i+1]), 2))
  #  print(d[i])
    

   