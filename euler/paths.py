from modules.myfuncs import isPath

max = 21
for j in range(max):
    count = 0
    for i in range(2**(2 * j)):
        if isPath(i, j):
            count += 1
    print(j, count, count / (2**(2*j)))

