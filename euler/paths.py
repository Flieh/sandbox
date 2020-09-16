from modules.myfuncs import isPath

count = 0
SIDES = 20
for i in range(2**(2 * SIDES)):
    if isPath(i, SIDES):
        print(i,)
        count += 1
        print(count)
