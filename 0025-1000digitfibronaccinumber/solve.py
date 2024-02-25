
digits = 1000
secondtolast = 1
last = 1
now = 2
index = 3

while True:
    if len(str(now)) >= digits:
        break
    # how much would a rotating index be faster?
    secondtolast = last
    last = now
    now = secondtolast + last
    index += 1
print('huge fibronacci number with', digits,'digits is',now,'at index', index)