
import math

def stringValue(letter):
    return(ord(letter)-64)
    
def wordValue(word):
    total = 0
    for letter in word:
        total += stringValue(letter)
    return total

def isTriangle(number):
    test = 8*number + 1
    root = math.floor(math.sqrt(test))
    if root**2 == test:
        return True
    else:
        return False

'In some prior problem I learned: An integer x is triangular if and only if 8x + 1 is a square'
    
# read in


# read in
rawnames = []
f = open('0042-codedtrianglenumbers/p042_words.txt','r')
lines = f.readlines()
for l in lines:
    l=l.split(',')
    rawnames.append(l)

rawnames = rawnames[0] #just one line
names = []
for rawname in rawnames:
    name = rawname.replace('"',"")
    names.append(name)


total = 0 
for name in names:
    print(name, wordValue(name),isTriangle(wordValue(name)))
    if isTriangle(wordValue(name)):
        total += 1
print(total)
