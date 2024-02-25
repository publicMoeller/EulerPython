

def digitsum(n):
    total = 0
    for i in str(n):
        total += (int(i)**5)
    return total

"""
10^x = x*(9^5) 
The relevant point is about
x = 5.51 so we test till 6 digits
"""
total = 0
test = 10 # single digit -> not a sum
while len(str(test)) <= 6:
    if test == digitsum(test):
        total += test
        print(test)
    test +=1

print(total)
