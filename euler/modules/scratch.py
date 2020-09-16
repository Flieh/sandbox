import prime

largestPrimeFactor = 0
TARGET =  600851475143
# TARGET =  6008514751431
i = 1

while i < (int(TARGET ** 0.5)) :
    if prime.isFactor(i, TARGET):
        largestPrimeFactor = i
        print(largestPrimeFactor)
    i = prime.nextPrime(i)

