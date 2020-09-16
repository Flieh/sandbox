def divAll(d,t):
    if d == 1:
       return True
    else:
        if t % d == 0:
            return divAll(d - 1, t)
    return False

DIVS = 10
target = DIVS
flag = False

while not divAll(DIVS, target):
        target += 1

    print(target)

