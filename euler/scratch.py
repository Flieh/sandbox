from modules.flieh import gen_one

TIMES = 5000
a = gen_one(TIMES)
for i in range(TIMES):
    print(next(a))

