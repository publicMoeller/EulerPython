import math



def digitFactorial(n):
    result = 0 
    for i in str(n):
        result += math.factorial(int(i))
    return result


total = 0
for i in range(10, 10**7):
    if digitFactorial(i) == i:
        print('found', i)
        total += i
print(total)

