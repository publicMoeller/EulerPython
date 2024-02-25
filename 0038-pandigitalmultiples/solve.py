

def isPan(num:int) -> bool:
    """Checks if the arguments taken together are 1 through 9 pandigital"""
    
    check = []
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



def conProd(candidateSeed: int) -> int:
    """calculates the concatenated product with candidateSeed

    returns 9-digit concatenated product if ever reached
    returns 0 if not pandigital or no step with 9 digits exists """
    multiple = 1
    candidate = []
    while len(candidate) < 9:
        candidate.extend(str(multiple*candidateSeed))
        multiple += 1
        

    if len(candidate) > 9:
        return 0

    candidate = int(''.join(candidate))
    
    # length is 9
    if isPan(candidate):
        return candidate
    else:
        return 0
   



def main():
    candidateSeed = 1
    biggest = 0
    # 5-digit candidates lead to more than 9 digits afer concatenating
    while candidateSeed <= 9999:
        this = conProd(candidateSeed)
        if this > biggest:
            biggest = this

        candidateSeed += 1
    print("Biggest concatendated product is:",biggest)
    candidateSeed += 1



if __name__ == '__main__':
    main()