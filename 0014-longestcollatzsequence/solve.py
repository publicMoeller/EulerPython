
#length known collatz sequences
# Starting with nonsensical 0 to align index and real number
collatz=[0,0]


#fill collatz list up to the nth collatz sequence
def fillCollatz(n):
    while len(collatz) < n:
        candidate = len(collatz)
        running = candidate
        steps = 0
        while running != 1:
            if running%2 == 0:
                running/=2
            else:
                running = 3*running+1
            steps+=1
            if running<=len(collatz)-1:
                collatz.append(collatz[int(running)]+steps)
                break

fillCollatz(999999)
maximum = max(collatz)
print('Maximum is ', maximum, "steps starting with", collatz.index(maximum))