from math import sqrt

"""
A tiny class that holds an array of primes that it fills in accordance
with current needs. 
Id does
- testing for primes
- returns the nth prime
-surrenders all previously calculated primes or a slice of the list
- calculates a vector containing the incidences of all prime factors of a number

TODO:
    - Use numpy to not be horribly slow
    - ensure the slicing tolerance that standard slicing has
    - estimate position when searching for nth prime and search more 
    intelligently for it
    - add the number of divisors function built into a problem recently
    - add the function to built built a number from the array of factor incidences
"""
class Primer:
    
    
    def __init__(self):
        self.primes = [2,3]

    # method for expanding the array of primes to a size target
    def expand(self,target):
        testnext = self.primes[-1]+2
        while (len(self.primes)<target):
            for prime in self.primes:
                if(prime>sqrt(testnext)):
                    self.primes.append(testnext)
                    testnext +=2
                    break
                if (testnext%prime==0):
                    testnext +=2
                    break #not a prime then



    def testPrime(self,n):
        # slow obviously.
        # Either use prime number theorem and search from there
        # or use sorted property to repeatedly half search space
        primePointer = 0
        limit = len(self.primes)-1
        while self.primes[primePointer] < n:
            if primePointer == limit:
                self.expand(limit+100)
                limit = len(self.primes)-1
            primePointer +=1
        if self.primes[primePointer] == n:
            return True
        else:
            return False
        return False


    # Print all found primes or a certain amount
    def primeprint(self, amount=0):
        if amount == 0:
            amount = len(self.primes)
        else:
            self.expand(amount)
        for i in range(1,len(self.primes)+1):
            print('prime number ',i,' is: ',self.primes[i-1])
    

    # returns the whole stored array or a slice if optional parameters used
    def surrender(self, start = 0, stop = 0, step = 1):
        if stop == 0 and step == 1:
            return self.primes
        else:
            if stop != 0:
                self.expand(stop)
                return self.primes[start:stop:step]
            else:
                return self.primes[::step]


    # returns nth prime
    def nth(self,n):
        if n > len(self.primes):
         self.expand(n)
        return self.primes[n-1]
    
    # returns array with incidences of prime factors
    # e. g. [2,0,2,2] for 4988
    def factorize(self,n):
        self.testPrime(n) # easy way to fill up to the highest prime needed
        factors = []

        for prime in self.primes:
            count = 0
            #print("testing for", prime)
            while n%prime==0:
                n = n//prime
                count += 1
            factors.append(count)
            count = 0 
            #print(factors)
            if n == 1:
                break
        return factors
            
            






