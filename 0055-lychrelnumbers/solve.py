
def isPalindrome(s):
     return ( str(s)[0:]==str(s)[::-1])


def isLychrel(n): # by our experimental standard
    candidate = n
    for i in range(50):
        candidate = int(candidate) + int(str(candidate)[::-1])
        if isPalindrome(candidate):
            print(n,candidate)
            return False
    return True


lychrelCounter = 0
for i in range(1,10000):
    if isLychrel(i):
        lychrelCounter += 1

print(lychrelCounter)
