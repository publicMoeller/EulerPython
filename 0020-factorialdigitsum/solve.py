
#further opt: cut off tailing 0s
# Our problem is not really large
# enough start doing that.

N = 100

def factorial(n):
    acc = 1
    for x in range(1,n):
        acc*=x
    return acc


hugenum= factorial(N)
print(hugenum)
# using string seems weird. better options?
digits = [int(d) for d in str(hugenum)]

sum = sum(digits)
print('digit sum:',sum)
