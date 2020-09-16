def isPali(inp):
    inp = str(inp)
    firstHalf = inp[:int(len(inp) / 2)]
    secondHalf = inp[int(len(inp) / 2):]
    if len(firstHalf) != len(secondHalf):
        secondHalf = secondHalf[1:] 
    secondHalf = secondHalf[::-1]
    if firstHalf == secondHalf:
        return True
    else:
        return False
