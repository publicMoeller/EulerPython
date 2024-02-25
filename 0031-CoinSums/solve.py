
# Choose your coin sizes in ascending order and your amount to count options for
coins = [1,2,5,10,20,50,100,200]
MAXAMOUNT = 200


# Initialize lookup table. 0 Otions to form 0 ct from any coins
options = [[0,0,0,0,0,0,0,0]] 


def choose(coin, currentAmount):
    """returns number of options given we choose a certain coin"""
    remaining = currentAmount - coins[coin]
    if remaining < 0:
        return 0

    #use previous computation with no coins larger than choosen here. If the line without the +1 looks weird, read the notes again and be aware that we implicitly have choice by adding the choice method results.
    if remaining == 0:
        return 1 + (options[remaining][coin])
    return (options[remaining][coin])



def create_line(results):
    """computes the next line for the lookuop table from current results"""
    if len(results) != len(coins):
        print('something is very wrong in main')

    line = []
    accumulator = 0
    for option in results:
        accumulator += option
        line.append(accumulator)

    return line



def main():
    currentAmount = 1
    while currentAmount <= MAXAMOUNT:

        # get numbers per choosen coin
        results = []
        for coin in range(len(coins)):
            results.append(choose(coin, currentAmount))

        # append summed up real numbers of options
        options.append(create_line(results))
        currentAmount += 1

    print('lookup table:')
    for i,line in enumerate(options):
        print(i,line)


if __name__ == '__main__':
    main()