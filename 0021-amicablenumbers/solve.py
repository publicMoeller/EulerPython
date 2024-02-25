

def potentialFriend(num):
    divisors = []
    for div in range(1,num):
        if num%div == 0:
            divisors.append(div)
    return(sum(divisors))


total = 0
for n in range(1,10000):
    '''we could test whole chains and remove elements
    from the list but this seems fast enough'''
    candidate = potentialFriend(n)

    if candidate != n and potentialFriend(candidate) == n:
        total += n
        print('found', n)
print(total)




