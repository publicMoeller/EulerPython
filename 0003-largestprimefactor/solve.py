"""This would be somewhat more effective if we were to calculate a list of primes first.
but that will be in a later problem anyway. We are going primitive here.
Only optimisazion will be shrinking the number by dividing by the found prime
factors and stopping when it is prime"""

import itertools
num = 600851475143

for i in itertools.chain( [2], range(3,num+1, 2)):
    if (i >= num):
        break
    while (num%i==0):
        num= num//i
    
print(num)