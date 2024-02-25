"""
It can be seen that the number, $125874$, and its double, $251748$, contain exactly the same digits, but in a different order.
Find the smallest positive integer, $x$, such that $2x$, $3x$, $4x$, $5x$, and $6x$, contain the same digits.
"""


def main() -> int:
    testee = 1
    found = False
    while not found:
        testeeString = sorted(str(testee))
        for i in range(2,7):
            if sorted(str(i*testee)) != testeeString:
                break
            if i == 6:
                found = True
        if found:
            print(testee)
            return testee
        testee += 1
        
if __name__ == '__main__':
    
    main()
    
