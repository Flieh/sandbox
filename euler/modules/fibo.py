# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
<<<<<<< HEAD
    return result[-1]

def memo(func):
    memo = []
    def helper(n):
        if n not in memo:
            memo[n] = func(a)
        return memo[x]
    return helper
=======
    return result

def last_fib(n):
    return fib2(n)[-1]
>>>>>>> d91c550421e88fae43cf94764fe49e2f7fc65784
