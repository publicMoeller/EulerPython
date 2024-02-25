'''Mostly recycling an changing isPan from 0032 here. Also completly unused since I only generate Pan-numbers. I'll leave it here for future reference'''
import sympy
import itertools


def isPan(num:int ,n:int) -> bool:
    """Checks if the arguments taken together are 1 through n pandigital"""
    if n > 9 or n < 1:
        raise ValueError("Pandigitality makes no sense with this parameter")
    check = []
    for digit in str(num):
        if int(digit) == 0 or int(digit) > n:
            return False
        if int(digit) in check:
            return False
        else:
            check.append(int(digit))
    if len(check) == n:
        return True
    else:
        return False
    



def main():
    """generates all 1-to-n-pan numbers for n in [1,...,9], checks for primality and returns the largest"""
    largest = 0
    for n in range(1,10):
        candidates = (list(itertools.permutations(range(1,n+1))))
        for candidate in candidates:
            number = ''
            for digit in candidate:
                number = number + str(digit)
            if sympy.isprime(int(number)):
                largest = int(number)
    print(largest)




if __name__ == '__main__':
    main()