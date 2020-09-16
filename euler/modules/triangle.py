def nextTriNumber(n):
    count = 1
    triNum = 0
    while triNum <= n:
        triNum += count
        count += 1
    return triNum
        
def getDivisors(n):
    divisorList = []
    for i in range(1, int( n / 2) + 1):
        if n % i == 0:
            divisorList.append(i)
    divisorList.append(n)
    return divisorList

def findTriplets(n):
    for i in range(1,n):
        for j in range(i +1, n):
            for k in range(j + 1, n):
                if (i**2 + j**2 == k**2):
                    if (i + j + k == n):
                        return i*j*k
