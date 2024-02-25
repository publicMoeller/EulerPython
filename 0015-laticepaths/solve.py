
# We just create an array of path nodes and add up 
# all nodes that lead there.



# Number of nodes per side. Equals Blocks+1
dimensions = 21
pathsums = [[0 for x in range(dimensions)] for y in range(dimensions)] 

for i in range(0,dimensions):
    for j in range(0,dimensions):
        if i==0:
            if j==0:
                pathsums[i][j]=1
            else:
                pathsums[i][j]= pathsums[i][j-1]
        elif j==0:
            pathsums[i][j]= pathsums[i-1][j]
        else:
            pathsums[i][j]= pathsums[i-1][j]+pathsums[i][j-1]

        
      
print('Pathsums as matrix')
print('(looks bad for non-tiny numbers)')         
for line in range(dimensions):
    print(pathsums[line])


print('number of paths: ', pathsums[dimensions-1][dimensions-1])
