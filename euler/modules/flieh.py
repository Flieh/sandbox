'''remarks'''


def gen_one(limit):
    '''first get example'''
    for i in range(limit):
        yield i ** i

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def last_fib(n):
    return fib2(n)[-1]

def get_digits(n):
    return len(str(n))

def fib(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def memoize(fun):
    '''decorator to memoize a functions'''
    memo = {}

    def helper(item):
        if item not in memo:
            memo[item] = fun(item)
        # print(memo)
        return memo[item]
    return helper


def num_rows_pyr(num_els):
    '''determine number of pyramid
    rows from number of elements'''
    rows = 0
    count = 0
    while count < num_els:
        rows += 1
        count += rows
    return rows


def total_first_els(pyramid):
    '''return the sum of all first elements in pyramid'''
    total = 0
    for i in range(len(pyramid)):
        total += pyramid[i][0]
    return total


def total_last_els(pyramid):
    '''return the sum of all last elements in pyramid'''
    total = 0
    for i in range(len(pyramid)):
        total += pyramid[i][-1]
    return total
