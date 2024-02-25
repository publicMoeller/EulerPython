
n = 1
step = 0
stepsize = 0
total = 1
while n < 1001*1001:
    if step%4 == 0 :
        stepsize += 2
    step += 1
    n = n + stepsize
    total += n

print(total)
