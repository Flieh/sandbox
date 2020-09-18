TARGET = 500 
triangle = [[1]]
for i in range(TARGET):
    row = []
    for j in range(len(triangle[i]) + 1):
        if j == 0:
            row.append(1)
        elif j == len(triangle[i]):
            row.append(1)
        else:
            row.append(triangle[i][j - 1] + triangle[i][j])
    triangle.append(row)
    if len(row) % 2 > 0:
        print(row[int(len(row)/2)])
