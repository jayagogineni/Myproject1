
import sys
import math
import itertools

x_coords = []
y_coords = []
minput = [] #manupulated list
cluster = []
coords = []
k = 3 # to specify if number of clusters is 3 so that we can break the loop

#reading the file from the text file

with open('point_sets1.txt', 'r') as f:
        for line in f:
         line = line.split()
         line = map(float, line)
         cluster.append(line) # cluster is nothing but each individual cluster at first
#print(cluster) # outerlists
         
       
# calculating the distance between the points

# finding the euclidean distance
def dist(a1, a2):
    return math.sqrt((a2[0] - a1[0])**2 + (a2[1] - a1[1])**2)
    
# calculating the centroid         
def centroid(*z):
    x_coords = [p[0] for p in z]
    y_coords = [p[1] for p in z]
    leng = len(z)
    centroid_x = sum(x_coords)/ leng
    centroid_y = sum(y_coords)/ leng
    return [centroid_x, centroid_y]  
    
# finding the closest points using itertools    
min_dist = float("inf")
for a1, a2 in itertools.combinations(cluster, 2):
    if dist(a1,a2) < min_dist:
        min_dist = dist(a1,a2)
        closest_coords = (a1,a2)

print(closest_coords, min_dist)

# appending the list with the closest value pair cluster and removing the added pairs, so that we can make 
#all the clusters in just one list names cluster 
cluster.append(closest_coords)
cluster.remove(a1)
cluster.remove(a2)

# to print the data in output file
sys.stdout = open("output.txt", "w")
for list in cluster:
    print (list,    "cluster")
# for 2nd iterations
# let minimum distance be infinity at first so that we can easily store the min distance values and use to form the clusters
min_dist = float("inf")
for a1, a2 in itertools.combinations(cluster, 2):
# when the clusters hav only points    
    if len(a1) <= 2 and len(a2) <= 2 :
        if dist(a1,a2) < min_dist:
            min_dist = dist(a1,a2)
            closest_coords = (a1,a2)
            if len(cluster)==3:    # to stop the iterations as soon as we get 3 clusters
                break
# when there is one big cluster and one cluster with one point        
    elif len(a1) > 2 and len(a2) <= 2:
        a1 = centroid(*a1)
        if dist(a1,a2) < min_dist:
            min_dist = dist(a1,a2)
            closest_coords = (a1,a2)
            if len(cluster)==3:
                break
# when the two clusters have more than one              
    else :
        a1 = centroid(*a1)
        a2 = centroid(*a2)
        if dist(a1,a2) < min_dist:
            min_dist = dist(a1,a2)
            closest_coords = (a1,a2)
            if len(cluster)==3:
                break
    
    #print(closest_coords, min_dist)
    # we append the pairs to the 
    cluster.append(closest_coords)
    cluster.remove(a1)
    cluster.remove(a2)


#print(lists)

#for a1, a2 in itertools.combinations(lists, 2):
 #   if len(a1) > 1:
        
        
sys.stdout = open("output.txt", "w")
for list in cluster:
    print (list,    "cluster")
 
 