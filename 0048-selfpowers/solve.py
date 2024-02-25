
""" we will hold our number relatively 
small by using modulo on the summands 
(thx python for modular pow saves a few lines.
We only threw away the few extra digits that
accumulate once at the and"""

digits = 0
for i in range(1,1001):
    digits += pow(i,i,10000000000)

print(digits%10000000000)