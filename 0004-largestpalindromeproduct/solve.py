
import string

limit=1000

# Tiny palindrome checker
def ispalindrome(s):
    #print(str(s)[0:])
    #print(str(s)[::-1])
    #print( str(s)[0:]==str(s)[::-1])
    return ( str(s)[0:]==str(s)[::-1])




highest = 0
for i in range(limit):
    for j in range (i+1):
        candidate = i*j
        #print('considering', candidate)
        if candidate>highest:
            #print('higher')
            if (ispalindrome(candidate)):
                highest = candidate

print(highest)



