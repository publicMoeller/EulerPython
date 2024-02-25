
from math import sqrt


limit= 2000000
primes = [2]
testnext = 3


while (primes[-1]<limit):
    if testnext >=limit:
        break
    for prime in primes:
        if(prime>sqrt(testnext)):
            primes.append(testnext)
            testnext +=2
            break
        if (testnext%prime==0):
            testnext +=2
            break #not a prime then


print(sum(primes))