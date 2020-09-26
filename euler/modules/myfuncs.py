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

def build_pyramid(inp_list):
    pyramid = []
    row = 0
    while len(inp_list) > 0:
        pyramid.append([])
        for i in range(row + 1):
            pyramid[row].append(inp_list.pop(0))
        row += 1
    return pyramid

DIGITS = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
        }
TEENS = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
        }
TENS = {
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
        }

