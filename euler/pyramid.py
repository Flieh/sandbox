from modules.myfuncs import totalPyramid
from modules.myfuncs import getRightPyramid
from modules.myfuncs import getLeftPyramid
from modules.myfuncs import build_pyramid
from modules.flieh import total_first_els
from modules.flieh import total_last_els
from modules.flieh import num_rows_pyr

pyramid_string = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
# pyramid_string = "3 7 4 2 4 6 8 5 9 3"
path = []
pyramid_els = list(map(lambda x: int(x), pyramid_string.split(' ')))
pyramid = build_pyramid(pyramid_els)
while len(pyramid) > 0:
    path.append(pyramid[0][0])
    if total_first_els(pyramid) < total_last_els(pyramid):
        pyramid = getRightPyramid(pyramid)
    else:
        pyramid = getLeftPyramid(pyramid)
print(path)
print(sum(path))
