import sys
import math
import os
minput =  [] # manuplated list
flist = []  # final list

list1 = []
count = 0
with open('point_sets1.txt', 'r') as f:
        for line in f:
            line = line.split()
            list1.append(line)
            print(line)
         
         
         
"""for line in list1:
    #print(line)
    minput = line.split()
    x,y = float(minput[0]) , float(minput[1])
    flist += [(x, y)] 
    print(flist)
"""    
    

    
    

sys.stdout = open("output.txt", "w")         
for list in list1:
   print(list, " cluster")
   