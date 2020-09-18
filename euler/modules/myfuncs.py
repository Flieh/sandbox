def countCollatz(n):
    count = 0
    while n != 1:
        count += 1
        if isEven(n):
            n = n/2
        else:
            n = n * 3 + 1
    return count

def isEven(n):
    if n % 2 == 0:
        return True
    return False

def isPath(n,sides):
    if str(bin(n)).count('1') == sides:
        return True
    return False

def totalPyramid(pyramid):
    total = 0
    for i in range(len(pyramid)):
        for j in pyramid[i]:
            total += j
    return total

def getRightPyramid(p):
    new_p = []
    for i in range(len(p)):
        if i == 0:
            continue
        row = []
        for j in range(len(p[i])):
            if j == 0:
                continue
            row.append(p[i][j])
        new_p.append(row)
    return new_p

def getLeftPyramid(p):
    new_p = []
    for i in range(len(p)):
        if i == 0:
            continue
        row = []
        for j in range(len(p[i])):
            if j == len(p[i]) - 1:
                continue
            row.append(p[i][j])
        new_p.append(row)
    return new_p
