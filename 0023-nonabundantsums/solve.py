
from math import floor
from math import sqrt

def abundant(n):
    divisors = []
    for i in range(1,n):
        if n%i == 0:
            divisors.append(i)
    if sum(divisors) > n:
        return True
    else:
        return False


limit = 28123 # >limit --> is sum of two abundand numbers


numbers = [i for i in range(1,limit+1)]
abundantNumbers = []
for i in range(1,limit):
    print('checking', i)
    if abundant(i):
        abundantNumbers.append(i)


found = []
for a in abundantNumbers:
    for b in abundantNumbers:
        if a<b:
            break
        found.append(a+b)
        
print('found', len(found), 'sums of two')
        
print('deleting now')

result = set(numbers)- set(found)


print(result)
print(sum(result))
            

