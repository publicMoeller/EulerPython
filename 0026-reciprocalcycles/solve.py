
def cycle(numerator, denominator):
    done = False
    states = []
    while not done:
        state = ((numerator//denominator, numerator%denominator))
        for i in states:
            if i == state:
                done = True
                break
        if done:
            return(len(states) - states.index(state))  
        else: 
            states.append(state)
        if states[-1][-1] == 0: # no cycle
            return 0
        numerator = (numerator%denominator)*10
        
    


def main():
    maximum = 0
    maxDenominator = 0
    for i in range(1,1000):
        thisCycle = cycle(1,i)
        if thisCycle > maximum:
            maximum = thisCycle
            maxDenominator = i
    print('At 1  /',maxDenominator ,'maximum cycle length of', maximum)


if __name__ == '__main__':
    main()