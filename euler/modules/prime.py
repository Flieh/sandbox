# prime function module

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    # print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True 

def nextPrime(n):
    n = n + 1
    while not isPrime(n):
        n = n + 1
    return n

def isFactor(n, t):
    if n == 0:
        return False
    elif t % n == 0:
        return True
    else:
        return False

def getNthPrime(n):
    prime = 2
    for i in range(1, n):
        prime = nextPrime(prime) 
    return prime
