import sys
import math


def helloworld():
    return 'hello world'

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
def fibit(n):
    a = 0
    b = 1
    if n in (a,b):
        return n
    retval = 1
    for i in range(n - 1):
        retval = a + b
        a = b
        b = retval
    return retval

class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n

        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')
            # Check for computed Fibonacci numbers

        if n >= len(self.cache):
            # Compute and cache the requested Fibonacci number
            self.cache.append(self(n-1)+self(n-2))

        return self.cache[n]

if __name__ == "__main__":
    fib_of = Fibonacci()
    sys.setrecursionlimit(100000)
    print(fib_of(13420))
    sys.setrecursionlimit(1000)
