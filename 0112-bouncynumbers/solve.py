
from fractions import Fraction


def isBouncy(n: int) -> bool:
    """checks numbers for bouncyness"""
    up = False
    down = False
    last = None
    for i in str(n):
        if last != None and i > last:
            up = True
        if last != None and i < last:
            down = True
        if up and down: # exit early
            return True
        last = i
    return False


def main():
    bouncy = 0
    test = 100
    while True:
        if isBouncy(test):
            bouncy += 1
        if Fraction(bouncy, test) == Fraction(99,100): # exact percentages, no room for representation error
            break
        test += 1
    print(test)

if __name__ == "__main__":
    main()