

def isPalindrome(s):
     return ( str(s)[0:]==str(s)[::-1])


total = 0
for i in range(1,1000000):
    if isPalindrome(i) and isPalindrome(bin(i)[2:]):
        total += i 

print(total)
