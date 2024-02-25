



f = open('p067_triangle.txt','r')
lines = f.readlines()


triangle = []
for l in lines:
    print(l)
    l=l.split()
    triangle.append(l)


# add maximum of all potenial predecessors to all fields
for i in range(1,len(triangle)):
    for j in range(i+1):
        if j==0:
            triangle[i][j]=int(triangle[i][j])+int(triangle[i-1][j])
        elif i==j:
            triangle[i][j]=int(triangle[i][j])+int(triangle[i-1][j-1])
        else:
            triangle[i][j]=max(int(triangle[i][j])+int(triangle[i-1][j]),int(triangle[i][j])+int(triangle[i-1][j-1]))

print(max(triangle[-1]))