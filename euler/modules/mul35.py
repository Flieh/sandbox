# find the sum of all positive integers less than MAX that are products of 3 or 5
MAX = 1000
acc = 0
i = 1
while i < MAX:
    if (i % 3 == 0) or (i % 5 == 0):
        acc += i
        print(acc)
    i += 1
print(acc)
