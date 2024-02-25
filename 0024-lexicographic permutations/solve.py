
# Brute force! (see notes)

'''Itertools returns lexicographically ordered according to input order'''    
from itertools import permutations
numbers = [0,1,2,3,4,5,6,7,8,9]
permList = list(permutations(numbers))
print(permList[0])
print(permList[-1])
print(permList[999999])


