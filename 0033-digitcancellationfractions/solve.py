
from fractions import Fraction

def naiveChanel(numerator, denominator):
    """Produces the value for the interesting chaneling procedure
    
    returns None if no viable candidate, fraction type otherwise.
    Implementation strongly depends on numerator < denominator"""
    if str(numerator)[0] == str(denominator)[1]:
        if str(numerator)[1] == str(denominator)[0]:
            return None
            # fraction value would be 1, therefore != true value
        else:
            if int(str(denominator)[0]) == 0:
                return None
            return Fraction(int(str(numerator)[1]), int(str(denominator)[0]))
    else:
        if str(numerator)[1] == str(denominator)[0]:
            if int(str(denominator)[1]) == 0:
                return None
            return Fraction(int(str(numerator)[0]), int(str(denominator)[1]))

    if str(numerator)[0] == str(denominator)[0]:
        if int(str(denominator)[1]) == 0:
            return None
        return Fraction(int(str(numerator)[1]), int(str(denominator)[1]))

    if str(numerator)[1] == str(denominator)[1] and str(numerator)[1] != '0':
        if int(str(denominator)[0]) == 0:
            return None
        return Fraction(int(str(numerator)[0]), int(str(denominator)[0]))
    


def main():
    accumulator = Fraction(1,1)
    for denominator in range(10,100):
        for numerator in range(10,denominator):
            if Fraction(numerator, denominator) ==  naiveChanel(numerator, denominator):
                accumulator *= naiveChanel(numerator,denominator)
            #    print(numerator, denominator, naiveChanel(numerator, denominator))
            
    print('product of all terms is:',accumulator)

if __name__ == '__main__':
    main()

