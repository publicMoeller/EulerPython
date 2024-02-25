# No real gains over checking everything and adding are obvious
# "below not until 1000 is weird. solution a nice number but solution +1000 ugly?


sum = 0

for i in range(1,1000):
    if (i%3==0 or i%5==0):
        sum +=i
print('sum is: ', sum)

#solution is 233168
# If 233168 is more special than 234168 I do not see it.