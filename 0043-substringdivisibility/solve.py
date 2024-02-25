import itertools


def checkDivisibility(candidate:str) -> bool:
    if not int(candidate[1:4])%2 == 0:
        return False
    

    if not int(candidate[2:5])%3 == 0:
        return False
    

    if not int(candidate[3:6])%5 == 0:
        return False
   

    if not int(candidate[4:7])%7 == 0:
        return False
    

    if not int(candidate[5:8])%11 == 0:
        return False


    if not int(candidate[6:9])%13 == 0:
        return False
    

    if not int(candidate[7:10])%17 == 0:
        return False
    
    return True

def main():
    pool = '0123456789'
    pool = list(itertools.permutations(pool))
    total = 0

    for perm in pool:
        candidate = (''.join(perm))
        if checkDivisibility(candidate):
            total += int(candidate)
            

    print(total)




if __name__ == '__main__':
    main()