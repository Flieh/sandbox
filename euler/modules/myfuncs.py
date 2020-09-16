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
    else:
        return False

def isPath(n,sides):
    if str(bin(n)).count('1') == sides:
        return True
    else:
        return False

