import sys
import math
xes = []
ys = []
i=0
c = []
d = []
with open('point_sets1.txt') as f:
     for line in f:
         x, y = line.split()
         xes.append(x)
         ys.append(y)

#for i in range(len(xes)):
 #  print(xes[i],ys[i])
    
for i in range(len(xes)):
    print(float(xes[i]))
    print(float(ys[i]))
   # x1= math.pow( (float(xes[1]) - float(xes[i+1])), 2)
#    x2= math.pow( (float(ys[1]) - float(ys[i+1])), 2)
 #   y = float(x1)+ float(x2)
  #  d[i] = math.sqrt(float(y))
    
#for i in range(len(xes)):
#    d[i] = math.sqrt(math.pow( float(xes[1]) - float(xes[i+1]), 2) + math.pow( float(ys[1]) - float(ys[i+1]), 2))
#    print(float(d[i]))

    
    
sys.stdout = open("output.txt", "w")
for i in range(len(xes)):
    print (float(xes[i]), float(ys[i]), "cluster")

    