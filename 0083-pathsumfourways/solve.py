# read in
import copy


f = open('0081-pathsumtwoways/p081_matrix.txt','r')
lines = f.readlines()
grid = []
for l in lines:
    l=l.split(",")
    grid.append(l)

for i in range(len(grid)):
    for j in range(len(grid)):
        grid[i][j] = int(grid[i][j])



blocking = copy.deepcopy(grid)
for i in range(len(grid)):
    for j in range(len(grid)):
        blocking[i][j] = 0




# We will so exceed maximum recursion depth. Other options?
def shortestpath(i,j,blocking):
    localmin = 0 # flag for failure
    #right
    if j+1 < len(grid):
        right =
    #left
    left =
    #up
    up =
    #down
    down =
    return localMin
