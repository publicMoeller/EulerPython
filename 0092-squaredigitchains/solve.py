import math



def squareDigits(n):
    total = 0
    for i in str(n):
        total += int(i)**2
    return total

def reaches89(n):
    while True:
        n = squareDigits(n)
        if n == 89:
            return True
        if n == 1:
            return False
    


# We could save almost all processing time by remembering every numbers terminus and look up but this will do
total89 = 0
for i in range(1,10000000):
    if reaches89(i):
        total89 += 1
print(total89)
