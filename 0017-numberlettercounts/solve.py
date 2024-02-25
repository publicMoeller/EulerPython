
# THANK EULER EVER THIS IS ENGLISH NUMBERS!!! (Correction: Doing this with any natural language is busywork and a bad idea)
# A bit disappointed by the learning/busywork with this problem

# returns letter count of natural numbers
# between 1 and 1000
def letterCount(n):
    length = 0
    n = str(n)
    if len(n) > 4:
        print("out of scope")
    
    #AND
    if n[-2:] != '00' and n[:-2] != '':
        length += 3


       # Tenners
    compound = False# No idea what they are actually called [eleven, ... ,nineteen ]
    if len(n) >= 2:
        tenner = n[-2] 
        if tenner == '0':
            length += 0 # '  '
        elif tenner == '1':
            compound = True 
            compound = n[-2:]
            if compound == '10':
                length += 3 # 'TEN'
            if compound == '11':
                length += 6 # 'ELEVEN'
            if compound == '12':
                length += 6 # 'TWELVE'
            if compound == '13':
                length += 8 # 'THIRTEEN'
            if compound == '14':
                length += 8 # 'FOURTEEN'
            if compound == '15':
                length += 7 # 'FIFTEEN'
            if compound == '16':
                length += 7 # 'SIXTEEN'
            if compound == '17':
                length += 9 # 'SEVENTEEN'
            if compound == '18':
                length += 8 # 'EIGHTEEN' !!!!! -'T'
            if compound == '19':
                length += 8 # 'NINETEEN'

        elif tenner == '2':
            length += 6 #' TWENTY'
        elif tenner == '3':
            length += 6 #' THIRTY'
        elif tenner == '4':
            length += 5  #' FORTY' ENGLISH WHY??? :O
        elif tenner == '5':
            length += 5 #' FIFTY'
        elif tenner == '6':
            length += 5 #' SIXTY'
        elif tenner == '7':
            length += 7 #' SEVENTY'
        elif tenner == '8':
            length += 6 #' EIGHTY'
        elif tenner == '9':
            length += 6 #' NINETY'
    
    # Units
    if len(n) >= 1:
        unit = n[-1] # no match availible yet :(
        if compound:
            pass
        elif unit == '0':
            length += 0 # '  '
        elif unit == '1':
            length += 3 #'ONE'
        elif unit == '2':
            length += 3 #'TWO'
        elif unit == '3':
            length += 5 #'THREE'
        elif unit == '4':
            length += 4  #'FOUR'
        elif unit == '5':
            length += 4 #'FIVE'
        elif unit == '6':
            length += 3 #'SIX'
        elif unit == '7':
            length += 5 #'SEVEN'
        elif unit == '8':
            length += 5 #'EIGHT'
        elif unit == '9':
            length += 4 #'NINE'
    
 

        
    # Hundreds
    if len(n) >= 3:
        unit = n[-3] # no match availible yet :(
        if unit == '0':
            length += 0 # '  '
        elif unit == '1':
            length += 10 #'ONE HUNDRED'
        elif unit == '2':
            length += 10 #'TWO HUNDRED'
        elif unit == '3':
            length += 12 #'THREE HUNDRED'
        elif unit == '4':
            length += 11  #'FOUR HUNDRED'
        elif unit == '5':
            length += 11 #'FIVE HUNDRED'
        elif unit == '6':
            length += 10 #'SIX HUNDRED'
        elif unit == '7':
            length += 12 #'SEVEN HUNDRED'
        elif unit == '8':
            length += 12 #'EIGHT HUNDRED'
        elif unit == '9':
            length += 11 #'NINE HUNDRED'
    if len(n) >= 4:
        length +=11 #'ONE THOUSAND'
    
    return length


total = 0
for i in range(1,1001):
    print(i ,'has', letterCount(i) ,'letters')
    total +=(letterCount(i))

print(total)

