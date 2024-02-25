

'''
If the implementation of modular pow is efficient (not doing
the complete exponentiation first) this should be elementary
'''

exp = pow(2,7830457,10000000000)
prime = ((28433*exp)%10000000000)+1
print(prime)