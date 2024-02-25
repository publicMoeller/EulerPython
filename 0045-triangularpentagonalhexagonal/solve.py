"""
-build 3 generator functions
-increment the lowest untill all three are equal
- append that number to a list
- we do not care for indexes
"""

# how many do we want to find? (3 to just solve the problem)
wanted = 3
def TriangleGenerator():
    i = 1
    while True:
        yield (i*i+i)//2
        i +=1

def PentagomGenerator():
    i = 1
    while True:
        yield (3*i**2-i)//2
        i +=1

def HexagonGenerator():
    i = 1
    while True:
        yield 2*i**2-i
        i +=1


# find the actual numbers
tri = TriangleGenerator()
pen = PentagomGenerator()
hex = HexagonGenerator()

triCandidate = next(tri)
penCandidate = next(pen)
hexCandidate = next(hex)
results = []

while True:
    if triCandidate == penCandidate == hexCandidate:
        results.append(triCandidate)
        triCandidate = next(tri)
        penCandidate = next(pen)
        hexCandidate = next(hex)
        if len(results) >= wanted:
            break
    maximum =max(triCandidate,penCandidate,hexCandidate)

    if triCandidate < maximum:
        triCandidate = next(tri)

    if penCandidate < maximum:
        penCandidate = next(pen)

    if hexCandidate < maximum:
        hexCandidate = next(hex)

print(results)