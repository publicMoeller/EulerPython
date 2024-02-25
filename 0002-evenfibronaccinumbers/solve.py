# Number two does not seem to have any deep trickery to apply either. 
# I'll try to use a generator/yield. 
# Not a typical use case, because we are not building list of memory
# hungry objects, but I want to try.


# Fib starts with 1,2 in our definition, not 1,1 as often seen.
def fibronacciGenerator():
    yield 1
    yield 2
    secondToLast = 1
    last = 2
    while True:
        fib = last + secondToLast
        yield fib
        secondToLast = last
        last = fib
        

generator = fibronacciGenerator()
print(next(generator))
print('starting')
sum = 0


for x in generator: 
    if (x > 4000000):
        break
    if (x%2==0):
        sum+= x
print (' sum of even fibronacci numbers not exceeding 4000000 is:', sum)


""""
Afterthought:
more optimal: Evaluate only every third generator output since fib repeats a pattern of (odd odd even)
since residue classes follow:
odd + odd = even
even + odd = odd + even = odd
Probably neglectable wins in saving on checking compared to the calculations of the generator.
Relevant gains probably only by using a better way to get the Fibronacci numbers.
"""