
from math import sqrt


nth = 10001
primes = [2]
testnext = 3


while (len(primes)<nth):
    for prime in primes:
        if(prime>sqrt(testnext)):
            primes.append(testnext)
            testnext +=2
            break
        if (testnext%prime==0):
            testnext +=2
            break #not a prime then


print(primes)
print('Prime number', nth,'is', primes[-1])