
"""
Just copied primetools here.
It will probably change a lot in the future.

Idea:
Get the list of all lists of prime factors of all wanted divisors and merge them to have the maximum between
all lists for every single prime factor.

Why do we need all of them? (== Is this really the smalles possible number?)
If one list contains x^n it is needed because we wanted to have divisibility either
by x^n or by x^n*something, therefore we need them all, because we want to keep our new number divisible by that.

Why is it enough? 
Every divisor we want is a product from a subset of the multiset of all the divisors. Using the highest occourence
for all factors guarantees not having any shrinkage in possible combinations comparing any of the
multisets to the combined one.

"""
import primetools
primer = primetools.Primer()

# get list of lists of prime factors fo all divisors
N = 20
allFactors = []
for n in range(2,N+1):
    allFactors.append(primer.factorize(n))



    

l = 0
for i in allFactors:
    if len(i)>l:
        l= len(i)



factors = []

for i in range(l):
    highest = 0
    candidate = 0
    for set in allFactors:
        
        if len(set) > 0:
            candidate = set.pop(0)
        if candidate > highest:
            highest = candidate
    factors.append(highest)


primes = primer.surrender(start=0, stop=l)

acc = 1
for i in range(l):
    localAcc = pow(primes[i],factors[i])
    if localAcc != 0:
        acc *= localAcc
print(acc)
