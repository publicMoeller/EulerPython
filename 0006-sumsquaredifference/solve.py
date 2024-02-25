
"""we even have explicit formulas for these :)
Obviously eulers formula for sums and not so obviously
square pyramidal numbers or more general Faulhaber's formula
for sums of powers
"""

num = 100


def squaresum(n):
    return (2*pow(n,3)+3*n*n+n)//6

def sumsquare(n):
    return pow(((n*n+n))//2,2)

print(sumsquare(num)-squaresum(num))
