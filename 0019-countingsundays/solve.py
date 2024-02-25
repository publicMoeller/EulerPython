"""
So we start on 1900-01-07 because it is 
the first Sunday of the century and just jump through
the weeks
"""

"ISO Date YYYY-MM-DD-Weekday minus the leading zeros plus weekday"
date = [1900,1,1,1]
leapyear = 0

def tomorrow(date):
    monthOver = 0
    global leapyear
    date[2] += 1
    if date[3] == 7:
        date[3] = 1
    else:
        date[3] += 1
    if date[1] == 2 and date[2] > 28+leapyear: # is month over?
        monthOver = 1
    if date[1] in [4,6,9,11] and date[2] > 30:
        monthOver = 1
    if date[1] in [1,3,5,7,8,10,12] and date[2] > 31:
        monthOver = 1
    if monthOver:
        date[1] += 1
        date[2] = 1
        if date[1] > 12:
            date[0] += 1
            date[1] = 1
            date[2] = 1
            if date[0]%4 == 0 and date[0]%400 != 0:
                leapyear = 1
            else:
                leapyear = 0 
    return date

""" go from known monday to starting point"""
while date[0:3] != [1901,1,1]:
    date = tomorrow(date)


"""Test our actual range"""
sundayfirst = 0
while date[0:3] != [2001,1,1]:
    if date[2:4] == [1,7]:
        sundayfirst += 1
    date = tomorrow(date)


print(sundayfirst)
