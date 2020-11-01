# from modules.flieh import gen_one

# TIMES = 5000
# a = gen_one(TIMES)
# for i in range(TIMES):
#     print(next(a))
from modules.myfuncs import DIGITS, TEENS, TENS

count = 0
for i in range(1, 1000):
    out_string = ''
    if len(str(i)) > 2:
        out_string += DIGITS.get(int(str(i)[-3]))
        if str(i)[-2] == '0' and str(i)[-1] == '0':
            out_string += 'hundred'
        else:
            out_string += 'hundredand'
    if len(str(i)) > 1:
        if str(i)[-2] == '1':
            out_string += TEENS.get(int(str(i)[-1]))
        else:
            out_string += TENS.get(int(str(i)[-2]))
            out_string += DIGITS.get(int(str(i)[-1]))
    else:
        out_string += DIGITS.get(int(str(i)[-1]))
    count += len(out_string)
print(count)
