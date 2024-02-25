
import primetools

def distinct(PrimerInstance,n):
    factors = PrimerInstance.factorize(n)
    factors = list(filter(lambda x: x, factors))
    return len(factors)


x = primetools.Primer()
print(distinct(x,1024))
consecutive = 0
starting = 0
test = 1

while True:
    if consecutive == 4:
        print(starting)
        break
    if distinct(x,test) >= 4:
        if consecutive == 0:
            starting = test
        consecutive += 1
    else:
        consecutive = 0     
    test += 1