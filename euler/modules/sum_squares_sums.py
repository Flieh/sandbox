def sumOfSquares(n):
    acc = 0
    for i in range(1, n + 1):
        acc += i ** 2
    return acc

def squareOfSums(n):
    acc = 0
    for i in range(1, n + 1):
        acc += i
    return acc ** 2

def prodAdj(length, string):
    prodList = []
    for i in range(len(string) - length + 1):
        prod = 1
        for j in range(length):
            prod *= int(string[i + j])
        prodList.append(prod)
    return prodList

def getLargestElement(arr):
    largest = 0
    for i in arr:
        if i > largest:
            largest = i
    return largest
