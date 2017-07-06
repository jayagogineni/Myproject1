points = [[1.5,2.5],[1.5,2.5], [3,5]]
x_coords = []
y_coords = []
def centroid(*points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    leng = len(points)
    centroid_x = sum(x_coords)/ leng
    centroid_y = sum(y_coords)/ leng
    print([centroid_x, centroid_y])

centroid(*points)


"""import sys
xes = []
ys = []
i=0
with open('point_sets1.txt') as f:
     for line in f:
         x, y = line.split()
         xes.append(x)
         ys.append(y)

for i in range(len(xes)):
   print(xes[i],ys[i])
   

sys.stdout = open("output.txt", "w")
for i in range(len(xes)):
    print (xes[i], ys[i])"""
