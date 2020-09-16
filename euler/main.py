from modules.triangle import nextTriNumber
from modules.triangle import getDivisors
from time import perf_counter as pc

startTime = pc()
MAX = 100000
triNum = 1
largestListLen = 0
for i in range(MAX):
    if len(getDivisors(triNum)) > largestListLen:
        largestListLen = len(getDivisors(triNum))
        print(triNum, ': ', len(getDivisors(triNum)), pc()- startTime) 
    triNum = nextTriNumber(triNum)

# from time import perf_counter as pf

# def csv_reader(file_name):
#     file = open(file_name)
#     result = file.read().split("\n")
#     return result

# def csv_reader(file_name):
#     for row in open(file_name, "r"):
#         yield row

# start = pf()
# csv_gen = csv_reader("10000-sales-records.csv")
# row_count = 0

# for row in csv_gen:
#     row_count += 1

# print(f"Row count is {row_count}")
# end = pf()
# print(end - start)
