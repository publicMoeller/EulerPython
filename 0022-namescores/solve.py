
# converts UPPERCASE letters to pos in alphabet via Unicode
def stringValue(letter):
    return(ord(letter)-64)
    
def wordValue(word):
    total = 0
    for letter in word:
        total += stringValue(letter)
    return total



# read in
rawnames = []
f = open('0022-namescores/p022_names.txt','r')
lines = f.readlines()
for l in lines:
    l=l.split(',')
    rawnames.append(l)

rawnames = rawnames[0] #just one line
names = []
for rawname in rawnames:
    name = rawname.replace('"',"")
    names.append(name)

print(names)
names = sorted(names)


total = 0
for i in range(len(names)):
    total += (i+1)*wordValue(names[i])
    
print(total)