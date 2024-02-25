import math
import primetools


primer = primetools.Primer()
factorRequirement = 500


"""
Unfortunately we need to do all the prime decomposition even if we are not interested
in prime factors. e.g having divisibility by 2 and 6 ensuring div by 6 means doing nothing.
for nine we need to increase the amount of prime factor 3 to double occourence.
"""
def maxfactor(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        c.append(max(a.pop(0), b.pop(0)))
    if len(a) != 0:
        c + a
    if len(b) != 0:
        c = c + b
    return c

"""
For triangle number t:
8t+1 is a square number
"""
def isTriangle(n):
    a = math.sqrt(8*n+1)
    b = math.floor(a)
    if a ==b:
        return True
    else:
        return False

"""
find the number of possible divisors for a prime decomposition. 
It should be 2^the occourence of primes. We can choose for every single one
to include it or not, wen mult. our divisor together. Including 0 and all.
"""
def divisors(factors):
    occourences = 1
    for i in factors:
        if i != 0:
            occourences *= i+1
    return occourences
        

"""
Find Number for spectrum
"""
def specToNumber(spectrum):
    number = 1
    pos = 1
    for i in spectrum:
        if i != 0:
            number *= pow(primer.nth(pos),i)
        pos += 1
    return(number)


"""
So i wrote a lot of superflouos stuff and what I intended does not seem to be possible.
because we can not order prime decompositions like[2,1,1] [1,0,0,1]. 
Doing it relatively brute-ish
"""
triangle = 1
step = 1
while True:
    div =divisors(primer.factorize(triangle))
    if  div > factorRequirement:
        break
    print(triangle, div)
    step += 1
    triangle +=  step

print(triangle)


""" I must be overlooking something very obvious. This works but takes far too long.
The Primetools obviously could be faster. But that cannot be all"""