
import functools



f = open('nums.txt',"r")
lines = f.readlines()
print(str(functools.reduce(lambda a,b: int(a)+int(b),lines))[0:9])