digits = []
next = 1
while len(digits) < 1000000:
    for i in str(next):
        digits.append(i)
    next += 1


total = 1
for i in range(7):
    total *= int(digits[10**i-1])

print(total)
