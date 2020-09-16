from palindrome import isPali

MAXRANGE = 999
MINRANGE = 10
largestPali = 0
for i in range(MINRANGE,MAXRANGE):
    for j in range(i, MAXRANGE):
        if isPali(i*j) and (i * j) > largestPali:
            largestPali = i * j
            print(largestPali)
