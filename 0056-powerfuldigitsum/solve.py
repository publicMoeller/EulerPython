
def digitsum(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total


maximum = 0
for a in range(1,100):
    for b in range(1,100):
        candidate = digitsum(pow(a,b))
        if candidate > maximum:
            maximum = candidate
            maxA = a
            maxB = b
            print(maximum, a, b)

print('Maximal digit sum is', maximum, 'at', maxA ,'pow', maxB )
