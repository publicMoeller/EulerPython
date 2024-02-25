"""
No elaborate ways to enumerate wothout doubling digits, just brute force, should be fast enough.
- Smarter skipping numbers
"""


def isPan(*nums):
    """Checks if the arguments taken together are 1 through 9 pandigital"""
    
    check = []
    for num in nums:
        for digit in str(num):
            if int(digit) == 0:
                return False
            if int(digit) in check:
                return False
            else:
                check.append(int(digit))
    if len(check) == 9:
        return True
    else:
        return False
    

def isSubPan(*nums):
    """Checks if the arguments taken together can be completed to be 1 through 9 Pandigital
    
    Note that isPan(*something) -> NOT isSubPan(*something) because we cannot add anything without making it not pan"""
    
    check = []
    for num in nums:
        for digit in str(num):
            if int(digit) == 0:
                return False
            if int(digit) in check:
                return False
            else:
                check.append(int(digit))
    if len(check) < 9:
        return True
    else:
        return False


def main():
    total = 0
    for product in range(1,10000):
        #print('checking',product)
        if isSubPan(product):
            for multiplicand in range (1,product+1):
                if product%multiplicand == 0 and isPan(product,multiplicand,int(product/multiplicand)):
                    total += product
                    print("found",product,'=',multiplicand,'*',int(product/multiplicand),"sum:",total)
                    break
    print('Solution is:',total)
                    


    






if __name__ == '__main__':
    main()