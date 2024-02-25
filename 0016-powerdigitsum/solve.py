


def modpowertwo(n):
    num = 1
    while n > 0:
        n = n-1
        num = 2*truncate(num)
    return num        




def truncate(number):
    while number % 10 == 0:
        number //= 10
    return number


num = modpowertwo(1000)
print(num)

result = 0
for i in str(num):
    result += int(i)
print(result)


