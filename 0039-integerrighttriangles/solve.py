

def main():
    maxOptions = 0
    maxCircumference = 0 
    circumferrence = 3
    while circumferrence <= 1000:
        options = 0
        print("checking", circumferrence)
        # we need to enforce c > b > a to not count double 
        # I feel like I am missing some obvious way to do less work
        for c in range(circumferrence//2,0,-1):
            for b in range(c,0,-1):
                for a in range(b,0,-1):
                    if a + b + c == circumferrence:
                        if a**2 + b**2 == c**2:   
                           options += 1
                    
        
        if options > maxOptions:
            maxOptions = options
            maxCircumference = circumferrence
            print(maxCircumference, options)
        circumferrence += 1
    print(maxCircumference)
                        


if __name__ == '__main__':
    main()