from modules.myfuncs import countCollatz

MAX = 1000000
maxTerms = 0
for i in range(1, MAX):
    if countCollatz(i) > maxTerms:
        maxTerms =  countCollatz(i)
        print(i, ' , ', maxTerms)

    
