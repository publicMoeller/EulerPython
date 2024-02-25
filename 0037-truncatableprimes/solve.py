import sympy

def main():
    """finds the sum of all 11 L+R-truncatable primes
    
    - For definitions see: https://projecteuler.net/problem=37
    - we do not proof any properties about candidates, just brute force until we have all
    - remember: 1-digit numbers do not count for our definition
    - we assume primes are small, otherwise we should use a more sophisticated approach anyway 
        - """

    counter = 0 
    sum = 0
    candidate = 11 # first 2-digit prime
    while counter < 11:
        if sympy.isprime(candidate):
            if lrTruncatable(candidate):
                sum += candidate
                counter += 1
                print("found:", candidate)
        candidate = sympy.nextprime(candidate)
    print('Sum of first 11 L+R-truncatable Primes is',sum)
                

def lrTruncatable(candidate:int) -> bool:
    l = str(candidate)
    r = str(candidate)

    # after every loop len(r) = len(l)
    while len(r) > 1:
        r = r[:-1]
        l = l[1:]

        if not sympy.isprime(int(r)):
            return False
        if not sympy.isprime(int(l)):
            return False
    
    return True



if __name__ == '__main__':
    main()