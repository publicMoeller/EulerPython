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


pathsums = copy.deepcopy(grid)
for i in range(len(grid)):
    for j in range(len(grid)):
        pathsums[i][j] = 0

for i in range(len(grid)):
    for j in range(len(grid)):
        if i == 0:
            if j == 0:
                pathsums[i][j] = grid[i][j]
            else:
                candidate = grid[i][j] + pathsums[i][j-1]
                if candidate < pathsums[i][j] or pathsums[i][j]==0:
                    pathsums[i][j] = candidate
        else:
            if j == 0:
                candidate = grid[i][j] + pathsums[i-1][j]
                if candidate < pathsums[i][j]or pathsums[i][j]==0:
                    pathsums[i][j] = candidate
            else:
                candidate = grid[i][j] + pathsums[i][j-1]
                if candidate < pathsums[i][j]or pathsums[i][j]==0:
                    pathsums[i][j] = candidate
                candidate = grid[i][j] + pathsums[i-1][j]
                if candidate < pathsums[i][j]or pathsums[i][j]==0:
                    pathsums[i][j] = candidate




print(pathsums[-1][-1])