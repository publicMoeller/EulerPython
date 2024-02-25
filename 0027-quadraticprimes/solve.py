import primetools

'''checks for specific a,b the number of primes
that are produced from n = 0 onwards'''
def check(primerInstance,a,b):
    n = 0
    while True:
        candidate = n**2 + a*n + b
        if primerInstance.testPrime(candidate):
            n += 1
            #print("found one",a,b,n)
        else: 
            break
    return n


def main():
    x = primetools.Primer()
    maxCount = 0
    maxa = 0
    maxb = 0
    for a in range(-999,1000):
        for b in range(-1000,1001):
            candidate = check(x,a,b)
            if candidate > maxCount:
                maxCount = candidate
                maxa = a 
                maxb = b
    print('Maximal number of primes is',maxCount,'with parameters a:',maxa,'b:',maxb,'and parameter product', maxa*maxb)



if __name__ == '__main__':
    main()
