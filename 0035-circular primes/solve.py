""" 
Again using copy of primetools, because I do not want to go back to 
every single problem, when changing stuff.

It probably is time to start using numpy and wait less.
"""
import primetools
x = primetools.Primer()
limit = 1000000


def isCircularPrime(n):
    n = str(n)
    if len(n) > 1: #99% of the runtime gone
        for i in n:
            if i == '5':
                return False
            if int(i)%2==0:
                return False
    l = len(n)
    n = n + n[:-1]
    for i in range(l):
        #print(n[i:i+l],x.testPrime(int(n[i:i+l])))
        if not x.testPrime(int(n[i:i+l])):
            return False
    return True



x.testPrime(limit) #fills up our array
primes = x.surrender()
counter = 0

print(primes)

for i in primes:
    if i > limit: #deep and shallow coppies ^^
        break
    if isCircularPrime(i):
        counter += 1
        print(i, "is circPrime")
   
print(counter)

