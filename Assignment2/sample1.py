import sys
import math
import itertools

x_coords = []
y_coords = []
minput = [] #manuplated list
lists = []
coords = []

#reading the file from the text file

with open('point_sets1.txt', 'r') as f:
        for line in f:
         line = line.split()
         line = map(float, line)
         lists.append(line)
         #print(line) # outerlists
         

# calculating the distance between the points

def dist(a1, a2):
    return math.sqrt((a2[0] - a1[0])**2 + (a2[1] - a1[1])**2)


min_dist = float("inf")
for a1, a2 in itertools.combinations(lists, 2):
    if dist(a1,a2) < min_dist:
        min_dist = dist(a1,a2)
        closest_coords = (a1,a2)

print(closest_coords, min_dist)

lists.append(closest_coords)
lists.remove(a1)
lists.remove(a2)




def centroid(*z):
    x_coords = [p[0] for p in z]
    y_coords = [p[1] for p in z]
    leng = len(z)
    centroid_x = sum(x_coords)/ leng
    centroid_y = sum(y_coords)/ leng
    return [centroid_x, centroid_y]
    

    

    
#print(lists)

#for a1, a2 in itertools.combinations(lists, 2):
 #   if len(a1) > 1:
        
        


 
sys.stdout = open("output.txt", "w")
for list in lists:
    print (list, "cluster")
 
 