

import math

num = 1000
done = 0
# range is maximal, because are guaranteed 
# uniqueness and will just break
for a in range(1,num):
    if (done):
        break
    for b in range(1,num):
        if (done):
            break
        c = math.sqrt(a*a+b*b)
        if (a+b+c == num):
            done = [a,b,int(c)]

print("Triple: ",done)
print("Product: ",done[0]*done[1]*done[2])