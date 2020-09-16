# find the sum of all even elements of fibonnaci group while member <= MAX 
MAX = 4000000
acc = 0
el = 1
prevEl = 1 
while el <= MAX:
    if el % 2 == 0:
        acc += el
    newEl = el + prevEl
    prevEl = el
    el = newEl
print(acc)
