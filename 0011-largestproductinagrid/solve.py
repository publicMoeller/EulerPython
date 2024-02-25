
# read in
f = open('0011-largestproductinagrid/grid.txt','r')
lines = f.readlines()
grid = []
for l in lines:
    l=l.split()
    grid.append(l)



# cast to int and print
for i in range(len(grid)):
    for j in range(len(grid)):
        grid[i][j] = int(grid[i][j])

for i in grid:
    print(i)

print(len(grid))
print(len(grid[0]))
# do the actual job
local = 0
maximum = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        
        if i+3 < len(grid): # to the 'right'
            local = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
            if local > maximum:
                maximum = local
            local = 0
        if j+3 < len(grid): # 'down'
            local = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
            if local > maximum:
                maximum = local
            local = 0
        if (i+3 < len(grid)) and (j+3 < len(grid)): # 'diagonal'
            local = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            if local > maximum:
                maximum = local
            local = 0
        if (i+3 < len(grid)) and (j-3 < len(grid)): # 'other diagonal'
            local = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
            if local > maximum:
                maximum = local
            local = 0

print(maximum)
